import paho.mqtt.client as mqtt
import time


######## função de callback para recebimento de mensabem ########
def on_message(client, userdata, message):
    print(f"Nova mensagem recebida no tópico '{
          message.topic}': {message.payload.decode()}")


# configurações do broker e de segurança da comunicação
client = mqtt.Client(client_id="", userdata=None, protocol=mqtt.MQTTv5)
client.tls_set(tls_version=mqtt.ssl.PROTOCOL_TLS)
client.username_pw_set("python", "Wsl123456789@")

# dados do broker
broker = "2fccf781db1044daad74b457363a6fca.s1.eu.hivemq.cloud"
porta = 8883

try:  # tente conectar ao broker
    client.connect(broker, porta)
    client.subscribe("topico_teste")
    print("Conexão bem-sucedida! Você está conectado ao broker.")

except Exception as error:
    print(f"FALHA NA CONEXÃO. Código de erro: {error}")

# callback de atualização do tópico inscrito
client.on_message = on_message
client.loop_start()  # crio uma thread que fica analisando a conexão,
# e disparando o callback quando necessário

# laço usado para demonstrar que a thread não trava o código
while True:
    for c in range(0, 1000):
        print(c)
        c += 1
        time.sleep(1)
