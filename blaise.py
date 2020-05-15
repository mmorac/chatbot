from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

app = Flask(__name__)

chatbot = ChatBot("Blaise")
trainer = ListTrainer(chatbot)

trainer.train("chatterbot.corpus.spanish")

#Español

trainer.train(["hola", "¡Hola!"])
trainer.train(["hola Blaise", "¡Hola!"])
trainer.train(["cómo te llamas?", "Me llamo Blaise, como Pascal"])
trainer.train(["quién es Mario Mora?", "El jefe (así me dijo que lo llamara) es un ingeniero de software"])
trainer.train(["tiene experiencia", "Sí, ha trabajado por varios años como desarrollador"])
trainer.train(["cómo lo contacto", "Puedes llamarlo al (506)8333-8227 o enviarle un correo a marioemorac.gmail.com"])
trainer.train(["cuantos años tiene", "¡Es súper joven! (no me arriesgaré a que me despidan)"])
trainer.train(["cuáles lenguajes sabe?", "Hasta donde sé, sabe C#, Python, SQL, Javascript y Angular"])
trainer.train(["cuáles idiomas habla?", "Habla español, inglés, portugués y está aprendiendo alemán. Un día de estos se va a volver loco."])

#INGLÉS

trainer.train(["hello", "Hi! Welcome!"])
trainer.train(["hello Blaise", "Hello!"])
trainer.train(["what's your name?", "My name is Blaise, like Pascal"])
trainer.train(["who is Mario Mora?", "The boss (he insisted I call him that) is a Software Engineer"])
trainer.train(["does he have experience?", "Yes, he has been working as a developer formally and just for fun, I am living proof of it."])
trainer.train(["how do I contact him?", "You can call him at (506)8333-8227 or email him to marioemorac.gmail.com"])
trainer.train(["how old is he?", "He is SO young (I don't want to get fired)"])
trainer.train(["which programming languages does he know?", "As far as I know, C#, Python, SQL, Javascript and a bit of Angular"])
trainer.train(["languages does he speak?", "Speaks Spanish (native), English (fluent), Portuguese (fluent) and is learning German. I'm worried he will reach a point where he mixes it all together."])


@app.route("/", methods=["GET", "POST"])

def index():
    if(request.method == "GET"):
        return render_template("index.html")

    if(request.method == "POST"):
        data = request.data
        mensaje = request.form.get('msg')
        respuesta = chatbot.get_response(mensaje.lower())
        return render_template("index.html", mensaje = respuesta)
