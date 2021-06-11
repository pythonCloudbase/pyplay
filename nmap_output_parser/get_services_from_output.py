input_file = open('os_new_output.txt', 'r+').readlines()

services = []
for i in input_file:
    i = i.strip()
    try:
        if(i[0].isnumeric()):
            service = i.split(" ")[-1]

            if(service not in services):
                services.append(service)

    except:
        pass 

# print(services)

