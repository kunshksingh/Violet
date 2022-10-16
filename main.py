from Experiences import *
from Violet import *
from Questions import *
from Answers import *


texts = [] 
v = Violet()

#ASYNC PORTION 1
q = Questions()
questions = None
ans = Answers()
answers = None
characteristics = []

def p1():
    '''
    Regenerates response of Violet based on the current conversation stored as a list (texts).

    In: List[str]
    Out: None (updates Violet)
    '''
    questions = q.socrates(v.convo, (v.convo.split(':')[-1]))
    v.insight = ans.davidHilbert(v.convo, questions)


experiences = []
#ASYNC PORTION 2
def p2(): #TODO Also generate "qualities" from Characteristics.py
    '''
    Generates Violet's emotional distribution based on her past experiences

    In: None
    Out: None (updates Violet)
    '''
    exps = Experiences()
    em = Emotion()
    experiences = exps.violetExps(experiences=[], manualExperiences=[])#TODO Update with actual experiences 
    v.characteristics = (', ').join(list(experiences.keys()))[:-2] #Keys are characteristics
    v.emotion = em.emotionalDistribution(experiences)

def updateConvo(conversation,texts=None): #Conversation used for testing
    '''
    Updates conversation based on input, and returns what Violet should say.

    In: texts: List[str]
    Out: output: str
    '''
    #conversation = texts.join("\n") #May need to change the way this works
    v.convo = conversation
    p1()
    v.output = v.generate_output()
    return v.output
def parseConvo(conversation):
    '''
    Adds relevant 'T:' and 'P:' to help Violet better parse the AI model

    In: conversation: str
    Output: parsed: str
    '''
    conversation.strip()
    splitvos = conversation.split('\n')
    parsedList = []
    i = 0
    j = 0
    while j<len(splitvos):
        if i%3== 0:
            parsedList.append("T: "+str(splitvos[j]))
            i += 1
            j += 1
        elif i%3 == 1:
            parsedList.append("P: "+str(splitvos[j]))
            i += 1
            j += 1
        else:
            parsedList.append("\n")
            i += 1
            j += 1
    parsed = ("\n").join(parsedList)
    return parsed

#TODO Implement multithreading to sufficiently speed up Violet's runtime
#p2()
c  = """Hi! How may I help you?
I'm feeling down lately.

That sounds tough. I'm here to listen if you want to talk about it.
I don't really know, how would a therapist help me?

Well, sometimes it can be helpful to talk to someone who will understand and can offer helpful advice. Is there anything in particular you would like to talk about?
I don't know where to start.

That's okay. Why don't we start with telling me a little bit about yourself?
I'm... a college school student I guess. I'm in my second year.

What's been going on that's been tough for you lately?
I feel like I'll never be enough. I don't know this feels kind of useless

It sounds like you've been going through a lot lately. I'm here for you if you want to talk about anything that's on your mind. I'm also happy to offer any advice or resources that may be helpful.
I hate you. I don't want to talk about that."""
print(parseConvo(c))
#print(updateConvo(conversation=c))
