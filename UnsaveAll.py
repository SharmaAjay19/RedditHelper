from Login import reddit
savedposts = list(reddit.user.me().saved(limit=None))
print(f"Fetched {len(savedposts)} saved posts.")
while len(savedposts)>0:
	for saved in savedposts:
		try:
			saved.unsave()
			saved.clear_vote()
		except ClientException as e:
			print(f"{saved.permalink} failed to unsave due to {str(e)}")
	savedposts = list(reddit.user.me().saved(limit=None))
	print(f"Fetched {len(savedposts)} saved posts.")