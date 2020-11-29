# TP RT0704-Partie 1
## Producteur-consommateur

### 1. Créez un environnement virtuel sur la machine virtuelle

* docker pull alpine

création du docker file

Construction de notre image perso via le Dockerfile

* docker build -t debian-perso .
1)2 et 3)
Lancement du conteneur avec forward de port
* docker run -it --hostname debian-tp2 --name debian-tp2  -p 2222:22 debian-perso /bin/bash

lancement manuel du service ssh
* service ssh start


## Ecrivez une fonction de création d'une file nommée (*cf* cours)


voir le script


# DockerFile

1) création du dockerfile

* docker pull alpine

![](img/dockerfile-alpine)

2) Test création du conteneur

* docker build -t alpine-graphviz .

3) Test exécution

* docker run -it --hostname alpine-graphviz --name alpine-graphviz alpine-graphviz /bin/sh

on constate que graphviz est bien installé avec :
* apk info graphviz


# API docker en Python

1) installation du module docker
* pip3 install docker

2) exécuter un conteneur simple


