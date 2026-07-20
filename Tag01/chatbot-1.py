##############################################################################
# OPENAI CHATBOT
##############################################################################
# Soll unser Unternehmen und Produkte kennen
# Soll diesbezüglich auf Kundenfragen möglichst adäquat antworten
# Antworten des ChatBots als MP3 fetchen und abspielen
##############################################################################

from openai import OpenAI                                                       # api klasse von openai SDK importieren
import os, time                                                                 # betriebssystem & time package importieren
from prompts import *                                                           # unsere prompts importieren
from dotenv import load_dotenv                                                  # package um auf .env datei zuzugreifen
from pathlib import Path                                                        # pathlib für parent folder auswahl
import warnings                                                                 # package, dass warnings unterdrücken kann
warnings.filterwarnings("ignore")                                               # warnings unterdrücken (wg. pygame)
from pygame import mixer                                                        # straight forward gui package (hier für sound player)

##############################################################################

load_dotenv()                                                                   # der runtime zugriff auf .env erlauben
client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))                       # objekt für open mkit api key instanzieren

##############################################################################

def get_reply(messages: list):                                                  # funktion für chatbot anfrage
    messages.insert(0, {"role": "system", "content":  SYSTEM_RULES})            # companyinfos und grundlegende regeln als erste message
    messages.insert(1, {"role": "system", "content":  CATALOG})                 # produktkatalog als zweite message
    completion = client.chat.completions.create(                                # text api anfragen: neuer text
        model="gpt-4.1-mini",                                                   # kleineres model genügt hier
        max_completion_tokens=200,                                              # kurze antworten mit begrenztem aufwand erledigen
        messages=messages                                                       # system prompts und chat historie mitgeben
    )
    return completion.choices[0].message.content                                # nur text antwort aus antwort objekt returnen

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def get_speech(text):                                                           # funktion um aus text audio zu generieren
    response = client.audio.speech.create(                                      # audio api anfragen: neue audio
        model="gpt-4o-mini-tts",                                                # text-to-speech model wählen
        voice="alloy",                                                          # stimme wählen
        input=text,                                                             # text übergeben den wir als audio wollen
    )
    return response.content                                                     # nur audio als binary aus antwort objekt holen

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def write_audio(path, audio):                                                   # funktion um audio datei zu speichern
    with open(path, "wb") as file:                                              # blank file für binary stream anlegen und cachen
        file.write(audio)                                                       # audio in stream schreiben

##############################################################################

mixer.init()                                                                    # sound player initialisieren
messages = []                                                                   # liste aus messages vordefinieren
print("-"*100)                                                                  # trennlinie in konsole
for index, msg in enumerate(TEST_QUESTIONS):                                    # loop über unsere testfragen
    messages.append({"role": "user", "content": msg})                           # aktuelle testfrage zu chatverlauf hinzufügen
    assistant_reply = get_reply(messages[:])                                    # echte kopie der messages liste an chatbot
    messages.append({"role": "assistant", "content": assistant_reply})          # antwort von openai zu chatverlauf hinzufügen
    print("CUSTOMER:  ", msg)                                                   # testfrage printen
    print("ASSISTANT: ", assistant_reply)                                       # antwort printen
    print("-"*100)                                                              # trennlinie in konsole
    time.sleep(2)                                                               # 2 sekunden warten

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
'''
    speech_path = Path(__file__).parent / f"speech{index}.mp3"                  # dynamischen pfad und dateinamen für mp3 bauen
    audio = get_speech(assistant_reply)                                         # mp3 holen
    write_audio(speech_path, audio)                                             # mp3 speichern
    time.sleep(2)                                                               # 2 sekunden warten

    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    mixer.music.load(speech_path)                                               # player mit aktueller mp3 laden
    mixer.music.play()                                                          # mp3 abspielen
    while mixer.music.get_busy():                                               # warten bis mp3 fertig abgespielt hat
        time.sleep(1)                                                           # nur 1 mal pro sekunde player status abfragen
'''
##############################################################################