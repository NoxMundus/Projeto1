import pika
import json

#O que define ser falso é que no campo Location tenham valores diferentes para _clienteid iguais
#O arquivo é o Sample.json

#Conexão com o RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters(
    host="localhost",
     port=5672,
     virtual_host="/")
)

channel = connection.channel()

#Seta as propriedades das mensagens
properties = pika.BasicProperties(
    # expiration="10000",
     priority= 7,
     app_id="",
     content_type="application/json",
     reply_to="replay_queue"           
)

#Carrega o arquivo Json e quebra dentro do array
with open('/home/ec2-user/Aulas/Cloud/Projeto/Sample.json', 'r') as f:
    data = json.loads(f.read())

#Anda o array e vai enviado os conteudos como mensagens
for x in data:
    bodymsg = {"msg":x}
    print(bodymsg)
    print("----------------------------------------------------------------------------------------------------------------")
    channel.basic_publish(exchange="amq.direct",
                      routing_key="antifraudekey",
                      body=bodymsg.__str__(),
                      properties=properties,
    )

#terminando fecha a conexão
channel.close()
