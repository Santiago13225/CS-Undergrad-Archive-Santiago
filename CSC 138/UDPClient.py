#UDP Client
from socket import * #Includes Python’s socket library!
serverName = '127.0.0.1'
serverPort = 12061
clientSocket = socket(AF_INET, SOCK_DGRAM) #Creates a UDP socket for the server.
#^Creates a datagram with server IP and port = x;
message = raw_input('Input lowercase sentence:') #Gets user input from the keyboard.
clientSocket.sendto(message,(serverName, serverPort))
#^Attaches the server name and port to the message and then sends it into the socket.
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
#^Simply reads the reply characters from the socket into string.
print modifiedMessage #Prints out the received string.
clientSocket.close()  #Closes the socket.

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
