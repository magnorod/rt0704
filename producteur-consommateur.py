#!/usr/bin/python3
import pika

def creationFileNommee(connection, queue_name):    
    channel = connection.channel()
    channel.queue_declare(queue_name)
    print("file "+queue_name+" créée")
    return channel

def ecritureSimpleFile(channel, queue_name, message):
    channel.basic_publish(exchange='',routing_key=queue_name,body=message)
    print("message envoyé : {}".format(message))


def lectureSimpleFile(channel, queue_name):
    method_frame, header_frame, body = channel.basic_get(queue_name)
    if method_frame:
        print(method_frame, header_frame, body)
        channel.basic_ack(method_frame.delivery_tag)
    else:
        print(" Rien à lire ")


if __name__ == "__main__":
    host='172.17.0.3'
    queue_name='file-perso1'

    connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
    channel=creationFileNommee(connection,queue_name)
    ecritureSimpleFile(channel,queue_name,'salut')
    
    # Force le vidage du network buffer
    connection.close()

    # Connexion au gestionnaire de file
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=host))
    channel=creationFileNommee(connection,queue_name)

    lectureSimpleFile(channel, queue_name)
    lectureSimpleFile(channel, queue_name)
    lectureSimpleFile(channel, queue_name)

    



