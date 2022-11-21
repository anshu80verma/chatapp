# import the requiring modules in the code
import socket
import threading
import tkinter as tk
from tkinter import font
from tkinter.ttk import *
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox

HOST = '127.0.0.1'
PORT = 1234


root = tk.Tk()
root.geometry("600x600")
root.title("prychat")
root.resizable(False,False)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=4)
root.grid_rowconfigure(2, weight=1)
# colors using in the projects
perpal = '#fcfcfc'
pink  = '#da83fc'
blue = '#a11fff'
WHITE = "white"
BLACK = '#080600'
FONT = ("Helvetica", 17)
SMALL_FONT = ("Helvetica", 13)

photo = PhotoImage(file = r"start3.png")
img = PhotoImage(file = r"send1.png")
name= PhotoImage(file = r"name2.png")

client = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

def add_message(message):
    message_textbox.config(state=tk.NORMAL)
    message_textbox.insert(tk.END , message + '\n')
    message_textbox.config(state=tk.DISABLED)


def connect():
     # connect with server 
    try:
        client.connect((HOST,PORT)) 
        print("successfully connected to server")
        add_message("[SERVER] Succesfully connected to server")
    except:
        messagebox.showerror("Unable to connect" , f"Unable to connect with server {HOST}, {PORT}")


    username = username_textbox.get()
    if username != '':
        client.sendall(username.encode())
    else:
        messagebox.showerror("Invalid username" , "username cannot be empty")

    threading.Thread(target=listen_for_messages_from_server, args=(client, )).start()

    username_textbox.config(state=tk.DISABLED)
    username_button.config(state=tk.DISABLED)

def send_message():
    message = message_send.get()
    if message != '':
        client.sendall(message.encode())
        message_send.delete(0, len(message))
    else:
        messagebox.showerror("Empty message", "Message cannot be empty")

    

# frame divide the screen into diffrint parts 
top_frame = tk.Frame(root, width=600, height=100,bg= perpal)
top_frame.grid(row=0,column= 0 , sticky=tk.NSEW)

username_label = tk.Label(top_frame,image=name)
username_label.pack(side=tk.LEFT, padx=10)
# enter the username is here 
username_textbox = tk.Entry(top_frame, font= FONT , width=35, background='#b3f0ff')
username_textbox.pack(side=tk.LEFT,padx=5)


middle_frame = tk.Frame(root, width=600, height=400,bg='#e6e9f0')
middle_frame.grid(row=1,column= 0 , sticky=tk.NSEW)


bottom_frame = tk.Frame(root, width=600, height=100,bg='#a2e3f5')
bottom_frame.grid(row=2,column= 0 , sticky=tk.NSEW)


# creating button of JOIN
username_button =tk.Button(top_frame,image=photo , bg =BLACK , fg=WHITE, command=connect)
username_button.pack(side=tk.RIGHT,padx=10)


# entry button 
message_send =tk.Entry(bottom_frame,font= FONT ,width=38)

message_send.pack(side=tk.LEFT,padx=10)

# send button
send_button = tk.Button(bottom_frame,image=img,bg = WHITE , fg=WHITE, command=send_message)
send_button.pack(side=tk.LEFT,padx=10)
# send_button.bind("<Return>",lambda event: send_message())

message_textbox=scrolledtext.ScrolledText(middle_frame,font= SMALL_FONT,bg ='#e6e9f0',fg ='#050505', width= 64 ,height= 26)
message_textbox.config(state=tk.DISABLED)
message_textbox.pack(side=TOP)

def listen_for_messages_from_server(client):
    while 1:
        message = client.recv(2048).decode('utf-8')
        if message != '':
            username = message.split("~")[0]
            content = message.split("~")[1]

            add_message(f"[{username}] {content} ") 
        else:
            messagebox.showerror("Error","Message receve from client is empty")

def main():
    root.mainloop()
if __name__ =='__main__':
    main()