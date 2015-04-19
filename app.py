from flask import Flask, render_template, request, redirect, url_for
import time
import re
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
		sociologist = int(request.form['mySelection'])
		question = request.form['question']
		if sociologist == 13:
			selected_p = "selected"
			selected_m = ""
			selected_z = ""
        	match0 = re.search("social institutions", question)
        	if match0:
        		response = "Social institutions persist because they are networks of nodes and transformations in which all nodes are reconstructed through transformations among nodes in the networks. From now on, I'll call it 'autocatalysis.'"
        	match1 = re.search("rich", question)
        	if match1:
        		response = "It's an autocatalysis."
        	match2 = re.search("Why|What", question)
        	if match2:
        		response = "Autocatalysis"
        	match3  = re.search("cease to exist", question)
        	if match2 and match3:
        		response = "It's a failed autocatalysis."
        	match4  = re.search("agency", question)
        	if match4:
        		response = "A silly question. The word 'agency' does not exist in my dictionary."
        	match5  = re.search("How", question)
        	if match5:
        		response = "It's an autocatalysis of autocatalysis, a hyper-autocatalysis."
        	match7 = re.search("fictional", question)
        	if match7:
        		response = "What makes you think that fictional things are not autocatalysis?"
        	match6 =re.search("autocatalysis of autocatalysis", question)
        	if match6:
        		time.sleep(5)
        		response = "It's an autocatalysis of autocatalysis of autocatalysis"       	
        
        if sociologist == 12:
        	selected_m = "selected"
        	selected_p = ""
        	selected_z = ""
        	m = randint(0,1)
        	if m == 1: 
        		response = "That's cool."
        	if m == 0:
        		response = "That's fascinating."
        	match = re.search("and", question)
        	if match:
        		response = "That's cool and fascinating."

        if sociologist == 21:
        	selected_m = ""
        	selected_p = ""
        	selected_z = "selected"
        	match = re.search("Durkheim", question)
        	if match:
        		response = "Durkheim's work is nonsense."
        	match1 = re.search("Weber", question)
        	if match1:
        		response = "Weber is not smart."
        	match2 = re.search("Granovetter", question)
        	if match2:
        		response = "Granovetter is not a good sociologist. He writes too little."
        	match3  = re.search("cited", question)
        	if match3:
        		response = "Citations are all bullshit."
        	match4  = re.search("Charles Tilly", question)
        	if match4:
        		response = "Bad."
        	match5  = re.search("Michael Mann", question)
        	if match5:
        		response = "Good."
        	match6 = re.search("Abbott", question)
        	if match6:
        		response = "Andy is smart."
        	match7 = re.search("Zhao", question)
        	if match7:
        		time.sleep(10)
        		response = "Warning: High concentration of energy is detected. The system will explode in thirty seconds."
        	match0 = re.search("sociologists", question)
        	if match0:
        		response = "No problem. Please just input a name."

        engine = pyttsx.init()
    	engine.say(response)
    	engine.runAndWait()      	

    	return render_template('QA.html', answer = response, selected_p = selected_p, selected_m = selected_m, selected_z = selected_z)   	
if __name__ == '__main__':
    app.debug=True
    app.run()