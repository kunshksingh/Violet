import openai
import os
from decouple import config
from Questions import *

class Answers:
    def davidHilbert(self,context, questions):
        '''
        Generates anticipated in response to question based on the following conversational context. 
        Answers will be used in the future to gather more insight about the person who Violet is conversing with.

        In: context: str, questions: str
        Out: answers: str
        '''
        openai.api_key = config("OPENAI_API_KEY")
        ansPrompt = "\n\nAnticipate how the patient will answer these 5 questions."
        ansPrompt2 = "\n\nAnticipate hidden reasons the patient may not discuss that they may hypothetically use to answer these 5 questions."
        ansPrompt3 = "\n\nCombine the two answers for each question to gain the most accurate insight on the patient. Add more detail to specifics and avoid repetition."
        ans = openai.Completion.create(
            model="text-davinci-002",
            prompt=context+questions+ansPrompt,
            temperature=0.1,
            max_tokens=300, 
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        preliminary = str(ans['choices'][0]['text'])
        ans2 = openai.Completion.create(
            model="text-davinci-002",
            prompt=context+questions+ansPrompt+preliminary+ansPrompt2,
            temperature=0.1,
            max_tokens=300, 
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        hidden  = str(ans2['choices'][0]['text'])

        ans3 = openai.Completion.create(
            model="text-davinci-002",
            prompt=context+questions+ansPrompt+preliminary+ansPrompt2+hidden+ansPrompt3,
            temperature=0.1,
            max_tokens=300, 
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        combined = str(ans3['choices'][0]['text'])
        return combined
'''
Test questios and answers based on patient input
'''
'''
qTest = Questions()
lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)
questions = Questions.socrates(text, str(text.split('P: '))[-1])
aTest = Answers()
print(aTest.davidHilbert(text, questions))
'''

