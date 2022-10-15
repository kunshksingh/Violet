import openai
import os
from decouple import config

class Questions:
    def socrates(context, currResponse):
        '''
        Generates questions in response to "currResponse" based on the following conversational context. 
        Questions will be used in the future to gather more insight about the person who said the currResponse.

        In: context: str, currResponse: str
        Out: questions: str
        '''
        openai.api_key = config("OPENAI_API_KEY")

        questions = openai.Completion.create(
            model="text-davinci-002",
            prompt="The following is context to a conversation between a therapist ('T') and a patient ('P')\n\n"+context+"\n\nThe patients last response was:"+currResponse+"\n\nGenerate five questions that may provide more insight to the therapist about the patient and the patient's emotions.",
            temperature=0.1,
            max_tokens=300, 
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return str(questions['choices'][0]['text'])

