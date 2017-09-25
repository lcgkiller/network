from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
print ('컴파일러3.3 버전 TCP 서버 예제')
print ('The server is ready to receive')
while 1:
     connectionSocket, addr = serverSocket.accept()
     
     sentence = connectionSocket.recv(1024)
     capitalizedSentence = sentence.upper()
     connectionSocket.send(capitalizedSentence)
     connectionSocket.close()
