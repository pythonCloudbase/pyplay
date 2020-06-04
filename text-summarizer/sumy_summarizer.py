from sumy.parsers.plaintext import PlaintextParser 
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer 

file = "henry.txt"
parser = PlaintextParser.from_file(file.encode("utf-8"), Tokenizer("english"))
summarizer_lsa = LsaSummarizer()

summary_2 = summarizer_lsa(parser.document,20)
# summarize with 5 sentences

f = open(file + "_output.txt", "a")


for sentence in summary_2:
    f.write(str(sentence))

f.close()



