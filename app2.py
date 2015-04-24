from flask import Flask, render_template, request, redirect, url_for
import time
import re
import random
from random import randint
import pyttsx

app = Flask(__name__)

@app.route('/')
def make_index_resp():
    return(render_template('index.html'))

@app.route('/QA/',methods=['GET','POST'])
def get_an_answer():
    if request.method == 'GET':
        return(render_template('QA.html'))
    elif request.method == 'POST':
        
        namelist=['Abbott','zhao','McRoberts','John_Padgett']
        name=''
        response=''


        if request.form['question']==u'':
            sociologist = int(request.form['mySelection'])
            mac=''
            p=''
            z=''
            #info=request.form
            #question = request.form['question']
            if sociologist==13:
                name=namelist[3]
                p='selected="selected"'
                
            if sociologist==12:
                name=namelist[2]
                mac='selected="selected"'
            if sociologist==21:
                name=namelist[1]
                z='selected="selected"'
            if sociologist==1:
                name=namelist[0]
            return render_template('QA.html', name=name,answer = response,mac=mac,p=p,z=z)
        if not request.form['question']==u'':
            mac=''
            p=''
            z=''
            #info=request.form
            sociologist = int(request.form['mySelection'])
            if sociologist==13:
                name=namelist[3]
                p='selected="selected"'
            if sociologist==12:
                mac='selected="selected"'
                name=namelist[2]
            if sociologist==21:
                name=namelist[1]
                z='selected="selected"'
            if sociologist==1:
                name=namelist[0]
            question = request.form['question']
            if not (sociologist==13 or sociologist==12 or sociologist==21):
                
                time.sleep(1)
                response="So sorry, I am busy watching the folly!! Try asking someone else"
            if sociologist == 13:
                p='selected="selected"'
                match0 = re.search("institutions|Institution|insitution|insitition|Institutions|instituions|instition", question)
                match1 = re.search("rich|Rich|Richs|richs|poor", question)
                match2 = re.search("Why|What|why|what", question)
                match3  = re.search("cease|ceaze", question)
                match4  = re.search("agency|Agency|agensy|agnecy", question)
                match5  = re.search("How|how", question)
                match7 = re.search("fictional|fictionsal|Fictional", question)
                match6 =re.search("autocatalysis of autocatalysis|auto", question)
                find=False
                if match0:
                    find=True
                    time.sleep(1)
                    response = "First of all, this folly is gorgeous. Well, Social institutions persist because they are networks of nodes and transformations in which all nodes are reconstructed through transformations among nodes in the networks. From now on, I'll call it 'autocatalysis.'"
                if not match0 and match1:
                    find=True
                    time.sleep(1)
                    response = "It's an autocatalysis."
                if not match0 and match2:
                    find=True
                    time.sleep(1)
                    response = "Autocatalysis"	
                if match2 and match3:
                    find=True
                    time.sleep(1)
                    response = "It's a failed autocatalysis."
                if match4:
                    find=True
                    time.sleep(1)
                    response = "You know what, that's a silly question. The word 'agency' does not exist in my dictionary."
                if match5:
                    find=True
                    time.sleep(1)
                    response = "It's an autocatalysis of autocatalysis, a hyper-autocatalysis."
                if match7:
                    find=True
                    time.sleep(1)
                    response = "What makes you think that fictional things are not autocatalysis?"
                if match6:
                    find=True
                    time.sleep(3)
                    response = "It's... an autocatalysis of autocatalysis of autocatalysis"
                if find==False:
                    time.sleep(2)
                    response="I am not sure what your are asking...maybe there is a typo"
            if sociologist == 12:
                mac='selected="selected"'
                m = randint(0,1)
                if m == 1: 
                    time.sleep(1)
                    response = "That's cool."
                if m == 0:
                    time.sleep(1)
                    response = "That's fascinating. The folly is fascinating"
                match = re.search("and", question)
                if match:
                    time.sleep(1)
                    response = "That's cool and fascinating. autocatalysis is fascinating"
            explodeDetect=False
            if sociologist == 21:
                find=False
                z='selected="selected"'
                match = re.search("Durkheim|durkeim|durkheim|durkhaim|durheim|duheim|durkaim|dukeim|duerkeim|duerkheim", question)
                if match:
                    find=True
                    time.sleep(1)
                    response = "Durkheim, idiot,  work's nonsense."
                match1 = re.search("Weber|weber|waber|max|Marx|Max", question)
                if match1:
                    find=True
                    time.sleep(1)
                    response = "Weber is not smart at all."
                match2 = re.search("Granovetter|gran|novet|Gran", question)
                if match2:
                    find=True
                    time.sleep(1)
                    response = "ha, Granovetter, not a good sociologist. He writes too little."
                match3  = re.search("cited|Cite|Cited", question)
                if match3:
                    find=True
                    time.sleep(1)
                    response = "Citations, ...,all bullshit."
                match4  = re.search("Tilly|till|tily|Tily", question)
                if match4:
                    find=True
                    time.sleep(1)
                    response = "...Bad."
                match5  = re.search("Mann|mann|man|Man", question)
                if (not match1) and match5:
                    find=True
                    time.sleep(1)
                    response = "...His first book is Good."
                match6 = re.search("Abbott|abbot|abbott|Abbot|Abott|bot", question)
                if (not match5) and (not match4) and match6:
                    find=True
                    time.sleep(1)
                    response = "Haha, Andy is smart."
                match7 = re.search("Zhao|zhao", question)
                if match7:
                    find=True
                    time.sleep(1)
                    explodeDetect=True
                    response = "Warning: High concentration of energy is detected. The system will explode in thirty seconds."
                match0 = re.search("sociologists|sociologist|socioligist|sociloguist|sociolist", question)
                if match0:
                    find=True
                    response = "No problem. Please just input a name."
                if find==False:
                    response="say it again, there are too many laughings, I couldn't hear you clearly"
            engine = pyttsx.init()
            voices = engine.getProperty('voices')

            engine.setProperty('voice',u'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')
            if sociologist==2 or sociologist==4 or sociologist==15 or sociologist==19:
                engine.setProperty('voice',u'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0')
                engine.setProperty('rate',170)
            if sociologist==8:
                engine.setProperty('voice',u'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
            # if sociologist == 13:
            #     engine.say("First of all, this folly is gorgeous")
            if sociologist ==12:
                engine.setProperty('rate',19)
                mac='selected="selected"'
            engine.say(response)
            if explodeDetect==True:
                engine.setProperty('voice',u'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-GB_HAZEL_11.0')
                engine.setProperty('rate',255)
                for i in range(30):
                    time.sleep(0.1)
                    engine.say(str(30-i))
                    engine.setProperty('volume',engine.getProperty('volume')*1.2)
                
                
            # for voice in voices:
            #   engine.setProperty('voice', voice.id)  # changes the voice
            #   print voice.id
            #   engine.say(response)
            engine.runAndWait() 
                 	

            return render_template('QA.html', name=name,answer = response,mac=mac,p=p,z=z)#selected_p = selected_p, selected_m = selected_m, selected_z = selected_z) 
        # else:
        #     return render_template('QA.html')  	
if __name__ == '__main__':
    app.debug=True
    app.run()