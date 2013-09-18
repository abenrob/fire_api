#!venv/bin/python
from flask import Flask, jsonify, abort, make_response
import urllib2
import csv
root_url = 'http://activefiremaps.fs.fed.us/data/lg_fire/'

app = Flask(__name__)

@app.route('/fire/api/v1.0/<datestring>', methods = ['GET'])
def get_fires(datestring):
	try:
		response = urllib2.urlopen(root_url+'lg_fire_nifc_'+datestring+'.csv')
		remotecsv = response.read().split('\n')
		datarows = remotecsv[1:]
		reader = csv.reader(datarows)
		data_out = [];
		counter = 0
		for row in reader:
			if len(row) == 6:
				latitude, longitude, fire_name, fire_number, area, report_date = row
				row_out = {}
				row_out['latitude'] = latitude
				row_out['longitude'] = longitude
				row_out['fire_name'] = fire_name
				row_out['fire_number'] = fire_number
				row_out['area'] = area
				row_out['report_date'] = report_date
				data_out.append(row_out)
				#print latitude, longitude, fire_name, fire_number, area, report_date
			counter+=1
		response.close()  # close the file
		return jsonify({'fires': data_out, 'date': datestring})
	except urllib2.HTTPError as e:
		abort(404)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

if __name__ == '__main__':
    app.run(debug = True)