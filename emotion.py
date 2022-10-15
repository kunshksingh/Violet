import os
import openai

class Emotion:
    def emotionalDistribution(self, characteristics):
        openai.api_key = os.getenv("OPENAI_API_KEY")

        emotion = openai.Completion.create(
            model="text-davinci-002",
            prompt="The following is a probability distribution of emotions experienced by a therapist in the past:\n\n{ \"compassionate\": 0.5, \"love\":0.5}\n\nConsider possibly adding a low degree of an extreme including, which may be one of fear, excitement, frustration, depression, ecstasy, or thrill, in hopes of improving the therapist's response to a patient. However, the therapist retains mostly a playful, bubbly, strong-willed, and youthful energy.  Always consider the probability distribution of emotions: compute the emotion that the therapist feels right now. Use complex verbiage and determine the concealed emotion of the therapist in thorough detail.",
            temperature=0.9,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0.15,
            presence_penalty=0.9
        )
        return str(emotion['choices'][0]['text'])
        #TODO Create another method that creates voice fluctuations based on emotion: includes breaths/softness in voice/inflections.