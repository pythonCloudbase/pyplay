# getting the followers of the user who have atleast 1000 followers
# not working

import twint

c = twint.Config()
c.Username = "fanbyprinciple"
c.Store_object = True
c.User_full = True

# try:
#     twint.run.Followers(c)
# except Exception as e:
#     print(e)

# target_followers = twint.output.users_list
twint.run.Followers(c)

# # Dictionary of object
# print("Dictionary of output")
# for i in twint.output.__dict__:
#     print(i) 

# # print(twint.output.__dict__)

target_followers = twint.output.users_list

print("Target followers ")
print(target_followers)


K_followers = []

for user in target_followers:
    if user.followers >= 1000:
        K_followers.append(user)

# saving into a csv
with open('K_followers.csv', 'w') as output:
    output.write('id,username,followers,following\n')
    for u in K_followers:
        output.write('{},{},{},{}\n'.format(u.id, u.username, u.followers, u.following))