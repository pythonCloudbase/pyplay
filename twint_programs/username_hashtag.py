import twint

c = twint.Config()

c.Username = "iamoperand"
#c.Search = "#hacktoberfest"

twint.run.Search(c)