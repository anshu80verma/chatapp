# import qall the module i need in the project

import socket
import threading

HOST = '127.0.0.1'
PORT = 1234
LISTNER_LIMIT = 5
active_clients = [] #list of all connected clients

def listen_for_messages(client, username):

    while 1:

        message = client.recv(2048).decode('utf-8')
        if message != '':
            
            final_msg = username + '~' + message
            send_messages_to_all(final_msg)

        else:
            print(f"The message send from client {username} is empty")

def send_message_to_client(client,message):
    client.sendall(message.encode())

def send_messages_to_all(message):
    
    for user in active_clients:

        send_message_to_client(user[1], message)


# function to hendal clint
def client_handler(client):
    while 1:
        username = client.recv(2048).decode('utf-8')
        if username != '':
            active_clients.append((username, client))
            prompt_message = "SERVER~" + f"{username} added to the chat"
            send_messages_to_all(prompt_message)
            break
        else:
            print("client username is enpty")

    threading.Thread(target=listen_for_messages, args=(client, username, )).start()
def main():
    # creating the server socket by class object
    # AF_intel : we are going to use IPv4 address
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        server.bind((HOST,PORT))
        print(f"Running the server on {HOST} {PORT}")
    except:
        print(f"unable to bind to host{HOST} and port {PORT}")


    # set the server limits
    server.listen(LISTNER_LIMIT)
    # this while loop will listen the clint connections
    while 1:
        client, address = server.accept()
        print(f"successfully connected to the client {address[0]} and {address[1]} ")
        
        threading.Thread(target=client_handler, args=(client, )).start()


if __name__  =='__main__':
    main()
