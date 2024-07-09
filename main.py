import speech_recognition as sr
import requests
import os
import random
from playsound import playsound
from gtts import gTTS
import subprocess
from time import sleep


recognizer = sr.Recognizer()

def speak(string):
    tts = gTTS(text=string, lang='tr', slow=False)
    rand = random.randint(1, 30)
    sayi = 1 + rand
    file = f"answer{sayi}.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

def make_phone_call(phone_number):


    command = f'adb shell am start -a android.intent.action.CALL -d tel:{phone_number}'
    subprocess.run(command, shell=True, check=True)
    print(f"{phone_number} numarasını aradım.")
    input()
    speak("Merhaba Emin Bey Buyrun")





phone_number = "+905457302177"  # Aranacak telefon numarasını buraya ekleyin
make_phone_call(phone_number)

def send_message_to_discord(message):
    payload = {
        'mesaj': message,
        'ip': '::1',
        'url': 'https://discord.com/api/webhooks/1072139576820383834/6WN9Rhnq9HI0G6Sc44ZAwAFPPYsT0Aopw_AHNjlB0qLhb6TivArYDv4zGcPo4KFt-pEb'
        }

    res = requests.post('https://haqan.dev/zapkins/wp', data=payload)
    print(res.status_code)

def main():
    with sr.Microphone() as source:
        print("Sizi dinliyorum, ne yapabilirim?")
        speak("Sizi dinliyorum, ne yapabilirim?")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language="tr-TR")
        print(f"Siz: {command}")

        if "mesaj yolla" in command:
            response = "Elbette, ne mesajı iletebilirim?"
            print(f"Asistan: {response}")
            speak(response)
            

            # Kullanıcının mesajını al
            with sr.Microphone() as source:
                print("Mesajınızı söyleyin:")
                audio = recognizer.listen(source)
                message = recognizer.recognize_google(audio, language="tr-TR")
                print(f"Siz: {message}")

            # Discord'a mesajı gönder
            send_message_to_discord(message)

            response = "Mesajınız Discord'a gönderildi."
            print(f"Asistan: {response}")
            speak(response)
            
        else:
            response = "Üzgünüm, anlayamadım."
            print(f"Asistan: {response}")
            speak(response)
            

    except sr.UnknownValueError:
        print("Üzgünüm, sizi duyamadım.")
    except sr.RequestError as e:
        print(f"Ses tanıma hatası: {e}")


if __name__ == "__main__":
    main()
    command2 = 'adb shell service call phone 3'
    subprocess.run(command2, shell=True, check=True)
