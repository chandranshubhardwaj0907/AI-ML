# Q10. Mini Project – OOP Chat System 
# Letʼs create a Chat System using OOPs concepts. We have to create classes: 
# And we have to implement functions: 
# •  sending messages 
# •  viewing chat history 
# •  user joining and leaving the chatroom 
# User 
# Message 
# ChatRoom 

class user:
    def __init__(self , name):
        self.namee = name
        
    def send_message(self , chatroom , message):
        chatroom.add_message(self.namee , message)
        
class message:
    def __init__(self , sender , content):
        self.sender = sender
        self.content = content
        
class chatroom:
    def __init__(self):
        self.users = []
        self.messages = []
        
    def join(self , user):
        self.users.append(user)
        print(f"{user.namee} has joined the chatroom.")
        
    def leave(self , user):
        self.users.remove(user)
        print(f"{user.namee} has left the chatroom.")
        
    def add_message(self , sender , content):
        msg = message(sender , content)
        self.messages.append(msg)
        
    def view_chat_history(self):
        for msg in self.messages:
            print(f"{msg.sender}: {msg.content}")
            
            
room = chatroom()

u1 = user("Chandranshu")
u2 = user("Aman")

room.join(u1)
room.join(u2)

u1.send_message(room, "Hello!")
u2.send_message(room, "Hi!")

room.view_chat_history()

room.leave(u1)
    