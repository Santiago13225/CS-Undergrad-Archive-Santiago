#UDP Client
from socket import *
serverName = 'hostname' //here, 127.0.0.1
serverPort = 12000
clientSocket = socket(AF_INET, 
 SOCK_DGRAM)
message = raw_input('Input lowercase sentence:')
clientSocket.sendto(message,(serverName, serverPort))
modifiedMessage, serverAddress = 
 clientSocket.recvfrom(2048)
print modifiedMessage
clientSocket.close()

#TCP Client
'''
from socket import *
serverName = 'servername' //here, 127.0.0.1
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = raw_input('Input lowercase sentence:')
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
print 'From Server:', modifiedSentence
clientSocket.close()
'''