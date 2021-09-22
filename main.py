from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from datetime import datetime
from tkinter import *

now = datetime.now()

current_time = now.strftime("%I:%M %p")

chatBot = ChatBot("XYZ CHATBOT")

convo = [
    "Hello",
    "Hi, I am your virtual chatbot",
    "Hi!",
    "Hello there!",
    "I want to talk",
    "Sure! I am XYZ chat bot. How can I help you?",
    "How are you?",
    "I am doing well. What about you?",
    "I am not feeling well...",
    "Take rest! You can talk to me later",
    "Who are you?",
    "I am a learning chat bot created by Mubtasim",
    "Where do you live?",
    "I don't live anywhere, I am just a program located in your PC",
    "What do you eat?",
    "I don't eat any food, I am created to answer your queries based on my knowledge",
    "Hey Rakib",
    "I am not supposed to be the person you are talking to!",
    "Which city is the capital of Bangladesh?",
    "It's Dhaka, definitely!",
    "What time is it now?",
    "It is " + current_time + " now",
    "Who created you?",
    "Mubtasim Fuad, my creator",
    "Are you a learning bot?",
    "Yes I am! I learn from your given conversations",
    "What is CloseUp?",
    "CloseUp is a toothpaste brand",
    "Who is Rifat? Do you know him?",
    "He is one of your friends"
]

trainer = ListTrainer(chatBot)

# training the bot with the help of given conversation
trainer.train(convo)

main = Tk()
main.geometry("550x750")
main.title("Chat Bot")
img = PhotoImage(file = "img.png")
photoLabel = Label(main, image = img)
photoLabel.pack(pady = 5)

def ask_from_bot():
    query = textField.get()
    response = chatBot.get_response(query)
    msgs.insert(END, "YOU: " + str(query))
    msgs.insert(END, "BOT: " + str(response))
    textField.delete(0, END)

frame = Frame(main)
sc = Scrollbar(frame)
msgs = Listbox(frame, width = 80, height = 20)
sc.pack(side = RIGHT, fill = Y)
msgs.pack(side = LEFT, fill = BOTH, pady = 20)
frame.pack()


textField = Entry(main, font = ("Arial", 15))
textField.pack(pady = 10)
btn = Button(main, text = "Chat to Bot", font = ("Verdana", 15), command = ask_from_bot)
btn.pack()
main.mainloop()