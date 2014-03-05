# I think this is everything I need
import ConfigParser
import getopt
import os
import sys
import twitter
import random

# Logging in to the Twitter API. Fill in with actual info.
api = twitter.Api(consumer_key='API key',
					       consumer_secret='API secret',
					       access_token_key='Access token',
					       access_token_secret='Access secret')

# Function to choose a random line from the pre/postfix file.
def random_line(afile):
	line = next(afile)
	for num, aline in enumerate(afile):
		if random.randrange(num + 2): continue
		line = aline
	return line

# Setting up variables for loop.
current = ""
gotweet = ""
clean = ""
count = 0
# pulling the tweet from CNN Breaking
test = api.GetUserTimeline("428333")
post = open("postfix.txt", "r")

# This loop takes the most recent tweet from CNN, slices out the HTML and sees if it's too long for our purposes. If it is, it goes to the next one, otherwise it adds a post-fix to the end.
while gotweet == "":
	current = test[count].text
	clean = current[:-23:]
	if len(clean) < 85:
		gotweet = clean.title() + random_line(post)
	else:
		count += 1

print gotweet

# Where the magic happens
api.PostUpdate(gotweet)

post.close()