import ast

def mongoToDict(object):
	obj = ast.literal_eval(object.to_json())
	obj['id'] = obj['_id']['$oid']
	obj['_id'] = obj['id']

	return obj
