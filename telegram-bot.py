import os
import json
import requests
from telegram import Bot
from telegram.ext import CommandHandler, Updater
from dotenv import load_dotenv

load_dotenv()  # Load environment variables

# Your Telegram bot token
TELEGRAM_API_TOKEN = os.getenv('7884840608 : AAFWzcZhjSAewGay0eIPF7IIMxA6ByUDRHg')

# Set up bot
bot = Bot(7884840608 : AAFWzcZhjSAewGay0eIPF7IIMxA6ByUDRHg)

def start(update, context):
    update.message.reply_text("Hello, I'm your bot!")

def lambda_handler(event, context):
    # Set up the updater and dispatcher
    updater = Updater(token=TELEGRAM_API_TOKEN, use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start))

    # Webhook URL to receive updates
    webhook_url = os.getenv('WEBHOOK_URL')
    
    if event.get('httpMethod') == 'POST':
        payload = json.loads(event['body'])  # Get the request payload
        bot.process_new_updates([payload])   # Process the updates via webhook
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'Update received'})
        }

    return {
        'statusCode': 400,
        'body': json.dumps({'message': 'Invalid request'})
    }
