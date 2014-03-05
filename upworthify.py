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
broken = []
count = 0
test = api.GetHomeTimeline()
post = open("postfix.txt", "r")

# The loop takes the most recent tweet from @upworthify's timeline,  splits it into a list, then drops the last item (since they're all breaking news accounts that tend to end their tweets with links, this works 9/10 times)
# It then re-assembles the list as a sentence, drops the last space, and checks if there's punctuation to drop as well, before adding a suffix to the end.
# If the final assembled tweet is too big, or too small, the loop continues, and if it hasn't found something after ten tries, it quits.
while len(gotweet) == 0 or len(gotweet) > 140:
	current = test[count].text
	broken = current.split(" ")
	broken = broken[:-1]
	for word in broken:
		clean += word + " "
	clean = clean[:-1]
	if clean[len(clean) - 1] == "." or clean[len(clean) - 1] == "," or clean[len(clean) - 1] == ":":
		clean = clean[:-1]
	gotweet = clean.title() + random_line(post)
	count += 1
	if count > 10:
		break

# and this is where we send the final product to Twitter
api.PostUpdate(gotweet)

post.close()