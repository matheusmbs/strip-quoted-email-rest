import talon
from talon import quotations
talon.init()

def readRequest():
    arq = open('request.html', 'r')
    texto = arq.read()
    arq.close()
    return texto

def reply(menssagem):
    reply = quotations.extract_from(menssagem, 'text/html')
    return reply

print reply("teste")