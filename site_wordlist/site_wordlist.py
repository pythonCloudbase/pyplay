
import requests as r
from bs4 import BeautifulSoup as bs
import argparse as ap

# url = "https://www.nadra.gov.pk/?__cf_chl_jschl_tk__=e17ee01c3e1c4ba36ed9b44e3764ba861fe7a61c-1623383234-0-AUfe73hDRG-fLoC0hHYwI1otBKxHKEOUpe2O7TlA1jw765tynkm_EmC9Ye7BrJhAw9gDUQiAerIzotBgUNuyeangI2DxXSdKaydoo2JLlYN699O6SPIPFm82fbs7uIeP5pMxsD6xeo9D4oCN6N4umdAPNHER4l6d8eAygpF4vLUz9F3oan-gfd8W3Gxt7npLLSVWfiFSo4OisI643uGNlbTNUtcbRgIaiaib8ROaV-1Q3zxUS-lit3TvXQPogoWUPLwXwttYKrBdn-GRkipkfhdGRsl-u31Rf6w_LleyLqKFdmq-bd0PiDONOppv7UW8ENzSmhT9YBNS4YaH3XbvQhTtpIg05x9A_JqQFR2kQck8rf4PDz7yEx5gwyTsFkgEqKC9brJg8sCcSAuZMr6ifEY"
url = "https://www.paknavy.gov.pk/"
url = "https://www.bahria.edu.pk/office-directory/"
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