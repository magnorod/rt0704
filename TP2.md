# TP de RT 0704 : Une plateforme de code à la demande PARTIE 2 : test des services et des bibliothèques

## Producteur / consommateur dans RabbitMQ

Dans un premier temps, on va faire un programme python de lecture, écriture dans une file, selon un modèle producteur /consommateur.

1. Créez un environnement virtuel sur la machine virtuelle
2. Installez dans cet environnement virtuel les modules Flask et Pika
3. Connectez vous depuis VSCode sur l'hôte à l'invité, et accédez à l'environnement virtuel précédemment créé
4. Ecrivez une fonction de création d'une file nommée (*cf* cours)
5. Ecrivez une fonction d'écriture simple dans une file (*cf* cours), vous n'utiliserez pas de *fanout* juste une écriture directe
6.  Ecrivez une fonction de lecture simple dans une file (*cf* cours)
7.  testez les deux fonctions précédentes

## Docker File

1. Créez un Docker file permettant la création d'un conteneur Alpine contenant Graphviz
2. Testez la création du conteneur 
3. Testez l'exécution du conteneur

## API Docker en Python

Il est possible de piloter Docker depuis une API python.

1. Installez le module python Docker
2. Ecrivez une fonction permettant d'exécuter un conteneur simple
3. Ecrivez une fonction permettant de construire un conteneur à partie d'un *dockerfile*
4. Testez les deux fonctions écrites avec le conteneur précédent
5. Ecrivez une fonction permettant de récupérer la liste des conteneurs en cours exécution

## API GIT en python

Il est possible d'accéder, en python, aux dépôts GIT de deux manières :

- En exécutant une commande système depuis python
- En exploitant une API GIT

En fonction de choix d'exploitation de l'accès GIY que vous aurez fait,

1. Installez les éléments nécessaires à l'exploitation de GIT sur votre plateforme
2. Ecrivez une fonction permettant de cloner localement le contenu d'un dépôt

Vous pourrez exécuter la mise en place des fichiers sur le dépôt GIT de façon manuelle, si vous le souhaitez, vous pouvez écrire aussi les fonctions suivantes :
1. Ecrivez une fonction réalisant la création d'un projet GIT
2. Ecrivez une fonction permettant d'ajouter un fichier au projet précédemment créé
3. Ecrivez une fonction permettant de mettre à jour un fichier du projet précédemment créé
4. Ecrivez une fonction réélisant la destruction d'un projet GIT