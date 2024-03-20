## Como rodar o projeto

Garanta que tem os 4 arquivos:
Samples.json -> Tem os exemplos usados
Producer.py -> Monta o producer e sobe as mensagens
Consumer.py -> Monta o consumer e tratar as mensagens 
docker-compose.yaml -> tem as configs do docker compose


### 1. Install docker, caso tenham falhas em usar comandos com o docker só, usar sudo 

sudo yum install -y yum-utils

sudo yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

sudo yum install docker

sudo groupadd docker

#### Coloque seu usuario
sudo usermod -aG docker ec2-user

newgrp docker

docker version


### 2. Install docker-compose, caso tenham falhas em usar comandos com o docker só, usar sudo 

sudo curl -SL https://github.com/docker/compose/releases/download/v2.24.6/docker-compose-linux-x86_64 -o /usr/local/bin/docker-compose

sudo chmod +x /usr/local/bin/docker-compose

docker-compose version

#### 2.1 Uma vez feito a instalação do docker compose. Faça um down e um up, na pasta em que estiver o arquivo do compose passado. 

docker-compose down

docker-compose up


### 3. Instalar o python e suas bibliotecas 

sudo yum install python3-pip

pip install pika

pip install minio

pip install redis


### 4. Alterar os paths conforme a maquina, esse projeto

#### 4.1 Em producer.py, linha 25, alterar o path para onde estiver o arquivo de samples:

with open('/home/ec2-user/Aulas/Cloud/Projeto/Sample.json', 'r') as f:

#### 4.2 Ema consumer.py, linha 75, alterar o path para uma pasta que será usada para temporariamente guardar os arquivos que iram para o minio:

file_caminho = "/home/ec2-user/Aulas/Cloud/Projeto/Temp/"+file_name


### 5. Lembrete

#### 5.1 Minio está com o user e senha abaixo e não o default
access_key="ricardo",
secret_key="test1234",

#### 5.2 Ordem do python

1-> Consumer.py
2-> Producer.py


