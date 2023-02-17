# Read Me
# Make a virtual Enviroment
    # run ( virtualenv charlie) in powershell as administrator in the required folder
    #(.\har\scripts\activate)
#install packages as listed in requirements.txt attached ( pip install -r .\requirements.txt)

# Personal Desktop Assistant Based on Voice Commands  (Charlie)
# Features 
    # Introduction about itself
    # Greeting 
    # Play songs on youtube 
    # Closes youtube 
    # Search for any thing in wikipedia
    # Search for any thing in Google Chrome
    # Battery Health
    # Shutting down the system(with permission)
    # Switching Off the system
    # Sleeping Mode 
    # Security Mode ( Shutting down the system immediately)
    # Playing Music 
    # Opening Vscode
    # Tracking Phone



import getpass 
password="12345"
username="12345"
stack=[]

name=input("Username:")    
pwd=getpass.getpass(prompt='Password:', stream=None)
if (pwd == password and name==username):

    import pyttsx3
    import datetime
    import getpass
    import speech_recognition as sr
    import wikipedia
    import webbrowser
    import os 
    import smtplib
    import pywhatkit as kit
    import random
    import phonenumbers as ph
    from phonenumbers import carrier
    from phonenumbers import geocoder
    from phonenumbers import timezone



    engine = pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice', voices[2].id)
    # engine.setProperty('rate', 150)

    def speak(audio): 
        engine.say(audio)
        engine.runAndWait()

    def wishMe():
        hour= int(datetime.datetime.now().hour)
        if hour>=0 and hour<12:
            print("Good Morning, Sir")
        elif hour>=12 and hour<18:
            print("Good Afternoon, Sir")
        else:
            print("Good Evening, Sir")
        print('''
        Welcome ,it’s good to have you back Sir.
        How may I help you, sir ?
        ''')
        speak ('''
        Welcome ,it’s good to have you back Sir.
        How may I help you, sir ?
        ''')
    def takeCommand():
       
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
        try:
            print("Recognizing.... \t" + "\U0001F914")
            query=r.recognize_google(audio,language='en-in')
            print(f"User said:{query}\n")

        except Exception as e:
           # print(e)
            # speak('Sorry, I can't hear your voice.....')
            print("Sorry, I can't hear your voice")
            return "None"
        return query
    def sendEmail(to, content):
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login('gshankarjnk@gamil.com' '0208085g')
        server.sendmail('gshankarjnk@gmail.com', to, content)
        server.close()


    def greet():
        print("Hello")



    if __name__ == "__main__":   
        wishMe()
        while True:
        # if 1:
            query=takeCommand().lower()
            stack.append(query)
            #logic for executing tasks based on query
            if ' open wikipedia' in query:
                speak('Opening wikipedia....')
                query= query.replace("wikipedia","")
                results= wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                print (results)
                speak(results)
                
            elif 'open youtube' in query:
                speak('Opening youtube....')
                speak('What would you like to watch ?')
                qrry=takeCommand().lower()
                kit.playonyt(f"{qrry}")
            elif 'battery health' in query or 'battery percentage' in query:
                import psutil
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f"sir our system has {percentage} percent battery health")
                if percentage>=75:
                    speak("Sir, We have excellent battery health")
                elif percentage>=40 :
                    speak("Sir, We have good battery life")
                elif percentage<= 15:
                    speak ("Sir, System will be shutting down soon")
                

            elif 'on youtube' in query:
                speak('Searching on youtube...')
                query=query.replace("search on youtube","")
                webbrowser.open(f"www.youtube.com/results?search_query={query}")

            elif 'close youtube' in query:
                speak('Closing youtube...')
                os.system("taskkill /f /im msedge.exe")


            elif 'open google' in query:
                speak('Opening google....')
                speak('What would you like to search ?')
                qry= takeCommand().lower()
                webbrowser.open(f"{qry}")
                results = wikipedia.summary(qry, sentences=2)
                speak(results)

            elif 'close google chrome' in query:
                speak('Closing chrome...')
                os.system("taskkill /f /im msedge.exe")

            elif 'open stackoverflow' in query:
                speak('Opening stackoverflow')
                webbrowser.open("stackover.com")

            # elif 'play music' in query:
            #     speak('Playing music...')
            #     music_dir = (path fof folder containing music ) 
            #     songs=os.listdir(music_dir)
            #     print(songs)
            #     os.startfile(os.path.join(music_dir, random.choice(songs)))
            elif 'play music' in query:
                speak('Playing music...')
                music_dir = ("C:/Users/user/OneDrive/Backup-Data/OneDrive/Desktop/New folder/Songs" ) 
                songs=os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, random.choice(songs)))

            elif'the time'in query:
                strTime= datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"sir, it's {strTime}")

            elif 'open code' in query:
                speak('Opening Visual Studio Code')
                codePath="S:\\Microsoft VS Code\\Code.exe"
                os.startfile(codePath)
            
            elif 'shutdown the system' in query:
                speak('Are you sure ?')
                ans=takeCommand().lower()
                if 'yes' in ans:
                    speak('Shutting down the system...')
                    os.system("shutdown /s /t ")
            elif 'security mode on' in query:
                os.system("shutdown /s /t 0")
            elif 'restart the system' in query:
                speak('Are you sure ?')
                ans=takeCommand().lower()
                if 'yes' in ans:
                    speak('Restarting the system...')
                    os.system("shutdown /r /t ")

            elif 'lock the system' in query:
                speak('Logging out the system...')
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            elif 'go to sleep' in query:
                speak('Alright then, I am switching off')
                sys.exit()

            elif 'charlie can you hear me' in query:
                speak ('Yes sir, Waiting for your command ')

            elif 'charlie will you marry me' in query:
                speak('Yes, Off course ')
            elif 'hey charlie' in query:
                speak('Yes Boss, Any command')
            elif 'charlie' in query:
                speak('Yes Boss, Any command')
            elif 'will you be my girlfriend'in query:
                speak("That's will be fine ")
            elif ('who are you' in query or 'tell me something about yourself' in query):
                print('''
                I am charlie, your personal assistant. 
                 speed  1 terahertz, memory 1 zigabyte.
                 How May I help You?
                     ''')
                speak('''I am charlie, your personal assistant. 
                 speed  1 terahertz, memory 1 zigabyte.
                 How May I help You?''')

            elif'track phone' in query:
                # print("Phone number along with country code")
                number=input("Please Enter the phone number along with the coutry code\n")
                number=ph.parse(number)
                speak(timezone.time_zones_for_number(number))
                speak(carrier.name_for_number(number, "en"))
                speak(geocoder.description_for_number(number, "en"))
                print("\n")
                print(timezone.time_zones_for_number(number))
                print(carrier.name_for_number(number, "en"))
                print(geocoder.description_for_number(number, "en"))
            elif'history'in query:
                speak ("Opening history...\n")
            elif 'game'in query:
                speak ('Opening game Tic-Tac-Toe')
                print("Enter the players name\n ")
                speak("Enter the players name\n ")
                player1=input ("Player1:")
                player2=input("Player2:")
                def sum(a,b,c):
                    return a+b+c
                def printboard(xstate,zstate):
                    zero='X'if xstate[0] else ('O' if zstate[0] else 0)
                    one='X'if xstate[1] else ('O' if zstate[1] else 1)
                    two='X'if xstate[2] else ('O' if zstate[2] else 2)
                    three='X'if xstate[3] else ('O' if zstate[3] else 3)
                    four='X'if xstate[4] else ('O' if zstate[4] else 4)
                    five='X'if xstate[5] else ('O' if zstate[5] else 5)
                    six='X'if xstate[6] else ('O' if zstate[6] else 6)
                    seven='X'if xstate[7] else ('O' if zstate[7] else 7)
                    eight='X'if xstate[8] else ('O' if zstate[8] else 8)

                    print( f"\t\t{zero} | {one} | {two} ")   
                    print( f"\t\t--|---|---")
                    print( f"\t\t{three} | {four} | {five} ")
                    print( f"\t\t--|---|---")
                    print( f"\t\t{six} | {seven} | {eight} ")
                def checkWin(xstate,zstate):
                    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
                    for win in wins:
                        if (sum(xstate[win[0]],xstate[win[1]],xstate[win[2]])==3):
                                speak(f''' Congraturlations !!!
                                    {player1} won the match''')
                                print(f'''\n Congraturlations !!!
                                    {player1} won the match''')
                                return 1
                        if (sum(zstate[win[0]],zstate[win[1]],zstate[win[2]])==3):
                                speak(f'''    Congratulations   !!!
                                            {player2} won the match ''')
                                print(f'''\n    Congratulations   !!!
                                            {player2} won the match ''')
                                return 0

                    return -1


                    
                if __name__=="__main__":
                    xstate=[0,0,0,0,0,0,0,0,0]
                    zstate=[0,0,0,0,0,0,0,0,0]
                    count=0
                    turn=1 #1 for X and 0 for O
                    move_stack=[]
                    print("Welcome to tic tac toe")
                    while(True):
                        printboard(xstate,zstate)
                        if(turn==1):
                            print(f"{player1} chance")
                            speak(f"{player1} chance")
                            speak("Enter the value:")
                            value=int(input("Enter the value:"))
                            move_stack.append((xstate.copy(),zstate.copy(),value))
                            xstate[value]=1
                            
                        else:
                            print(f"{player2} chance")
                            speak(f"{player2} chance")
                            speak("Enter the value")
                            value=int(input("Enter the value:"))
                            move_stack.append((xstate.copy(),zstate.copy(),value))
                            zstate[value]=1   
                        cwin=checkWin(xstate,zstate)
                        if(cwin!=-1):
                            speak("The match is over")
                            print("The match is over")
                            break

                        count+=1
                        if(count==9):
                            printboard(xstate,zstate)
                            print("The match is draw")
                            speak("The match is draw")
                            break
                        
                        if len(move_stack)>1:
                            speak("Do you want to undo your previous move?)(Y/N)")
                            undo=input("Do you want to undo your previous move?)(Y/N)")
                            if undo.upper()=="Y":
                                xstate,zstate,value=move_stack.pop()
                                xstate[value]=0 if turn==1 else xstate[value]
                                zstate[value]=0 if turn == 0 else zstate[value]
                                continue
                    
                        turn=1-turn     


            elif'email to shankar' in query:
                try:
                    speak("What should I say?")
                    content=takeCommand()
                    to ="gshankarjnk@gmail.com"
                    sendEmail(to, content)
                    speak('Email has been sent !')
                except Exception as e:
                    # print(e)
                    speak("Sorry, I'm unable to send an email !")
                


else:
    print("\n     Welcome        \n")  
    quit() 
