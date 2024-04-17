from flask import Flask,render_template,request,jsonify
from flask_cors import CORS
from chatbot import get_response
from chatbot import predict_class
import json

intents=json.loads(open('intents.json').read())
app=Flask(__name__)
CORS(app)

@app.get("/")
def index_get():
    return render_template("base.html")


@app.post("/predict")
def predict():
    text=request.get_json().get("message")
    ints=predict_class(text)
    response=get_response(ints,intents)
    # print(response)
    message={"answer":response}
    return jsonify(message)

if __name__ == "__main__":
    app.run(debug=True)

