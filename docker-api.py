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