import socket  # noqa: F401
def BrokerResponse(socket, response):
    socket.sendall(response)

def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    ClientSock, ClientAddr = server.accept() # wait for client
    data = ClientSock.recv(1024)
    print(f'data received from {ClientAddr} is {data} and its binary lenght is {data.__len__()} and the 7 and 8 members are {data[6:8]}')
    response = b"\x00\x00\x00\x00\x00\x00\x00\x07"
    ClientSock.sendall(response)
    BrokerResponse(ClientSock, response)
    

if __name__ == "__main__":
    main()
