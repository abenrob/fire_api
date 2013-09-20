#!venv/bin/python
from flask import Flask, abort, make_response, jsonify, redirect, request, render_template, url_for
import re, urllib2, csv
from functools import wraps

app = Flask(__name__)

def support_jsonp(f):
    """Wraps JSONified output for JSONP"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            content = str(callback) + '(' + str(f(*args,**kwargs).data) + ')'
            return app.response_class(content, mimetype='application/javascript')
        else:
            return f(*args, **kwargs)
    return decorated_function
@app.route('/')
def api_root():
	return render_template('api-root.html')

@app.route('/api/v1.0/<datestring>', methods = ['GET'])
@support_jsonp
def get_fires(datestring):
	root_url = 'http://activefiremaps.fs.fed.us/data/lg_fire/'
	"""matches date format YYYY-MM-DD"""
	r = re.compile('[1-9][0-9]{3}-[0-1][0-9]-[0-3][0-9]') 
	datematch = r.match(datestring)
	"""if a valid date format"""
	if datematch:
		try:
			response = urllib2.urlopen(root_url+'lg_fire_nifc_'+datestring+'.csv')
			datarows = response.read().split('\n')[1:] #drop header
			reader = csv.reader(datarows)
			data_out = {'type': 'FeatureCollection','features': []};
			counter = 0
			for row in reader:
				if len(row) == 6:
					counter+=1
					latitude, longitude, fire_name, fire_number, area, report_date = row
					row_out = {'type':'Feature','id':counter,
								'geometry':{'type':'Point','coordinates':[float(longitude),float(latitude)]},
								'properties':{'fire_name':fire_name,'fire_number':fire_number,'area':area,'report_date':report_date}}
					data_out['features'].append(row_out)				
			response.close()  # close the file
			return jsonify({'status':'success','geojson': data_out, 'date': datestring})
		except urllib2.HTTPError as e:
			return jsonify({'status':'error','error': 'no data', 'parameter': datestring})
	else:
		return jsonify({'status':'error','error': 'not valid date (format YYYY-MM-DD)', 'parameter': datestring})

@app.errorhandler(404)
@support_jsonp
def not_found(error):
    return jsonify({ 'error': 'Not found' })

if __name__ == '__main__':
    app.run(debug = True)