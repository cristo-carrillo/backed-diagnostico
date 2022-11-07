from flask import Flask, request
from routes.diagnosis_routes import diagnosis

app = Flask(__name__)

app.register_blueprint(diagnosis)


# if __name__=="__main__":
#     app.run(host="0.0.0.0",port="80",debug=True)