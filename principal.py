from flask import Flask, request
from routes.diagnosis_routes import diagnosis

app = Flask(__name__)

app.register_blueprint(diagnosis)


if __name__=="__main__":
    app.run(debug=True)