from random import choice
from sys import exit

import speech_recognition as sr
from pyttsx3 import speak

from assistant import commands_dict
from browser import *
from system import off_computer
from config import dialog_with_chatgpt


def listing_command():
    rec = sr.Recognizer()
    rec.pause_threshold = 0.5

    with sr.Microphone() as source:
        print('Karen: ...')

        rec.adjust_for_ambient_noise(source, duration=0.5)
        audio = rec.listen(source=source)
    try:
        text = rec.recognize_google(audio, language='ru-Ru').lower()

        print('Вы: ' + text[0].upper() + text[1:])
    except sr.UnknownValueError:
        text = 'Не понимаю, повторите.'
        print('Karen: ' + text)

    return text


def main():
    query = listing_command()
    flag = False
    if query == 'Не понимаю, повторите.':
        return main()

    for k, v in commands_dict['function_commands'].items():
        if query in v:
            speak(globals()[k]())
            flag = True
        if flag:
            break

    for k, v in commands_dict['hard_commands'].items():
        if query.split()[0] in v:
            speak(globals()[k](query))
            flag = True
        if flag:
            break

    for k, v in commands_dict['base_answer'].items():
        if query in k:
            speak(choice(commands_dict['base_answer'][k]) if isinstance(
                commands_dict['base_answer'][k], list) else commands_dict['base_answer'][k])
            flag = True
        if flag:
            break

    return main()


if __name__ == '__main__':
    main()
