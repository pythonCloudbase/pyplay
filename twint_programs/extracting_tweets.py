import twint

file1 = open("followers_jm.txt", "r")
follower_list = file1.readlines()

for f in follower_list:
    try:
        print("working for : ", f)
        c = twint.Config()
        c.Username = f.strip()
        #c.Search = "http"

        c.Retweets = True
        c.Limit = 100

        c.Since = '2020-11-30'
        c.Until = '2020-12-01'
        c.Store_csv = True
        c.Output =  f + "_file"
        # c.Format = "Tweet id: {id} | Date: {date} | Time: {time} | Tweet: {tweet} "

        twint.run.Search(c)
    except Exception as e:
        print(e)



