from flask import *
app = Flask(__name__)

@app.route("/formulaire")
def formulaire():
    return render_template("formulaire.html")

@app.route("/traitement", methods=['POST'])
def traitement():
    mydata = {}
    service = request.form["type_tache"]
    fichier = request.form["fichier"]
    cmd = request.form["cmd"]
    return render_template("traitement.html",data1=service,data2=fichier,data3=cmd)

if __name__=="__main__":
    app.run(host='0.0.0.0',port=8000, debug=True)