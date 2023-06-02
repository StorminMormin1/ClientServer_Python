# Credit for basic connection setup of the client_server model goes to:
# https://www.digitalocean.com/community/tutorials/python-socket-programming-server-client

import socket

names = ["Aaron", "Billy", "Cooper", "Dante", "Eric", "Frederick", 
         "Gavin", "Henry", "Israel", "Jacob", "Kevin", "Larry", "Michael",
         "Noah", "Oscar", "Patrick", "Qauhan", "Richard", "Samuel", "Trevor",
         "Ulrich", "Victor", "Wyatt", "Xavier", "Yohan", "Zach"]

def server_program():
    # get the hostname
    host = socket.gethostname()
    port = 5000  # initiate port num above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("New connection from: " + str(address))
    while True:
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("From connected user: " + str(data))

        # Send a name back to the client
        if data == 'names':
            conn.send("Enter a number for a letter that a name will start with:".encode())
            data = conn.recv(1024).decode()
            index = int(str(data)) # convert the character to ASCII number
            #index = index - 97 # make index relateable to lists
            print(index)
            if (index < len(names)):
                conn.send(names[index].encode())
                print("Sent looked-up name to client")
            else:
                conn.send("List index out of range".encode())
        
        # Read a file to the client
        elif data == "file":
            f = open("words.txt", "r")
            name = f.readline()
            conn.send(name.encode())

        # Send a custom input message to the client
        else:
            data = input(' -> ')
            conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection
    print(f"User {str(address)} disconnected from server.")

if __name__ == '__main__':
    server_program()