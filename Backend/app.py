from flask import Flask, request, jsonify
from dotenv import load_dotenv 
import os, pymongo

load_dotenv()
Mongo_uri = os.getenv("Mongo_uri")

if not Mongo_uri:
     raise ValueError("Mongo_uri not found in .env file")

try:
     client = pymongo.MongoClient(Mongo_uri, serverSelectionTimeoutMS=5000)
     client.admin.command('ping')
     db = client.test
     collection = db['ToDoPage_DB']
except pymongo.errors.ServerSelectionTimeoutError:
     raise ConnectionError("Failed to connect to MongoDB. Check your Mongo_uri in .env")

app = Flask(__name__)

@app.route('/submit',methods=['POST'])
def submit():
     try:
          form_data = dict(request.json)
          if not form_data:
               return jsonify({'error': 'No data provided'}), 400
          result = collection.insert_one(form_data)
          return jsonify({'message': 'Submitted Successfully', 'id': str(result.inserted_id)}), 201
     except Exception as e:
          return jsonify({'error': str(e)}), 500

@app.route('/view')
def view():
     try:
          data = list(collection.find())
          
          for i in data:
               i['_id'] = str(i['_id'])

          return jsonify({'data': data}), 200
     except Exception as e:
          return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
     app.run(host='localhost',port=5000,debug=True)
