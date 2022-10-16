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
characteristics = ""

def p1(texts): #Regenerates basic response based on user input
    texts = input
    conversation = texts.join("\n")
    questions = q.socrates(conversation)
    answers = ans.davidHilbert(conversation, questions)

experiences = []
#ASYNC PORTION 2
def p2(): #Generates once initially to get experiences/emotional distribution of AI
    exps = Experiences()
    experiences = exps.violetExps(experiences=[], manualExperiences=[]) 
    characteristics = list(experiences.keys()).join(', ')[:-2] #Keys are characteristics

def updateConvo(conversation):
    vio.conversation = conversation
    for i in range(len(conversation)):

#TODO Implement multithreading to sufficiently speed up Violet's runtime
v = Violet(conversation, answers, characteristics, emotions)
print(v.output)