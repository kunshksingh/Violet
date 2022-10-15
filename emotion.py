import os
import openai

class Emotion:
    def emotionalDistribution(self, characteristics):
        openai.api_key = os.getenv("OPENAI_API_KEY")
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt="Normalize the following emotional probability distribution into a gaussian distribution centered around 1.\n\n",
            temperature=0,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )