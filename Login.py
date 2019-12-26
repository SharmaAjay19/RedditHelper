import praw
username = "__username__"
pw = "__PASSWORD__"
client_id = "__CLIENTID__"
client_secret = "__CLIENTSECRET__"
reddit = praw.Reddit(client_id=client_id, client_secret=client_secret, user_agent='/u/'+username, username=username, password=pw)
