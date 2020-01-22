verbfile = open("dictionary/verbs.txt")

import random

VERB = []
for line in verbfile:
    VERB.append(line.strip())

#print(VERB)

# NOUNS = []
# with open("dictionary/nouns.txt") as nounfile:
#     NOUNS = [line.strip() for line in nounfile]

nounfile = open("dictionary/nouns.txt")
NOUN = []
for i,line in enumerate(nounfile):
    NOUN.append(line.strip())

with open("dictionary/adverbs.txt") as adverbfile:
    ADVERB = [line.strip() for line in adverbfile]

with open("dictionary/adjectives.txt") as adjectivefile:
    ADJECTIVE = [line.strip() for line in adjectivefile]   


# print(ADVERB, ADJECTIVE)

##dictionary loaded



print(random.choice(NOUN), random.choice(ADVERB), random.choice(ADJECTIVE), random.choice(VERB))

class Word(object):
    def __init__(self,dict):
        self.val = random.choice(dict)
    
    def __repr__(self):
        return str(self.val.strip())
    
class Noun(Word):
    def __init__(self):
        super(Noun,self).__init__(NOUN)

class Verb(Word):
    def __init__(self):
        super(Verb,self).__init__(VERB)

class Adjective(Word):
    def __init__(self):
        super(Adjective, self).__init__(ADJECTIVE)

class Adverb(Word):
    def __init__(self):
        super(Adverb, self).__init__(ADVERB)

