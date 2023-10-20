import pyaudio
import win32com.client
import speech_recognition as sr
import webbrowser as web
import os
import datetime
import openai
qe=""
def chat(topic):
    global qe
    openai.api_key = "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"
    qe=f"subha: {topic}\nradhe: "
   # print(f"subha: {topic}\n")
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": qe
            },
            {
                "role": "user",
                "content": ""
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    qe+=f"{response['choices'][0]['message']['content']}"
    print(qe)
    speaker.Speak(response['choices'][0]['message']['content'])


    return response['choices'][0]['message']['content']







def ai(ram):
  openai.api_key = "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"
  pag=f"Open Ai responce for text {ram} \n *************************************************************************************************** \n \n \n"
  # ram="love letter"
  response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
      {
        "role": "system",
        "content": ram
      },
      {
        "role": "user",
        "content": ""
      }
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
  )
  print(response["choices"][0]["message"]["content"])
  pag += response["choices"][0]["message"]["content"]

  #Todo = create a opein ai file for sroting open ai responce

  if not os.path.exists("Openai"):
      os.mkdir("Openai")
  with open(f"Openai/{''.join(ram.split('intelligence')[1:])}.text","w")as f:
      f.write(pag)


#  creating a voice recognation functon .........................


def voice_licening():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold=1
        audio=r.listen(source)
        try:
            query=r.recognize_google(audio,language="en-in")
            print(f"user said:{query}")
            return query
        except Exception as e:
            return "some error occer"


# main function if will exicuting first............................


if __name__ =='__main__':

    # say computer function use this speaker.Speak("object")...........

    speaker = win32com.client.Dispatch("SAPI.SpVoice")
while(1):
    print("lisin..")


#  call voice funtion call....................


    test =voice_licening()

   #  web pages opening.............................................................


    sites=[["youtube","https://www.youtube.com/"],["facebook","https://www.facebook.com/"],["wikipedia","https://www.wikipedia.org/"],["google","https://www.google.com/"]]
    for site in sites:
        if (f"opening {site[0]}".lower() in test.lower()):

            speaker.Speak(f"{test} sir..")
            web.open(site[1])


    #  file and music  opening.............................................................


    if("opening music".lower() in test.lower()):
        music_path= "C:/Users\subha\Downloads\dil.mp3"
        # p="C:/Users\subha\Desktop\WhatsApp - Shortcut.lnk"
        #t="C:/Users\subha\Downloads/roma.jpg"
        os.startfile(music_path)


        #  current time saying.............................................................


    elif("what is the time".lower() in test.lower()):

        time=datetime.datetime.now().strftime("%H:%M:%S")
        #t="C:/Users\subha\Downloads/roma.jpg"
        speaker.Speak(f"sir this time is {time}")



    # app opening...................................................................

    apps = [["whatsapp", "C:/Users\subha\Desktop\WhatsApp - Shortcut.lnk"],
            ["vscode", "C:/Users\subha\Desktop\Visual Studio Code.lnk"],
            ["calculator", "C:/Users\subha\Desktop\Calculator - Shortcut.lnk"],
            ["spotify", "C:/Users\subha\Desktop\Spotify.lnk"]]

    for app in apps:
        if (f"opening {app[0]}".lower() in test.lower()):

            speaker.Speak(f"{test} sir..")
            web.open(app[1])

    if("using artificial intelligence".lower() in test.lower()):
        a=ai(ram=test)
    elif("quite".lower() in test.lower()):
        exit()
    elif("reset".lower() in test.lower()):
        qe=""

    else:
        p=chat(test)
