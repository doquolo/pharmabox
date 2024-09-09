from flask import Flask, render_template, request, jsonify
import json

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

    if code == "1":
        return jsonify(
            [
                {
                    "id": "1",
                    "amount": 1,
                },
                {
                    "id": "4",
                    "amount": 1,
                },
            ]
        )
    elif code == "2":
        return jsonify(
            [
                {
                    "id": "2",
                    "amount": 1,
                },
                {
                    "id": "3",
                    "amount": 1,
                },
            ]
        )
    else:
        return jsonify({"state": "error", "reason": "invalid"})


app.run("0.0.0.0", debug=True)
