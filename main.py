import os
from google.cloud import aiplatform
from predict_text_classification_single_label_sample import predict_text_classification_single_label_sample
import discord
from discord.ext.commands import Bot
from dotenv import load_dotenv
load_dotenv()

""" Script to automate Discord chat bot to listen for chat messages, query
Google Cloud Vertex trained model endpoint, and depending on % confidence
of prediction, post reply directing original poster to FAQ link. """

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = Bot(command_prefix="!", intents=intents)

@client.event
async def on_ready():
    print("The bot is ready")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    else:
        print(message.author, message.content)
        # await message.channel.send("hello")

        # obtain prediction based on trained model endpoint
        res = predict_text_classification_single_label_sample(
            project="397132089433",
            endpoint_id="3340817702485753856",
            location="us-central1",
            content=message.content
        )

        pred_dict = dict(res[0])
        confidences = pred_dict['confidences']
        conf_not_question, conf_question = confidences

        if conf_question > conf_not_question:
            bot_reply = f'I am {round(conf_question * 100, 4)}% confident that you asked a question that might be answered in our FAQ at <https://tinyurl.com/zvy9wp98>'
            await message.reply(bot_reply)

client.run(os.getenv("TOKEN"))