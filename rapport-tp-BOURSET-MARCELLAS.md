# TP RT0704 - Marc Bourset-Marcellas

## Mise en place de l'environnement de développement

### Mettez en place un échange de clé RSA entre la machine physique et la machine virtuelle
`ssh-keygen -t rsa`

### Transfert de la clé publique de l'hôte sur l'invité
`ssh-copy-id -i ~/.ssh/id_rsa.pub user@172.18.10.20`


### Vérifiez que python3, pip3 et virtualenv / venv sont bien installés sur la machine virtuelle

`apt-get install python3 python3-pip -y `
`pip3 installvirtualenv `


### Création du script hello-world

```
#!/bin/python3
print("hello-world")
```

### Exécution du script 
`python3 hello-world.py`

## Installation de docker

### Installez Docker sur la machine Virtuelle

`sudo apt install docker.io -y`

### Ajout de user au groupe docker (pas besoin de root pour docker)
`sudo usermod -aG docker user`

### Testez l'installation de docker avec le conteneur **hello world**
`docker run hello-world`

## Gestionnaire de file
### Téléchargez et exécutez un conteneur RabbitMQ

Activation du pluggin management (http) et forward du port 15672 du conteneur rabbitmq au port 8080 de l'ubuntu server (VM)

utilisateur par défaut:
* id=guest
* mdp=guest

```
 docker run -d \
    --restart always \
    --hostname rabbitmq-perso \
    --name rabbitmq-perso \
    -p 8080:15672 \
    rabbitmq:3-management
```

## Flask

### Téléchargez et exécutez un conteneur Flask

Lancer un conteneur flash avec une redirection du port 8000 de l'invité sur le port 8081 de l'hote, le fichier app.py génère automatiquement le "hello-world"

```
docker run -d \
    --hostname conteneur-flask \
    --name conteneur-flask \
    -p 8081:8000 \
    altoning/flask3
```

accès OK via http://172.18.10.20:8081

```
user@vm-rt0704:~$ curl -I http://172.18.10.20:8081
HTTP/1.1 200 OK
Server: gunicorn/19.7.1
Date: Tue, 19 Jan 2021 21:48:07 GMT
Connection: close
Content-Type: text/html; charset=utf-8
Content-Length: 12
```



### Modification du fichier app

Création d'un conteneur flask qui exécutera un shell /bin/bash

```
docker run \
    -a stdin \
    -a stdout \
    -a stderr \
    -it \
    --hostname conteneur-flask \
    --name conteneur-flask \
    -p 8081:8000 \
    altoning/flask3 /bin/bash
```

`vi app.py`

```
from flask import Flask
app = Flask(_name_)

@app.route("/")
def hello():
    return "Hello World"

@app.route("/guerrier")
def guerrier():
    return "Je suis un guerrier"

@app.route("/mage")
def mage():
    return "Je suis un mage"

if __name__=="__main__":
    app.run(host='0.0.0.0',port=8000, debug=True)
```

Lancement du script boot.sh
`/bin/bash boot.sh`

### Créez une page web avec un template JINJA

Jinja 2 est déja installé

`mkdir templates`
`vi templates/template1.html`

```
<html>
    <head>
        <title> Un essai</title>
    </head>
    <body>
        {% if data %}
        <h1> Hello {{ data }}</h1>
        {% else %}
        <h1> Il manque un parametre</h1>
        {% endif %}
    </body>
</html>
```
`vi app.py`

```
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/render",methods=['GET'])
@app.route("/render/<name>", methods=['GET'])

def fct9(name=None):
    return render_template("template1.html",date=name)

if __name__=="__main__":
    app.run(host='0.0.0.0',port=8000, debug=True)
```
`python3 app.py`

### Réalisez la création d'un couple formulaire / page de traitement exploitant JINJA

`vi templates/formulaire.html`

```
<html>
    <head>
        <title>Plateforme execution de code</title>
    </head>
    <body>
        <center>
            <h2>Plateforme d'éxécution de code</h2>
        </center>
        <br>   
        <form action = "traitement" method ="post">
            <label for="type_tache">Choix du service:</label>
            <div>
                <input type="radio" id="Graphviz" name ="type_tache" value="Graphviz" >
                <label for="Graphviz">Graphviz</label>
            </div>
            <div>
                <input type="radio" id="Pandoc" name ="type_tache" value="Pandoc" >
                <label for="Pandoc">Pandoc</label>
            </div>
            <div>
                <input type="radio" id="ImageMagic" name ="type_tache" value="ImageMagic" >
                <label for="ImageMagic">ImageMagic</label>
            </div>
            <br>
            <br>
            <input type="file" id="fichier" name="fichier">
            <br>

            <label for="cmd">Commande (255 caractères max):</label>
            <br>
            <input type="text" id="cmd" name="cmd" requiered minlength="4" maxlength="255" size="70">
            <br>
            <div class="button">
                <button type="submit">Start</button>
            </div>
        </form>
    </body>
</html>
```

`vi templates/traitement.html`

```
<html>
    <head>
        <title>Plateforme execution de code</title>
    </head>
    <body>
        <center>
            <h2>Plateforme execution de code</h2>
        </center>
        <p>Le service demandé est : <br> {{ data1 }} </p>
        <p>Le fichier a traiter est : <br> {{ data2 }} </p>
        <p>La commande a éxecuter est : <br> {{ data3 }} </p>
    </body>
</html>
```

