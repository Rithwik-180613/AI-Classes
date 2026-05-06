print("Hi I am your Chatbot")
print("Typr bye to stop chatting")
while True:
    x=input("Enter your Prompt").lower()
    if(x=='hi'):
        print("Hello,How can I help you!")
    elif(x=='how are you'):
        print('I am doing Good')
    elif(x=='how are you feeling now'):
        print('I am Happy')
    else:
        print("Bye !!! Have a nice day")
        break           