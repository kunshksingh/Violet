from Experiences import *
from Violet import *
from Questions import *
from Answers import *


texts = [] 


#ASYNC PORTION 1
q = Questions()
questions = None
ans = Answers()
answers = None
characteristics = []
v = Violet()
class Main():
    def __init__(self):
        v = Violet()

    def p1(self):
        '''
        Regenerates response of Violet based on the current conversation stored as a list (texts).

        In: List[str]
        Out: None (updates Violet)
        '''
        questions = q.socrates(v.convo, (v.convo.split(':')[-1]))
        v.insight = ans.davidHilbert(v.convo, questions)


    experiences = []
    #ASYNC PORTION 2
    def p2(self): #TODO Also generate "qualities" from Characteristics.py
        '''
        Generates Violet's emotional distribution based on her past experiences

        In: None
        Out: None (updates Violet)
        '''
        exps = Experiences()
        em = Emotion()
        f = open("experienceData.txt", "r")
        readExperiences = f.read()
        f_content = readExperiences.split('\n\n')
        experiences = exps.violetExps(experiences=[], manualExperiences=[])#TODO Update with actual experiences 
        v.characteristics = (', ').join(list(experiences.keys()))[:-2] #Keys are characteristics
        v.emotion = em.emotionalDistribution(experiences)
        f.close()

    def updateConvo(self,texts): #Conversation used for testing
        '''
        Updates conversation based on input, and returns what Violet should say.

        In: texts: List[str]
        Out: output: str
        '''
        conversation = ("\n").join(texts)
        currConvo = self.parseConvo(conversation)
        v.convo = currConvo
        self.p1()
        v.output = v.generate_output()
        try:
            v.output.replace("Violet would say","")
        except:
            pass
        try:
            v.output.replace("Violet would say","")
        except:
            pass
        try:
            v.output.replace("\"","")
        except:
            pass
        return v.output
    def parseConvo(self,conversation):
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
    def main(self,c):
        convos = []
        for tuplet in c:
            convos.extend(tuplet)
        convos = [element for element in convos if element is not None]
        convos.insert(0,"Hi, I'm Violet. It's so nice to meet you today!")
        if (v.emotion is None):
            self.p2()
        return self.updateConvo(convos)
