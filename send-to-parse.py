import json,httplib
connection = httplib.HTTPSConnection('api.parse.com', 443)
connection.connect()
connection.request('POST', '/1/files/hello.txt', 'Hello, World!', {
       "X-Parse-Application-Id": "kKW7oJS0nwEG4V6f3LvYooU5BQxFnH6eZ9aS31A3",
       "X-Parse-REST-API-Key": "HEZHvUyEqV4VOV61YaEFbMywGKq7pJNlPhlQtWRt",
       "Content-Type": "text/plain"
     })
result = json.loads(connection.getresponse().read())
print result
