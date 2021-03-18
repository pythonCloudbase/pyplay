# -*- coding: utf-8 -*-
 
# Used to create regular expressions
import re
 
def remove_pdf_links(file_input, file_output):
    """ A Simplistic Python function to remove all links from a pdf file
    """
 
    # Open the pdf file in binary mode and extract contents
    f = open(file_input, mode='rb')
    data = f.read()
    f.close()

    # print(data)

    # PDF encode URL info as /URI(<<URL PATH>>) so we need a
    # regex to extract this information
    regexstring = "\\/URI \\((.*)\\)"
 
    # Compile string as regex
    regexcompiled = re.compile(regexstring, re.MULTILINE)
 
    # Make a copy of the pdf content for the output pdf file
    output = data
    
    # converting byte data into utf-8
    # data = data.decode('ISO-8859-1').strip()

    data = data.decode('ISO-8859-1')
    # print(data)

    f = open("new.txt", "w", encoding='ISO-8859-1')
    f.write(data)

    # Process the pdf contents
    # items = regexcompiled.finditer(data)
    
    # print(items)
    # # For each regex match
    # for match in items:
    #     # We have two options here, either replaces the PDF URL with a URL of the same size 
    #     # Like So:
    #     ## output = output.replace(match.group(1), ' ' * len(match.group(1)), 1)
    #     # Or replace the whole command with spaces to remove the URL
    #     # Like So:
    #     ## output = output.replace(match.group(0), ' ' * len(match.group(0)), 1)
    #     #
    #     # Experimentation shows that we should leave the ( ) in the encoded format
    #     # when we remove the /URI command, so the first option is the best approach
    #     output = output.replace(match.group(1), ' ' * len(match.group(1)), 1)
 
    # # Because replacing the URL with spaces still leaves the link clickable and
    # # opens a blank webpage in the local browser. We need to replace the 
    # # preceding /URL command to remove the clickable aspect.
    # # Note Experimentation shows that the pdf will crash if the () is not within
    # # pdf /Link tag, so ensure that it is above
    # # Replace might work for this task, but regex was handy so i used it
    # # regex to extract this information
    # regexstring = "\\/URI"
 
    # # Compile string as regex
    # regexcompiled = re.compile(regexstring, re.MULTILINE)
 
    # # Process the pdf contents
    # items = regexcompiled.finditer(data)
 
    # # For each regex match
    # for match in items:
    #     # Replace the /URI tag with spaces
    #     output = output.replace(match.group(0), ' ' * len(match.group(0)), 1)
 
    # # Save the modified pdf file as a binary file   
    # f = open(file_output, mode='wb')
    # f.write(output)
    # f.close()
 
 
 
# This is our application entry point
if __name__ == "__main__":
    # We could easy extract console argument and pass this information 
    # into the remove function, but I will leave that task to your discretion
    my_input = "./demo.pdf"
    my_output = "./Demo_PDF-NL.pdf"
    # remove html links and save pdf
    remove_pdf_links(my_input, my_output)