import random

VOWELS = ['a','e','i','o','u']

verbfile = open("dictionary/verbs.txt")
VERB = []
for line in verbfile:
    VERB.append(line.strip())

nounfile = open("dictionary/nouns.txt")
NOUN = []
for i,line in enumerate(nounfile):
    NOUN.append(line.strip())

with open("dictionary/adverbs.txt") as adverbfile:
    ADVERB = [line.strip() for line in adverbfile]

with open("dictionary/adjectives.txt") as adjectivefile:
    ADJECTIVE = [line.strip() for line in adjectivefile]   

#conditional conjunctions
C_CONJ = ["and", "but", "for", "or", "so", "yet"] # Coordinating conjunctions

#determiners
DETERMINERS = ["the", "this", "that", "my", "your", "his", "her", "its", "our", "their", "one", "each", "every", "another"] #https://www.ef.com/ca/english-resources/english-grammar/determiners/

#prepositions
prep = "Above, about, across, against, along, among, around, at, Before, behind, below, beneath, beside, between, beyond, by, Down, during ,Except , For, from ,In, inside, into ,Like, Near ,Of, off, on,Since,To, toward, through,Under, until, up, upon,With, within"
prepositions = prep.split(",")
PREPOSITIONS = []
for i in prepositions:
    PREPOSITIONS.append(i.lower().strip())



##dictionary loaded

sentence = []

def createSentence():
    sentence.append(random.choice(DETERMINERS))
    if (random.random() < 0.5) :
        sentence.append(random.choice(ADJECTIVE))
    sentence.append(random.choice(NOUN))
    if(random.random() < 0.5):
        sentence.append(random.choice(ADVERB))

    # code for getting verb

    sentence.append(random.choice(VERB)+ "s")

    if(random.random()< 0.8):
        sentence.append(random.choice(PREPOSITIONS))
        sentence.append(random.choice(DETERMINERS))
        if(random.random() < 0.7):
            sentence.append(random.choice(ADJECTIVE))
        sentence.append(random.choice(NOUN))

    if(random.random() < 0.3):
        sentence.append(random.choice(C_CONJ))
        createSentence()



createSentence()
#print(sentence)

print((" ".join(sentence) + ".").capitalize())


# print(random.choice(NOUN), random.choice(ADVERB), random.choice(ADJECTIVE), random.choice(VERB))

# class Word(object):
#     def __init__(self,dict):
#         self.val = random.choice(dict)
    
#     def __repr__(self):
#         return str(self.val.strip())
    
# class Noun(Word):
#     def __init__(self):
#         super(Noun,self).__init__(NOUN)

# class Verb(Word):
#     def __init__(self):
#         super(Verb,self).__init__(VERB)

# class Adjective(Word):
#     def __init__(self):
#         super(Adjective, self).__init__(ADJECTIVE)

# class Adverb(Word):
#     def __init__(self):
#         super(Adverb, self).__init__(ADVERB)

