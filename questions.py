import openai
import os

class Questions:
    def socrates(context, currResponse):
        '''
        Generates questions in response to "currResponse" based on the following conversational context. 
        Questions will be used in the future to gather more insight about the person who said the currResponse.

        In: context: str, currResponse: str
        Out: questions: List[str]
        '''
