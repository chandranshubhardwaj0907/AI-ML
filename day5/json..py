# javascript object notation
import json

json_str = '{ "name" : "Chandranshu","age" : 21, "city" : "Patiala", "address" : { "country" : "India", "state" : "Punjab", "street" : "123 Main"}}'

py_obj = json.loads(json_str)

print(type(py_obj), py_obj)
