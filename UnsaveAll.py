from Login import reddit
savedposts = list(reddit.user.me().saved(limit=None))
print(f"Listed {len(savedposts)} saved posts.")
for saved in savedposts:
	try:
		saved.unsave()
		saved.clear_vote()
	except ClientException as e:
		print(f"{saved.permalink} failed to unsave due to {str(e)}")