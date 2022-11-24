from flask import Flask
from flask_cors import CORS
import os
from routes.diagnosis_routes import diagnosis
from routes.kin_family import kin
from conexion import conexion_mongo

app = Flask(__name__)

app.register_blueprint(diagnosis)
app.register_blueprint(kin)
CORS(app)
conexion_mongo()
if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
    # app.run(debug=True)