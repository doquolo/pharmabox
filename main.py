from flask import Flask, render_template, request, jsonify
import json

import firebase_admin
from firebase_admin import firestore

creds = firebase_admin.credentials.Certificate("firebase_creds.json")
default_app = firebase_admin.initialize_app(creds)
firestore = firestore.client()
# import pharmabox_helper

with open("stationInfo.json", "r", encoding='utf-8') as file:
    data = json.loads(file.read())
    file.close()

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/checkout")
def checkout():
    return render_template("checkout.html")

@app.route('/banking')
def banking():
    return render_template("banking.html")

@app.route('/completed')
def completed():
    madon = request.args.get('madon')
    donthuoc = (firestore.collection("prescriptions").document(str(madon)).get()).to_dict()['list']
    command = []
    for thuoc in donthuoc:
        for i in range(int(thuoc["amount"])):
            command.append(data["medicine"][thuoc['id']]["slot"])
    print(command)
    # pharmabox_helper.dropMedicine(command)
    return render_template('completed.html')


@app.route("/getMachineID")
def getMachineID():
    return jsonify({"id": data["id"]})


@app.route("/getMedicineInfo")
def getMedicineInfo():
    id = request.args.get("id")
    try:
        return jsonify(data["medicine"][id])
    except Exception as e:
        return jsonify({"status": "error", "reason": "invalid"})


@app.route("/getCheckoutInfo")
def getCheckoutInfo():
    # TODO: link with db to return correct checkout info
    madon  = request.args.get("madon")
    donthuoc = (firestore.collection("prescriptions").document(str(madon)).get()).to_dict()
    if (donthuoc == None):
        return jsonify({"state": "error", "reason": "invalid"})
    else:
        return donthuoc['list']

app.run("0.0.0.0", port=80, debug=True)
