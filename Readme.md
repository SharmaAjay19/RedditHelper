First, make sure to install requirements using pip install -r requirements.txt

First steps:
1. Create a reddit app by going to this url. https://www.reddit.com/prefs/apps . Preferred app type is script-app.
2. Put in your username, password, client_id, client_secret (client credentials of the created app) in file Login.py

To Unsave all saved posts on your account:
Run UnsaveAll.py to unsave your saved posts. It will fetch saved posts in batches of 100 and sequentially unsave them.

To download images from all saved posts:
Run DownloadSaves.py.
