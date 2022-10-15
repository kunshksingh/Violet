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

import random
import numpy as np
import pandas as pd
import tensorflow as tf
import re
import os
import json
import pickle
import nltk


class Violet:
    def __init__(self, age, characteristics, experiences, emotion, gender, input):
        self.age = age
        self.characteristics = characteristics
        self.experiences = experiences
        self.emotion = emotion
        self.gender = gender
        self.input = input
        self.output = self.generate_output()

    def generate_output(self):
        prompt = "Violet is a 22-year old, female therapist who is the best at what she does. She seeks to be a friend to whoever"


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