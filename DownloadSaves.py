import requests,re
from Login import reddit

savedposts = list(reddit.user.me().saved(limit=None))
print(f"Fetched {len(savedposts)} saved posts.")
while len(savedposts)>0:
	for saved in savedposts:
		try:
			url = saved.url
			file_name = url.split("/")
			if len(file_name) == 0:
				file_name = re.findall("/(.*?)", url)
			file_name = file_name[-1]
			if "." not in file_name:
				print(f"Skipping {url} as it does not have a file name")
				continue
			res = requests.get(url)
			with open(f"{file_name}","wb") as f:
				f.write(res.content)
		except ClientException as e:
			print(f"Failed to download {url} due to {str(e)}")
	savedposts = list(reddit.user.me().saved(limit=None))
	print(f"Fetched {len(savedposts)} saved posts.")