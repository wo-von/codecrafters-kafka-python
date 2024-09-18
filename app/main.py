import socket  # noqa: F401


def main():
    # You can use print statements as follows for debugging,
    # they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server = socket.create_server(("localhost", 9092), reuse_port=True)
    ClientSock, ClientAddr = server.accept() # wait for client
    data = ClientSock.recv(1024)
    print(f'data received from {ClientAddr} is {data}')
    response = b"\x00\x00\x00\x00\x00\x00\x00\x07"
    ClientSock.sendall(response)
    

if __name__ == "__main__":
    main()