`vi app.py`

```
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
```

## Producteur-consommateur

### Créez un environnement virtuel sur la machine virtuelle

`docker pull alpine`

```
FROM alpine:latest

RUN apk add openssh python3 py3-pip --no-cache \
pip3 install flask pika --no-cache-dir

```

```
#!/usr/bin/python3
import pika

def creationFileNommee(connection, nom_file):
    channel = connection.channel()
    channel.queue_declare(nom_file)
    return channel

def ecritureSimpleFile(channel, nom_file, message):
    channel.basic_publish(exchange='', routing_key=nom_file, body=message)
    print("message envoyé : {}".format(message))

def lectureSimpleFile(channel, nom_file):
    method_frame, header_frame, body = channel.basic_get(nom_file)
    if method_frame:
        print(method_frame, header_frame, body)
        channel.basic_ack(method_frame.delivery_tag)
    else:
        print("rien à lire")
    #endif


if __name__ == "__main__":
    ip_rabbitmq="172.17.0.2"
    nom_file="Test"
    msg="Bonjour"
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=ip_rabbitmq))
    channel = creationFileNommee(connection, nom_file)
    ecritureSimpleFile(channel, nom_file, msg)
    lectureSimpleFile(channel, nom_file)
    connection.close
```

```
user@vm-rt0704:~/projet/projet-flask/script$ python3 script-rabbitmq.py 
message envoyé : Bonjour
<Basic.GetOk(['delivery_tag=1', 'exchange=', 'message_count=0', 'redelivered=False', 'routing_key=Test'])> <BasicProperties> b'Bonjour'
```

### DockerFile
`vi Dockerfile`

```
FROM alpine-perso:latest

RUN apk add graphviz --no-cache

```
2) Construction de l'image
`docker build -t alpine-perso-graphviz .`

3) Test exécution

``` 
docker run -it \
    --hostname alpine-graphviz \
    --name alpine-graphviz \
    alpine-perso-graphviz /bin/sh
```
on constate que graphviz est bien installé avec :
`apk info graphviz`

```
/ # apk info graphviz
WARNING: Ignoring APKINDEX.2c4ac24e.tar.gz: No such file or directory
WARNING: Ignoring APKINDEX.40a3604f.tar.gz: No such file or directory
graphviz-2.44.0-r0 description:
Graph Visualization Tools

graphviz-2.44.0-r0 webpage:
https://www.graphviz.org/

graphviz-2.44.0-r0 installed size:
7172096
```


## API docker en Python

### Installation du module docker

`pip3 install docker`

### Exploitation du module docker

```
#!/usr/bin/python3
import docker

def lancerConteneur(client, nomImage, nomConteneur, cmd):
    print(client.containers.run(image=nomImage, name=nomConteneur, command=cmd))
#endef

def buildConteneur(client, tag, path):
    print(client.images.build(tag=tag, path=path))
#endef

def listeConteneurUp(client):
    print(client.containers.list())
#endef

if __name__ == '__main__':
    client = docker.from_env()
    print("info: recuperation du client effectue")

    buildConteneur(client, 'alpine-perso:latest', 'alpine-perso/')
    print("info: build réalise")

    lancerConteneur(client, 'alpine-perso:latest', 'new-alpine', "/bin/ash")
    print("info: conteneur a ete lance")
     
    listeConteneurUp(client)
```

## API GIT en Python

### Installation de git 

`sudo apt install git `

### Exploitation de la commande système depuis Python

```
#!/usr/bin/python3
import os

def git_config(email,name):
    cmd='git config --global user.email "'+email+'" '
    os.system(cmd)
    cmd='git config --global user.name "'+name+'" '
    os.system(cmd)
#endef

def clone_projet_existant(url):
    cmd="git clone "+url
    print("info:cmd="+str(cmd))
    os.system(cmd) 
#endef

def creer_projet(project_path):
    cmd= "git init "+project_path
    print("info:cmd="+str(cmd))
    os.system(cmd) 
#endef

def ajouter_fichier(fichier,project_path):
    cmd="cd "+project_path+" &&  git add "+fichier
    print("info:cmd="+str(cmd))
    os.system(cmd) 
#endef

def maj_fichier(modif,project_path):
    cmd="cd "+project_path+" && git commit -m '"+modif+"'"
    print("info:cmd="+str(cmd))
    os.system(cmd) 
#endef

def supprimer_projet(project_path):
    cmd="rm -fr "+project_path+"/.git"
    print("info:cmd="+str(cmd))
    os.system(cmd) 
#endef

if __name__ == '__main__' :
    project_url="https://github.com/magnorod/test-rt0704"
    project_path="/home/user/projet-test3"
    fichier="fichier.txt"
    modif="correctif blabla OK"
    email="marcboursetmarcellas@gmail.com"
    pseudo="magnorod"
    
    git_config(email,pseudo)
    print("info: config git ok")

    clone_projet_existant(project_url)
    print("info: project cloné")

    creer_projet(project_path)
    print("info: project"+project_path+" créé")

    # on suppose que le fichier se trouve déja à la racine du projet (on l'ajoute juste au projet)
    ajouter_fichier(fichier,project_path)
    print("info: fichier"+fichier+" ajouté au projet")

    maj_fichier(modif,project_path)
    print("info: commit ok")

    supprimer_projet(project_path)
    print("info: projet supprimé")
    
#endif
```
