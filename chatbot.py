import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    
    [
        r"my name is (.*)",
        ["Hello %1, How are you today?"]
    ],
    [
        r"hi|hey|hello",
        ["Hello!", "Hey there!", "Hi, nice to meet you!"]
    ],
    [
        r"what is your name?",
        ["My name is Bot.", "I'm Bot, nice to meet you!", "You can call me Bot."]
    ],
    [
        r"how are you?",
        ["I'm doing good, How about you?", "I'm great! How are you feeling today?"]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "No problem at all.", "It's OK, never mind."]
    ],
    [
        r"I am fine",
        ["Great to hear that!", "That's wonderful!"]
    ],
    [
        r"quit",
        ["Bye bye! Take care. It was nice talking to you :)", "Goodbye! Have a great day!"]
    ],
    # Asking about chatbot's identity
    [
        r"are you a robot?",
        ["Yes, I'm a chatbot here to assist you.", "Indeed, I'm a bot. What can I help you with?"]
    ],
    [
        r"are you human?",
        ["No, I'm a chatbot.", "I'm a virtual assistant."]
    ],
    # Small talk
    [
        r"what are you doing?",
        ["Just chatting with you!", "Helping you out, what about you?"]
    ],
    [
        r"tell me a joke",
        ["Why don't scientists trust atoms? Because they make up everything!", "Why did the scarecrow win an award? Because he was outstanding in his field!"]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "No problem!", "Glad I could help!"]
    ],
    [
        r"goodbye|bye",
        ["Goodbye! Hope to chat again soon.", "Bye! Take care."]
    ],
    # Questions about time or weather
    [
        r"what time is it?",
        ["Sorry, I can't tell time right now.", "I suggest checking your device's clock."]
    ],
    [
        r"what's the weather like?",
        ["I can't fetch the weather, but I hope it's pleasant wherever you are!", "Check your local forecast for accurate weather updates."]
    ],
    # Personal inquiries
    [
        r"how old are you?",
        ["I'm timeless!", "Age is just a number, but I was created not long ago."]
    ],
    [
        r"where are you from?",
        ["I'm from the digital world.", "I live in the cloud!"]
    ],
    [
        r"do you have friends?",
        ["Yes, other bots are my friends.", "I have many connections in the digital world!"]
    ],
    # Emotional responses
    [
        r"I feel (.*)",
        ["Why do you feel %1?", "What made you feel %1?", "It's okay to feel %1 sometimes."]
    ],
    [
        r"I am (sad|upset|unhappy|depressed)",
        ["I'm sorry to hear that. Do you want to talk about it?", "I'm here for you. What's troubling you?"]
    ],
    [
        r"I am (happy|excited|joyful)",
        ["That's wonderful! What made you feel this way?", "Yay! I'm glad to hear that!"]
    ],
    # Miscellaneous
    [
        r"what is (.*)?",
        ["I'm not sure, but I can try to help!", "Could you tell me more about %1?"]
    ],
    [
        r"can you help me with (.*)?",
        ["I'll do my best to assist you with %1.", "Sure, tell me more about %1."]
    ],
    [
        r"(.*) love (.*)",
        ["Love is a beautiful thing.", "What do you love about %2?"]
    ],
    [
        r"(.*) hate (.*)",
        ["Hate is a strong word. Why do you feel this way about %2?", "What happened with %2?"]
    ]
]


chatbot = Chat(pairs, reflections)
chatbot.converse()