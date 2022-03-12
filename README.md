# Telegram-Weather-Bot

## What it is about

This is a python implementation of a Telegram chatbot that can be used to check the weather in your local area.

## Requirements

Python 3.X (tested on 3.10.2)

## How to install

From a console, run the following commands:

```commandline
git clone git@github.com:ravenesco/Telegram-Weather-Bot.git
cd Telegram-Weather-Bot
pip install -r requirements.txt
```

After that you will need to obtain:

1. Telegram Bot token by registering your Telegram bot (refer to BotFather instructions https://t.me/BotFather)
2. OpenWeather API key (create an account at https://openweathermap.org and go to API keys section of your profile)

Then put both tokens into `config.py`

Finally, to run the bot, simply execute the following command from a console:

```commandline
python bot.py
```

## Example of this bot

You will find this bot operational and can test it yourself at:  
https://t.me/RavenescoWeatherBot

Open chat with the bot and type `/start` to initialize it.

Then type `/forecast` to request weather forecast from the bot.
