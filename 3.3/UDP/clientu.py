from socket import *
serverName = 'localhost'
serverPort = 22000
clientSocket = socket(AF_INET, SOCK_DGRAM)
print ("컴파일러3.3 버전 UDP 클라이언 예제")
message = input('Input lowercase sentence:')
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print ('From Server(UDP):', modifiedMessage.decode())
clientSocket.close()
