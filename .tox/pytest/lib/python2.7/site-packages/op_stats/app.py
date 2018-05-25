#app.py 
from flask import Flask
import json
import sys
sys.path.append('/home/operativos/so-exam3')
from stats import Stats

app = Flask(__name__)

@app.route("/cpu")
def CPU():
    return json.dumps({'Consumo de CPU: ':str(Stats.get_cpu_percent()*100)+"%"})

@app.route("/ram")
def RAM():
    return json.dumps({'MEMORIA RAM disponible: ':str(Stats.get_ram())+"%"})

@app.route("/disco")
def DISK():
    return json.dumps({'Disco Duro disponible: ':str(Stats.get_disk())+"%"})


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
