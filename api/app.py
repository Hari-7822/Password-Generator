from flask import Flask
from flask.json import jsonify

from ..main import generate, OTPGenerate

app = Flask(__name__)
@app.route("/", methods=["GET"])
def index():
    res = {
        "Response": generate(7),
    }
    return jsonify(res)

@app.route("/otp", methods=["GET"])
def Otp():
    res = {
        "Response": OTPGenerate(6),
    }
    return jsonify(res)

@app.route("/django-otp", methods=["GET"])
def DjangoOtp(request):
    res= {
        "user": request.user.username,
        "Response": OTPGenerate(6),
    }
    return(request, jsonify(res))

if app.name == "__main__":
    app.run(debug=True)