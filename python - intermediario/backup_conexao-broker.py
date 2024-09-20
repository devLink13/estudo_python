import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conexão bem-sucedida! Você está conectado ao broker.")
        # Inscreva-se em um tópico para receber mensagens
        client.subscribe("topico_teste")
    else:
        print(f"Falha na conexão. Código de retorno: {rc}")


def on_message(client, userdata, message):
    print(f"Nova mensagem recebida no tópico '{
          message.topic}': {message.payload.decode()}")


def main():
    client = mqtt.Client(client_id="", userdata=None, protocol=mqtt.MQTTv5)
    client.on_connect = on_connect
    client.on_message = on_message

    # Configurações do broker (substitua pelos seus próprios valores)
    broker_address = "2fccf781db1044daad74b457363a6fca.s1.eu.hivemq.cloud"
    port = 8883

    # Conecte-se ao broker
    client.connect(broker_address, port)

    # Inicie o loop para manter a conexão ativa e processar mensagens
    client.loop_forever()


if __name__ == "__main__":
    main()
