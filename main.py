import speech_recognition as sr
from datetime import datetime
import pyttsx3
from openai import OpenAI


client = OpenAI()

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Verbal is listening...")

        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)

        print(f"You said: {text}")

        return text

    except sr.UnknownValueError:
        print("Verbal couldn't understand that.")

    except sr.RequestError as error:
        print(f"Speech recognition error: {error}")

    return None


def save_message(speaker, text):
    with open("conversation.txt", "a", encoding="utf-8") as file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file.write(f"[{timestamp}] {speaker}: {text}\n")

def respond_to_message(message):
    message = message.lower()
    
    shutdown_phrases = [
        "goodbye homie",
        "goodbye hom",
        "shut down homie",
        "stop listening homie"
    ]

    greeting_phrases = [
        "hello homie",
        "hey homie",
        "yo homie",
        "what's up homie"
    ]

    how_are_you_phrases = [
        "how are you",
        "how's it going",
        "how are you doing"
    ]

    whats_your_name_phrases = [
        "what's your name",
        "who are you"
    ]

    name_questions = [
        "what's the name of this program"
    ]

    if any(phrase in message for phrase in shutdown_phrases):
        return "Goodbye! Have a great day!", True
    
    elif any(phrase in message for phrase in greeting_phrases):
        return "Hello! Systems are running smoothly!", False

    elif any(phrase in message for phrase in how_are_you_phrases):
        return "I'm just a program, but I'm functioning as expected!", False

    elif any(phrase in message for phrase in whats_your_name_phrases):
        return "I'm Homie, your virtual assistant.", False
    elif any(phrase in message for phrase in name_questions):
        return "This program is called Homie, your virtual assistant.", False
    else:
        return "Sorry, I couldn't understand that.", False

    
#  Basic version of respond_to_message function without using lists and any() function
#     elif "hello homie" in message:
#         return "Hello! How can I assist you today?", False

#     elif "how are you" in message:
#         return "I'm just a program, but I'm functioning as expected!", False

#     elif "what's your name" in message:
#         return "I'm Homie, your virtual assistant.", False

#     else:
#         return "I'm not sure how to respond to that.", False
# 

def should_shutdown(message):
    shutdown_phrases = [
        "goodbye homie",
        "goodbye hom",
        "shut down homie",
        "stop listening homie"
    ]

    message = message.lower()

    return any(phrase in message for phrase in shutdown_phrases)

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def ask_ai(message):
    response = client.responses.create(
        model="gpt-5.6-luna",
        input=message
    )

    return response.output_text

def main():
    print("Homie is online.")

    while True:
        message = listen()

        if message:
            save_message("User", message)

            if should_shutdown(message):
                response = "Goodbye! Have a great day!"
                should_exit = True
            else:
                response = ask_ai(message)
                should_exit = False

            save_message("Homie", response)

            print(f"Homie: {response}")
            speak(response)

            if should_exit:
                print("See ya!")
                break

if __name__ == "__main__":
    main()
