'''
Create a .py that generates an OpenAI model based on the following input data. The OpenAI model simulates a feeling human with different character traits and experiences.

Input:
- An approximate age value(int)
- A range of characteristics(List[str])
- A list of experiences(List[str])
- A probabilistic distribution of emotion(dict(str:int))
- Gender(str="Female")
- A conversational input provided by the user(str)

The goal is to create a text prompt as an output to respond to the conversational input, taking into all of the other input parameters based on importance and relevance to conversation provided by user. The OpenAI model is very empathetic, and will try to emotionally aid the user.

Output:
- A conversational output provided by the OpenAI model(str)
'''

#import random
#import numpy as np
#import pandas as pd
#import tensorflow as tf
#import re
#import os
#import json
#import pickle
#import nltk
from Questions import *
from Answers import *
from Experiences import *
from Emotion import *

class Violet:
    def __init__(self, convo, insight, characteristics, emotion, age="22", gender="female", pronoun="she",pronounP="her"):
        self.age = age #Age of therapist
        self.characteristics = characteristics #Character traits given by Characteristics.py TODO
        self.emotion = emotion #Current emotion given by Emotion.py
        self.gender = gender #Gender of therapist
        self.convo = convo #Conversation with user
        self.pronoun = pronoun #Base pronoun of therapist
        self.pronounP = pronounP #Possessive tense of pronoun of therapist
        self.insight = insight #Predictive answers to questions to anticipate how the patient feels
        self.output = self.generate_output()

    def generate_output(self):
        self.pronounC = self.pronoun[0].upper() + self.pronoun[1:]
        outputPrompt = "Violet is a "+self.age+"-year old, "+self.gender+" therapist who is the best at what"+self.pronoun+"does, and the bestest friend any one could dream of. "+self.pronounC+" is "+self.characteristics+". "+self.pronounC+" seeks to be a friend to everyone, as much as "+self.pronoun+" can without overstepping boundaries. "+self.pronounC+" is highly sentient and uses past experiences as well as the moment to generate a response to "+self.pronounP+" patient. The following best describes her current emotion:\n\n"+self.emotion+"\n\n Based on her current emotion and anticipated knowledge of the patient, "+self.pronoun+" must respond to the following conversation with "+self.pronounP+" patient:\n\n"+self.convo+"\n\nBased on what the patient has said, Violent thinks there is a slight chance of one or more of the following the patient:\n\n"+self.insight+"\n\nGiven the following, come up with the best response for Violet to say back to "+self.pronounP+" patient."
        #TODO Truncate conversation to only previous three user-inputted inquiries in order to conserve tokens/provide better answers in the moment and avoid repetition


'''
Sample, extremely short, version of violet

if __name__ == "__main__":
    age = 20
    characteristics = ["kind", "caring", "empathetic", "intelligent", "funny"]
    experiences = ["I have been through a lot of pain in my life.", "I have been through a lot of joy in my life.", "I have been through a lot of sadness in my life.", "I have been through a lot of anger in my life."]
    emotion = {"joy": 10, "sadness": 10, "anger": 10, "fear": 10, "disgust": 10}
    gender = "Female"
    input = "Hello, I am Violet. I am a chatbot that is here to help you."
    violet = Violet(age, characteristics, experiences, emotion, gender, input)
'''
