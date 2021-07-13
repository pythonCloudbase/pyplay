
import requests as r
from bs4 import BeautifulSoup as bs
import argparse as ap


req = r.get(url, verify=True)

html = req.text

# print(html)

soup = bs(html, 'html.parser')

for script in soup(["script", "style"]):
    script.decompose()

text = soup.get_text()

words = []

wordcount = 0

# print(text)
minlen = 4

def findtags(tag_prefix, tagged_text):
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].most_common(10)) for tag in cfd.conditions())

for word in text.split():
    if (len(word) >= minlen):
        try:
            words.append(str(word.strip('.,:!;"?@#$%&*()')))
            wordcount += 1
        except:
            pass

all_words_small = [x.lower() for x in list((set(words)))]
all_words = [x for x in list((set(words)))]


import nltk
nltk.download('averaged_perceptron_tagger')
# nltk.download('tagsets')

post_tag_array = nltk.tag.pos_tag(all_words_small)


# NNP and NNPS are the targets
unique_tag = []
for i, j in (post_tag_array):
    if (j not in unique_tag):
        unique_tag.append(j)
# print(unique_tag)

proper_words = []

blacklist = ["NNS", "NN", "VBP", "VBN", "RB", "PRP$", "PRP", "VBG"]
for (x,y),z in zip(post_tag_array, all_words):
    if (y not in blacklist):
        
        proper_words.append(z)
        
        if ("-" in z):
            for i in z.split("-"):
                if(i.isalpha() and len(i)>2  ):
                    proper_words.append(i)
            
        

# print(proper_words)


# print(nltk.help.upenn_tagset())

f = open("bahria_office.txt", "w+",  encoding="utf-8")
f.write("\n".join(proper_words))