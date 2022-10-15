from CleanInput import *
from dotenv import load_dotenv

from decouple import config
import openai
import collections


class Experiences:
    probDict = None
    def violetExps(self,experiences, manualExperiences):
        '''
        Generates keywords based on a list of experiences, both personally and client generated (Client generated not currently implemented).
        Returns probability distribution of keywords over P(S) = 1.

        In: Experiences: List[str], manualExperiences:List[str]
        Out: probabilityDistribution: dict(), str->float
        '''
        openai.api_key = config("OPENAI_API_KEY")
        experiences.extend(manualExperiences)

        #Input Handling
        experienceStr = "A young and caring female therapist may have had the experience of working with a young girl who was sexually abused. The therapist may have helped the girl to feel safe and to talk about her experiences. The therapist may have also helped the girl to understand her feelings and to make a plan to heal."
        experiences.append(experienceStr)
        cleaner = CleanInput()
        words = []
        #Generate Keywords from each experience; parse into a list
        for experience in experiences:

            #Wrap experience in quotation marks"
            experience = "\""+experience+"\""

            start_sequence = "Traits:"

            keywords = openai.Completion.create(
                model="text-curie-001",
                prompt="Use the following experience to generate 10 character traits about Violet. \n\n\"I remember feeling powerless and alone as a child. I often felt like I didn't have anyone to turn to for help or support. I felt like I had to be perfect and always do everything right in order to be loved and accepted. I often felt like I was walking on eggshells, never sure when I would make a mistake and be rejected or ridiculed. I felt like I constantly had to prove myself and my worth. I often felt invisible and unimportant. I felt like my needs and feelings didn't matter. I felt like I was always trying to please others and put their needs before my own.\"\n\nTraits: powerful, alone, flawed, loved, accepted, rejected, ridiculed, visible, important, needy, feelings, people-pleasing\n\n"+experience+"\n\n",
                temperature=0,
                max_tokens=128,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                stop=["\n"],
                #best_of = 2 Too expensive
            )
            topKeywords = str(keywords['choices'][0]['text'])

            keywords2 = openai.Completion.create(
                model="text-babbage-001",
                prompt="Add more character traits relevant to the character traits below.\n\n"+topKeywords,
                temperature=0,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )
            topKeywords2 = str(topKeywords+keywords2['choices'][0]['text'])
            print(topKeywords2)
            #start_sequence = "Traits:"

            keywordsTrimmed = openai.Completion.create(
                model="text-davinci-002",
                prompt="Get rid of all character traits that do not belong. Condense all traits into a word each.\n\n"+topKeywords+"\n\n",
                temperature=0,
                max_tokens=64,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                #stop=["\n"]
            )
            topTrimmedKeywords = str(keywordsTrimmed['choices'][0]['text'])
            words.extend(cleaner.clean(topTrimmedKeywords))

        #Make simple probability distribution
        self.probDict = dict(collections.Counter(words))
        for prob in self.probDict:
            self.probDict[prob] = float(self.probDict[prob])/len(self.probDict)
        return self.probDict

    def keywords(self):
        return self.probDict

        #EXAMPLE EXPERIENCE IN TOKENS IN ORDER TO GET PROBABILITY DISTRIBUTION OF WORDS
        #experienceStr = "A young and caring female therapist may have had the experience of working with a young girl who was sexually abused. The therapist may have helped the girl to feel safe and to talk about her experiences. The therapist may have also helped the girl to understand her feelings and to make a plan to heal."
        #print(CleanInput.generateCleanInput(experienceStr))
#exps = Experiences()
#exps.violetExps(experiences=[], manualExperiences=[])