import paho.mqtt.client as mqtt

def conectado(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.publish("gabyllanga-15@outlook.com/t1")

def nuevoMensaje(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

    mensaje=msg.payload.decode('utf-8')
    if mensaje=='ON':
        print('encendido')

    if mensaje=='OFF':
        print('apagado')
client= mqtt.Client()  
client.username_pw_set('gabyllanga-15@outlook.com', password='gabyllanga')
client.on_connect = conectado
client.on_message = nuevoMensaje

client.connect("maqiatto.com", 1883, 60)

client.loop_forever()
