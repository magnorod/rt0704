# installation de la vm

# installation de docker
sudo apt install docker.io -y
ajout de l'utilisateur marc au groupe docker ( plus de sudo à taper)
sudo usermod -aG docker marc



# génération des clés RSA

## sur l'hote faire:

marc@magnorod:~$ ls .ssh
config  known_hosts
marc@magnorod:~$ ssh-keygen -t rsa
Generating public/private rsa key pair.
Enter file in which to save the key (/home/marc/.ssh/id_rsa): 
Enter passphrase (empty for no passphrase): 
Enter same passphrase again: 
Your identification has been saved in /home/marc/.ssh/id_rsa
Your public key has been saved in /home/marc/.ssh/id_rsa.pub
The key fingerprint is:
SHA256:TsSEY7hMGdSsdr4yOw8e6oevpPI/5N8uU3hrwAaIdmE marc@magnorod
The key's randomart image is:
+---[RSA 3072]----+
|   .o* ..        |
|   E+ *o         |
| ..+.+ .o        |
|....* ..         |
|. .. = .S        |
|    . *oo        |
|  .+o. =..       |
|.o.oBo+.o        |
|oo===Oo=o        |
+----[SHA256]-----+


## copie de la clé publique de l'hôte sur l'invité:
marc@magnorod:~$ scp .ssh/id_rsa.pub marc@192.168.1.4:/tmp
marc@magnorod:~$ ssh marc@192.168.1.4

marc@192.168.1.4 password:
id_rsa.pub                                            100%  609     0.6KB/s   00:00
ssh marc@192.168.1.4
cat /tmp/id_rsa.pub >> /root/.ssh/authorized_keys
rm /tmp/id_rsa.pub


## modification du fichier /etc/ssh/sshd_config
PubkeyAuthentication yes
AuthorizedKeysFile      .ssh/authorized_keys
ChallengeResponseAuthentication yes



# création du script
#!/bin/python3

print ("hello-world")

marc@marc-server:~/script-tp1-rt0704$ python3 hello-world.py 
hello-world


# installation de rabbitmq
docker pull rabbitmq
** Using default tag: latest
latest: Pulling from library/rabbitmq
171857c49d0f: Pull complete 
419640447d26: Pull complete 
61e52f862619: Pull complete 
856781f94405: Pull complete 
125d5ee3d600: Pull complete 
42de77c4d197: Pull complete 
4d65f87814dd: Pull complete 
f6c0bf06039f: Pull complete 
01671add1b7b: Pull complete 
088ff84cf8cb: Pull complete 
Digest: sha256:3da3bcd2167a1fc9bdbbc40ec0ae2b195df5df05e3c10c64569c969cb3d86435
Status: Downloaded newer image for rabbitmq:latest
docker.io/library/rabbitmq:latest **

## exécution du conteneur rabbitmq
activation du pluggin management (http) et forward du port 15672 du conteneur rabbitmq au port 8080 de l'ubuntu server (VM)

docker run -d --hostname my-rabbit --name some-rabbit -p 8080:15672 rabbitmq:3-management

docker run -idt --privileged --hotsname conteneur-flask --name conteneur-flask /bin/bash




# installation de flask