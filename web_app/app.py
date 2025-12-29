from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

items = [
    {"slno": 1, "name": "Apple", "price": 10, "qty": 0},
    {"slno": 2, "name": "Banana", "price": 5, "qty": 0},
    {"slno": 3, "name": "Orange", "price": 8, "qty": 0},
    {"slno": 4, "name": "Mango", "price": 15, "qty": 0},
    {"slno": 5, "name": "Grapes", "price": 12, "qty": 0},
]

@app.route("/")
def index():
    return render_template("index.html", items=items)

@app.route("/update", methods=["POST"])
def update():
    slno = request.json["slno"]
    for item in items:
        if item["slno"] == slno:
            item["qty"] += 1
            break
    return jsonify({"status": "ok"})

app.run(debug=True)
