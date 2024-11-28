# chatbot


This project demonstrates a simple chatbot built using Python and the NLTK library. The chatbot is programmed to respond to a variety of user inputs based on predefined patterns.

Features
Responds to greetings and small talk.
Handles questions about the chatbot's identity and functionality.
Offers emotional support and reacts to user emotions.
Provides humorous responses and jokes.
Can handle generic queries with basic responses.
Installation
Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/chatbot-nltk.git
cd chatbot-nltk
Install Python Dependencies: Ensure you have Python installed (Python 3.6 or later is recommended). Install the required package:

bash
Copy code
pip install nltk
Download NLTK Data (if required): Run the following commands in Python to ensure all necessary NLTK data is available:

python
Copy code
import nltk
nltk.download('punkt')
How to Run
Open a terminal in the project directory.
Run the chatbot script:
bash
Copy code
python chatbot.py
Start chatting with the bot in the terminal.
Chatbot Rules
The chatbot responds to various patterns defined in the pairs list. Here are some example interactions:

General Greetings
User: "hi"
Bot: "Hello!"
User: "what is your name?"
Bot: "My name is Bot."
Emotional Responses
User: "I am sad."
Bot: "I'm sorry to hear that. Do you want to talk about it?"
Jokes
User: "tell me a joke."
Bot: "Why don't scientists trust atoms? Because they make up everything!"
Exiting
User: "quit"
Bot: "Bye bye! Take care. It was nice talking to you :)"
Customization
You can customize the chatbot by modifying the pairs list in the script.

Add new patterns and responses as needed.
Use regex to create flexible patterns for better matching.
