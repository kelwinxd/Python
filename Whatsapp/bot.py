import pywhatkit as kit

# Função para enviar mensagens
def enviar_mensagem(numero, mensagem):
    kit.sendwhatmsg(numero, mensagem, 0, 0)

# Número de telefone para o qual você deseja enviar mensagens
numero_destino = "+5519991413905"  # Substitua pelo número de telefone real

# Mensagem que você deseja enviar
mensagem = "Olá, isso é uma mensagem de teste!"

# Enviar a mensagem
enviar_mensagem(numero_destino, mensagem)
