# Usage
1. Create a new bot using the BotFather. Get the bot token.
2. Create a new conversation with the bot. Use https://api.telegram.org/botYOUR_API_TOKEN/getUpdates to get the chat_id of the conversation. With python: ```import requests; requests.get('https://api.telegram.org/botYOUR_API_TOKEN/getUpdates')```
3. Put the token and chat id inside the main.py file. 
4. Modify the crontab file if you want to change the updating interval. Default is 10 minutes (i.e. every 10 minutes the bot checks if the ip changed and eventually sends it to you). 
5. Build the image: ```sudo docker build . -t ip-bot```
6. Run the bot: ```bash run.sh```. By default, it will always run (and start-again if the machine restarts).