#app.py 
from flask import Flask
import json
import sys
sys.path.append('/home/operativos/so-exam3/A00309844')
from stats import Stats

app = Flask(__name__)

@app.route("/CPU")
def CPU():
    return json.dumps({'Consumo de CPU: ':Stats.get_cpu_percent()})

@app.route("/RAM")
def RAM():
    return json.dumps({'RAM disponible: ':Stats.get_ram()})

@app.route("/DISK")
def DISK():
    return json.dumps({'Disco disponible: ':Stats.get_disk()})


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
