import paho.mqtt.client as mqtt
import time
import random
def conectado(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("gabyllanga-15@outlook.com/t1")

def nuevoMensaje(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    mensaje=msg.payload.decode('utf-8')
    if mensaje=='ON':
        print('ACTIVADO')

    if mensaje=='OFF':
        print('DESACTIVADO')
client= mqtt.Client()  
client.username_pw_set('gabyllanga-15@outlook.com', password='gabyllanga')
client.on_connect = conectado
client.on_message = nuevoMensaje

client.connect("maqiatto.com", 1883, 60)

n=0
while 1:
    time.sleep(1)
    valor1=random.randint(1,10)
    valor2=random.randint(10,20)
    client.publish('gabyllanga-15@outlook.com/t1',str(n)+';'+str(valor1)+';'+str(valor2))
    client.loop()
    n=n+1
