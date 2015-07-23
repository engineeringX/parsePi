import json,httplib

appID = "kKW7oJS0nwEG4V6f3LvYooU5BQxFnH6eZ9aS31A3"
apiKey = "HEZHvUyEqV4VOV61YaEFbMywGKq7pJNlPhlQtWRt"
uploadFilename = "samples.txt"

connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('POST', '/1/files/' + uploadFilename, open(uploadFilename, 'rb').read(), {
       "X-Parse-Application-Id": appID,
       "X-Parse-REST-API-Key": apiKey,
       "Content-Type": "text/plain"
     })

result = json.loads(connection.getresponse().read())
filename = result["name"]
print filename + ' uploaded'

#Uploaded the file to Parse
#Now associate it with Event Object
connection.request('POST','/1/classes/EventObject', json.dumps({
    "name": "Sample",
    "data": {
        "name": filename,
        "__type": "File"
         }
    }), {
        "X-Parse-Application-Id": appID,
        "X-Parse-REST-API-Key": apiKey,
        "Content-Type": "applicaton/json"
     }
    )
result = json.loads(connection.getresponse().read())
print filename + ' associated with object ' + result["objectId"]
