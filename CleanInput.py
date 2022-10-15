import nltk
nltk.download('punkt')

from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

import string
class CleanInput:
    def clean(self, text):
        """
        Takes in a string of text, then performs the following:
        1. Remove all punctuation
        2. Remove all stopwords
        3. Returns a list of the cleaned text
        """
        nopunc = [char for char in text if char not in string.punctuation]
        nopunc = ''.join(nopunc)
        return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]

    def lemmatize(text):
        return WordNetLemmatizer().lemmatize(text)

    def stemming(text):
        return PorterStemmer().stem(text)
    def generateCleanInput(text:str, lemmatize=True, stemming=False):
        """
        Takes in a string of text, then performs the following:
        1. Tokenize the string
        2. Lemmatize the string (default is True)
        3. Stem the string (default is False)
        4. Join the tokens back into a string
        5. Return the cleaned text
        """
        if lemmatize:
            cleaned_text = [CleanInput.lemmatize(word) for word in word_tokenize(text.lower())]
        elif stemming:
            cleaned_text = [CleanInput.stemming(word) for word in word_tokenize(text.lower())]
        else:
            cleaned_text = CleanInput.clean(text)
        return ' '.join(cleaned_text)
