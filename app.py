from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# Replace this URI with your actual MongoDB Atlas connection string
client = MongoClient("mongodb+srv://sivaprabhakaran2311069:siva%401502@cluster0.lg64dov.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client["pharmacy"]
collection = db["medicines"]

@app.route('/medicines', methods=['GET'])
def get_medicines():
    meds = list(collection.find({}, {'_id': 0}))
    return jsonify(meds)

@app.route('/add', methods=['POST'])
def add_medicine():
    data = request.get_json()
    collection.insert_one({
        "name": data['name'],
        "price": data['price'],
        "quantity": data['quantity']
    })
    return jsonify({"message": "Medicine added successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
