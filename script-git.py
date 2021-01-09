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
