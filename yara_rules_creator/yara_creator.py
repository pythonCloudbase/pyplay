input_method = input("""Enter the method you want to provide input 
                        (1 : for text)
                        (2 : for manual input)
                        :> """)
if(input_method == 2):
    name = input("Enter the rule name")
    meta = input("enter meta description")
    strings = input("Enter the strings separated by space")
    condition = input("Enter the condition (Default OR)")

else:
    file1 =  open("yara_input.txt")
    all_lines = file1.readlines()
    name = all_lines[0]
    meta = all_lines[1]
    strings = all_lines[2]
    condition = all_lines[3]
    file1.close()

var_  = "$text"

if condition == "":
    condition = "$text"

if var_ == "":
    var_ = "$text"

print(name)

output_text = """
rule {}
""".format(name)

starting_text = "{"

inside_rule = """
    strings:
        {} = {}
    
    condition:
        {}
""".format(var_, strings, condition)

ending_text = "}"

print(output_text + starting_text + inside_rule + ending_text)