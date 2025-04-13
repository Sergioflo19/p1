from flask import *

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "POST":
        print("JOSVEL GERENTE DE SM0 DAME CHAMBA")
    return render_template("index.html")