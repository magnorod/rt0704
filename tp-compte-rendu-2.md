# TP RT0704-Partie 1
## Producteur-consommateur

### 1. Créez un environnement virtuel sur la machine virtuelle

* docker pull alpine

création du docker file

Construction de notre image perso via le Dockerfile

* docker build -t alpie-perso .
1)2 et 3)
Lancement du conteneur avec forward de port
* docker run -it --hostname alpine-tp2 --name alpine-tp2  -p 2222:22 alpine-perso /bin/ash

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


## API docker en Python

1) installation du module docker
* pip3 install docker

2) 3) 4) 5) voir script

## API GIT en Python
Installation de la bilbiothèque
1)

* sudo apt install git
* pip3 install gitpython


2) voir script-git.py
git submodule add https://github.com/magnorod/rt0704