from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
print ('컴파일러3.3 버전 TCP 클라이언트 예제')
sentence = input('input lowercase sentence:')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print ('From Server(TCP):', modifiedSentence.decode())
clientSocket.close()
