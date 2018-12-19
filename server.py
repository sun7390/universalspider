#coding=utf-8
from flask import Flask
from flask.ext.pymongo import PyMongo
import json
app = Flask(__name__)
app.config.update(
	MONGO_URI = 'mongodb://localhost:27017/DEMO',
)
mongo = PyMongo(app)
@app.route('/')
def home_page():
	posts = []
	data = mongo.db['1'].find()
	for p in data:
		p.pop('_id')
		for i,j in enumerate(p):
			p[j].encode('utf-8').decode('unicode_escape')
		posts.append(p)
	thejson = json.dumps({'result':posts})
	return thejson
if __name__ == '__main__':
	app.run(debug=True)
