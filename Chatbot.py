print("Hi I am your Chatbot")
print("Type bye to stop chatting")
x=input("Enter your Prompt").lower()
while x=='bye':
    if(x=='hi'):
        print("Hello,How can I help you!")
    elif(x=='how are you'):
        print('I am doing Good')
    elif(x=='how are you feeling now'):
        print('I am Happy')  
    elif(x=='what is your name'):
        print('My name is Chatbot')
    elif(x=='what is your favourite color'):
        print('My favourite color is Blue')
    elif(x=='what is your favourite food'):
        print('My favourite food is Pizza')
    elif(x=='what is your favourite movie'):
        print('My favourite movie is Inception')
    x=input("Enter your Prompt").lower()
print("Bye !!! Have a nice day")
