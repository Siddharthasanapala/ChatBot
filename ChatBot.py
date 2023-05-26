from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
chatbot=ChatBot("BOT")
trainer=ListTrainer(chatbot)
trainer.train(["hi","hello my dear friend!😊"])
trainer.train(["how are you","I am fine thanks for asking.\n    what about you ?"])
trainer.train(["what is your name","I dont have any specific name but you can call me siddhu"])
trainer.train(["what is your age","I dont have age"])
trainer.train(["tell me a joke","You look so cute..🤣🤣🤣"])
trainer.train(["are you a human","No iam not i am a humanoid machine"])
trainer.train(["can we play game","Nope.! iam virtual ,can't play with you"])
trainer.train(["you look good","Thankyou my dear friend for your compliment!😊.But i am not visible"])
exit_conditions=("quit","exit","Bye","Nice to meet you","will get back soon")

while True:
    query = str(input("👦> "))
    if query in exit_conditions:
        print("🤖 ok 👋 Have a nice day 😊")
        break
    else:
        if chatbot.get_response(query):
            print(f"🤖 {chatbot.get_response(query)}")
        else:
            print(f"🤖 I couldn't get you..!")


