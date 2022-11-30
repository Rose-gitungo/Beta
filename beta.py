from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
from pymongo.message import query

conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]
chatbot = ChatBot('Beta')
#trainer = ListTrainer(chatbot)
#trainer.train(conversation)
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english.greetings")
while True:
    query = input(">>>")
    print(chatbot.get_response(Statement(text=query, search_text=query)))