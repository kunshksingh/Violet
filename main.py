from Experiences import *
from Violet import *
from Questions import *
from Answers import *

exps = Experiences()
exps.violetExps(experiences=[], manualExperiences=[]) #TODO Update with actual experiences from John

#TODO Implement multithreading to sufficiently speed up Violet's runtime
v = Violet(input, characteristics, experiences, emotion, age="22", gender="female")
print(v.output)