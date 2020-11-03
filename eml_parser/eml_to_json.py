import datetime
import json
import eml_parser


# { "class": "TreeModel",
#   "nodeDataArray": [ 
# {"key":0, "text":"NA\n", "loc":"0 0"},
# {"key":1, "parent":0, "text":"Getting more time", "brush":"skyblue", "dir":"right", "loc":"50 17.58166608810425"},
# {"key":11, "parent":1, "text":"Wake up early", "brush":"skyblue", "dir":"right", "loc":"189.6999969482422 -8.41833391189575"},
# {"key":12, "parent":1, "text":"Delegate", "brush":"skyblue", "dir":"right", "loc":"189.6999969482422 17.58166608810425"},
# {"key":13, "parent":1, "text":"Simplify", "brush":"skyblue", "dir":"right", "loc":"189.6999969482422 43.58166608810425"},
# {"key":3, "parent":0, "text":"Time wasting", "brush":"palevioletred", "dir":"left", "loc":"-20 17.58166608810425"},
# {"key":31, "parent":3, "text":"Too many meetings", "brush":"palevioletred", "dir":"left", "loc":"-126.51667022705078 -8.41833391189575"},
# {"key":32, "parent":3, "text":"Too much time spent on details", "brush":"palevioletred", "dir":"left", "loc":"-126.51667022705078 17.58166608810425"},
# {"key":33, "parent":3, "text":"Message fatigue", "brush":"palevioletred", "dir":"left", "loc":"-126.51667022705078 43.58166608810425"}
#  ]}


def convert_for_gojs(from_dict, to_dict):
  converted_json = '{ "class": "TreeModel",   "nodeDataArray": ['
  
  root = '{"key":0, "text":"NA ANKARA"},'

  converted_json += root

  counter = 1
  for from_key in from_dict.keys():

    substring = '{"key":' + str(counter) +', "parent":0, "text":"'
    substring += from_key
    substring += '", "brush":"palevioletred", "dir":"left"},'
    

    substring += '{"key":' + str(counter)+'1, "parent":' + str(counter) +', "text":"'
    substring += from_dict[from_key]
    substring += '", "brush":"darkseagreen", "dir":"left"},'

    converted_json += substring

    
    counter += 1

  for to_key in to_dict.keys():

    substring = '{"key":' + str(counter) +', "parent":0, "text":"'
 
    try:
      substring += to_key
    except:
      #print("could not be parsed: ", a)
      pass

    substring += '", "brush":"skyblue", "dir":"right"},'

    substring += '{"key":' + str(counter)+'1, "parent":' + str(counter) +', "text":"'
    substring += to_dict[to_key]
    substring += '", "brush":"coral", "dir":"left"},'
    
    converted_json += substring
    counter += 1


  
  converted_json += ']}'
  print(converted_json)


def convert_for_gojs_without_subject(from_dict, to_dict):
  converted_json = '{ "class": "TreeModel",   "nodeDataArray": ['
  
  root = '{"key":0, "text":"NA ANKARA"},'

  converted_json += root

  counter = 1
  for from_keys in from_dict.keys():

    substring = '{"key":' + str(counter) +', "parent":0, "text":"'
    substring += from_keys
    substring += '", "brush":"palevioletred", "dir":"left"},'
    
    converted_json += substring
    counter += 1

  for to_keys in to_dict.keys():

    substring = '{"key":' + str(counter) +', "parent":0, "text":"'
 
    try:
      substring += to_keys
    except:
      #print("could not be parsed: ", a)
      pass

    substring += '", "brush":"skyblue", "dir":"right"},'
    
    converted_json += substring
    counter += 1


  
  converted_json += ']}'
  print(converted_json)


from os import listdir
from os.path import isfile, join

# handling 'from' directory
frompath = './input_to_parser/from'
onlyfiles = [join(frompath, f) for f in listdir(frompath) if isfile(join(frompath, f))]

from_mails = []

for i in onlyfiles:
  with open(i, 'rb') as fhdl:
    from_mails.append(fhdl.read())


ep = eml_parser.EmlParser()

parsed_from_emls = []
for f in from_mails:
  parsed_from_emls.append(ep.decode_email_bytes(f))


# getting from addresses from the parsed mails
# and storing subjects in a dictionary format
from_dict = {}
for from_mail in parsed_from_emls:
  from_add = str(from_mail['header']['from'])
  subject = str(from_mail['header']['subject'].strip())

  if(from_add in from_dict.values()): 
    from_dict[from_add].append(subject)
  else:
    from_dict[from_add] = subject


# handling 'to' directory
topath = './input_to_parser/to'
onlyfiles = [join(topath, f) for f in listdir(topath) if isfile(join(topath, f))]

to_mails = []

for i in onlyfiles:
  with open(i, 'rb') as fhdl:
    to_mails.append(fhdl.read())


ep = eml_parser.EmlParser()

parsed_to_emls = []
for f in from_mails:
  parsed_to_emls.append(ep.decode_email_bytes(f))

# getting to addresses from the parsed mails
# and storing subjects in a dictionary format
to_dict = {}
for to_mail in parsed_to_emls:
  to_add = str(to_mail['header']['to'])
  subject = str(to_mail['header']['subject'].strip())

  if(to_add in to_dict.values()): 
    to_dict[to_add].append(subject)
  else:
    to_dict[to_add] = subject


# calling convert_to_js
convert_for_gojs(from_dict, to_dict)

