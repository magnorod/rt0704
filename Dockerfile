FROM alpine:latest

RUN apk add python3 --no-cache  \
&& apk add openssh --no-cache \
&& apk add openrc --no-cache \
&& adduser user -D -s /bin/sh \
&& echo "user:user" | chpasswd \
&& rc-update add sshd \
&& mkdir /run/openrc \ 
&& touch /run/openrc/softlevel


RUN python3 -m ensurepip \
&& python3 -m pip install --upgrade pip 

RUN pip3 install flask  \
&& pip3 install pika 

CMD 
