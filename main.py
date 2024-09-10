from flask import Flask, render_template, request, jsonify
import json
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
    with open('testCheckout.json', 'r', encoding='utf-8') as file:
        datacheckout = json.loads(file.read())
        file.close()
    madon = request.args.get('madon')
    donthuoc = datacheckout[madon]
    command = []
    for thuoc in donthuoc:
        for i in range(thuoc["amount"]):
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
    code = request.args.get("madon")

    with open('testCheckout.json', 'r', encoding='utf-8') as file:
        data = json.loads(file.read())
        file.close()
    try:
        return data[code]
    except Exception as e:
        return jsonify({"state": "error", "reason": "invalid"})


app.run("0.0.0.0", debug=True)
