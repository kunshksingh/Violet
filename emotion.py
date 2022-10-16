import os
import openai
from decouple import config

class Emotion:
    def emotionalDistribution(self, distribution):
        '''
        Uses a given emotional distribution to predict how Violet should feel(slightly) in her response to her patient.

        In: distribution: dict() str->int
        Out: detailed emotion: str
        '''
        openai.api_key = config("OPENAI_API_KEY")

        emotion = openai.Completion.create(
            model="text-davinci-002",
            prompt="The following is a probability distribution of emotions experienced by a therapist in the past:\n\n"+str(distribution)+"\n\nConsider possibly adding a low degree of an extreme emotion including, which may be one of fear, excitement, frustration, depression, ecstasy, or thrill, in hopes of improving the therapist's response to a patient. However, the therapist retains mostly a playful, bubbly, strong-willed, and youthful energy.  Always consider the probability distribution of emotions: compute the emotion that the therapist feels right now. Use complex verbiage and determine the regular and concealed emotion of the therapist in thorough detail.",
            temperature=0.9,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0.15,
            presence_penalty=0.9
        )
        return str(emotion['choices'][0]['text']).lstrip()
    #TODO Create another method that creates voice fluctuations based on emotion: includes breaths/softness in voice/inflections
    def voiceModulater(self):
        pass

