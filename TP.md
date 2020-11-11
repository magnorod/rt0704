# TP de RT 0704 : Une plateforme de code à la demande  PARTIE 1 : Mise en place d'éléments de l'infrastructure

## Mise en place de l'environnement de développement

Dans cette partie on considère que vous disposez d'une machine virtuelle de type Ubuntu Serveur

1. Installez VSCode sur la machine physique
2. Installez si nécessaire le module *remote development* de VSCode
3. Mettez en place un échange de clé RSA entre la machine physique et la machine virtuelle
4. Connectez vous depuis VSCode à la machine virtuelle
5. Vérifiez que python3, pip3 et virtualenv / venv sont bien installés sur la machine virtuelle
6. Créez un premier script python **hello world** et exécutez le

## Installation de docker

1. Installez Docker sur la machine Virtuelle
2. Testez l'installation de docker avec le conteneur **hello world**

## Gestionnaire de file

Le gestionnaire de file de message RabbitMQ s'exécutera dans un conteneur Docker.

1. Téléchargez et exécutez un conteneur RabbitMQ
2. Installez le *plugin* RabbitMQ d'accès WEB
   - Testez l'accès à l'interface d'administration de RabbitMQ 

## Flask

Le serveur Flask s'exécutera dans un conteneur Docker.

1. Téléchargez et exécutez un conteneur Flask
2. Réalisez un service retournant un simple "hello world" 
3. Créez une page web avec un template JINJA
4. Réalisez la création d'un couple formulaire / page de traitement exploitant JINJA
