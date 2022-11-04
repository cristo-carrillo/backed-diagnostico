from flask import Flask, request
from main import diagnosticate


app = Flask(__name__)

@app.route("/diagnostico", methods=['GET', 'POST'])
def diagnostico():
    sintomas_paciente = request.get_json()
    print(sintomas_paciente)
    return diagnosticate(sintomas_paciente)

if __name__=="__main__":
    app.run(debug=True)