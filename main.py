from flask import Flask, request
import os
from routes.diagnosis_routes import diagnosis

app = Flask(__name__)

app.register_blueprint(diagnosis)


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))