from Experiences import *
from Violet import *
from Questions import *
from Answers import *



texts = [] 

#ASYNC PORTION 1
conversation = texts.join("\n")
q = Questions()
questions = q.socrates(conversation)
ans = Answers()
answers = ans.davidHilbert(conversation, questions)
vio = Violet(conversation, answers)

def p1(texts): #Regenerates basic response based on user input
    texts = input
    conversation = texts.join("\n")
    questions = q.socrates(conversation)
    answers = ans.davidHilbert(conversation, questions)

experiences = []
#ASYNC PORTION 2
def p2(): #Generates once initially to get experiences/emotional distribution of AI
    exps = Experiences()
    exps.violetExps(experiences=[], manualExperiences=[]) #TODO Update with actual experiences from John

def updateConvo(conversation):
    for i in range(len(conversation)):

#TODO Implement multithreading to sufficiently speed up Violet's runtime
v = Violet(input, characteristics, experiences, emotion, age="22", gender="female")
print(v.output)