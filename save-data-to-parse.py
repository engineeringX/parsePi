import json,httplib

accel_scaling = 2**15
gyro_scaling = 131
temp_scaling = 0.03125
pulse_scaling = 1024

appID = "kKW7oJS0nwEG4V6f3LvYooU5BQxFnH6eZ9aS31A3"
apiKey = "HEZHvUyEqV4VOV61YaEFbMywGKq7pJNlPhlQtWRt"

connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()

def read_file():
	f = open('samples.txt')
	chunks = []

	for line in iter(f):
		line = line.replace("\n","")
		line = line.replace(" ","")
		line = line.split(',')

		chunks.append(line)

	f.close()
	parse_chunks(chunks)

def parse_chunks(chunks):
	chunks_length = len(chunks)

	a_x_list = []
	a_y_list = []
	a_z_list = []
	g_x_list = []
	g_y_list = []
	g_z_list = []
	tmp_list = []
	pul_list = []

	# Arbitrary chunk size
	chunk_size = chunks_length % 10

	for i in xrange(0, chunks_length, chunk_size):
		chunk = chunks[i: i + chunk_size];
		for x in range(0, len(chunk)):
			a_x_list.append(float(chunk[x][0]))
			a_y_list.append(float(chunk[x][1]))
			a_z_list.append(float(chunk[x][2]))
			g_x_list.append(float(chunk[x][3]))
			g_y_list.append(float(chunk[x][4]))
			g_z_list.append(float(chunk[x][5]))
			tmp_list.append(float(chunk[x][6]))
			pul_list.append(float(chunk[x][7]))

		a_x_avg = (sum(a_x_list)/float(len(a_x_list))) / accel_scaling
		a_y_avg = (sum(a_y_list)/float(len(a_y_list))) / accel_scaling
		a_z_avg = (sum(a_z_list)/float(len(a_z_list))) / accel_scaling
		g_x_avg = (sum(g_x_list)/float(len(g_x_list))) / gyro_scaling
		g_y_avg = (sum(g_y_list)/float(len(g_y_list))) / gyro_scaling
		g_z_avg = (sum(g_z_list)/float(len(g_z_list))) / gyro_scaling
		tmp_avg = (sum(tmp_list)/float(len(tmp_list))) * temp_scaling
		pul_avg = (sum(pul_list)/float(len(pul_list))) / pulse_scaling

		upload_data = [a_x_avg, a_y_avg, a_z_avg, g_x_avg, g_y_avg, g_z_avg, tmp_avg, pul_avg]
		print upload_data
		upload(upload_data)

def upload(upload_data):
	connection.request('POST','/1/classes/EventObject', json.dumps({
	    "a_x": float(upload_data[0]),
	    "a_y": float(upload_data[1]),
	    "a_z": float(upload_data[2]),
	    "g_x": float(upload_data[3]),
	    "g_y": float(upload_data[4]),
	    "g_z": float(upload_data[5]),
	    "tmp": float(upload_data[6]),
	    "pul": float(upload_data[7])
	    }), {
	        "X-Parse-Application-Id": appID,
	        "X-Parse-REST-API-Key": apiKey,
	        "Content-Type": "applicaton/json"
	     })
	result = json.loads(connection.getresponse().read())

read_file()
