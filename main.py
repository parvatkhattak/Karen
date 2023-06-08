# importing necessary modules
import speech_recognition   # for speech recognising
import win32com.client      # for communication between user and system
import webbrowser           # for opening webpages
import os                   # for interacting with operating system
import datetime             # for getting date and time
import openai               # for interacting with OpenAI API
from config import apikey   # for getting apikey
import subprocess           # for opening apk files

# initializing a variable
chatStr = ""   # to store input from user

# defining a function to perform conversation between user and system(Karen)


def chat(query):
    global chatStr
    openai.api_key = apikey
    # to add user's input to chatStr
    chatStr += f"User:{query}\n Karen: "
    # generating responses from OpenAI API based on chat history
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=chatStr,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo : try to wrap this in a try catch block
    # adding the responses by openAI to chatStr and returning
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write((text))

# defining a function to generate AI responses using OpenAI


def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for prompt:{prompt} \n******************************\n\n"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo : try to wrap this in a try catch block
    print(response["choices"][0]["text"])
    # adding responses to a text file with a specific name based on prompt given
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    with open(f"Openai/{''.join(prompt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write((text))

# defining function to speak the given text using Microsoft Zira voice


def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Voice = get_voice_by_name(
        "Microsoft Zira")  # Use Microsoft Zira voice
    speaker.Speak(text)

# defining a function to retrieves the voice object to the corresponding voice name


def get_voice_by_name(name):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    voices = speaker.GetVoices()

    for voice in voices:
        if name.lower() in voice.GetDescription().lower():
            return voice

    return None


# defining a function that takes audio input from user and recognising using google recognisation that gets returned as query
def takeCommand():
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        # r.pause_threshold = 0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"user said:{query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Karen"

# main program logic


def main():
    # program starts by speaking a greet message
    say("Hello, I am Karen How can I help you?")
    # using an infinite loop to continuously listen for user input
    while True:
        print("Listening...")
        # taking user query by using takeCommand()
        query = takeCommand()
        # todo : we can add more sites
        # providing some common websites URL
        if "Open youtube".lower() in query.lower():
            say("Opening youtube Sir...")
            webbrowser.open("https://www.youtube.com")
        elif "Open wikipedia".lower() in query.lower():
            say("Opening wikipedia Sir...")
            webbrowser.open("https://www.wikipedia.com")
        elif "Open google".lower() in query.lower():
            say("Opening google Sir...")
            webbrowser.open("https://www.google.com")
        elif "Open whatsapp".lower() in query.lower():
            say("Opening whatsapp Sir...")
            webbrowser.open("https://web.whatsapp.com")
        elif "Open moodle".lower() in query.lower():
            say("Opening moodle Sir...")
            webbrowser.open("https://lms.iitpkd.ac.in/login/index.php")
        elif "Open instagram".lower() in query.lower():
            say("Opening insta Sir...")
            webbrowser.open("https://www.instagram.com/")
        elif "Open Quara".lower() in query.lower():
            say("Opening Sir...")
            webbrowser.open("https://es.quora.com/")
        elif "open stackoverflow" in query.lower():
            say("Opening Sir...")
            webbrowser.open("https://stackoverflow.com/")

        # giving instructions to open calculator
        elif "open calculator" in query:
            path = "calc.exe"
            subprocess.Popen(path)

        # for returning time
        elif "the time today" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"Sir the time is {strfTime}")

        # for returning date
        elif "the date today" in query:
            strfDate = datetime.datetime.now().strftime("%Y-%m-%d")
            say(f"Sir, today's date is {strfDate}")

        elif "the day today" in query:
            day = datetime.datetime.now().strftime("%A")
            say(f"sir the day today is {day}")

        # if the query contains " using artificial intelligence" call ai()
        elif "Using artificial intelligence".lower() in query.lower():
            ai(prompt=query)

        # for exiting the program
        elif "Karen quit".lower() in query.lower():
            exit()

        # for reset past chat
        elif "Karen reset chat".lower() in query.lower():
            chatStr = ""
        else:
            # if the query doesn't contains any specified task mentioned above, it will call the chat()
            print("Chatting...")
            chat(query)


# calling main function
main()
