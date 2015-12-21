import time
import praw
import os
import re
import pdb

REDDIT_USERNAME = 'warwiki_bot' 
REDDIT_PASS = '4Ng+R=5km9T~qh!R' 

user_agent = ("Warframe Wiki Linker V0.1")
r = praw.Reddit(user_agent = user_agent)
r.login(REDDIT_USERNAME,REDDIT_PASS)

subreddit = r.get_subreddit("warframe")
subreddit_comments = subreddit.get_comments()
flat_comments = praw.helpers.flatten_tree(subreddit_comments)
already_done = set()

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        posts_replied_to = filter(None, posts_replied_to)



print(already_done)

bot_search = re.compile(r'.*{wfwiki:(.*)}.*')

for comment in flat_comments:
    search_result = re.search(bot_search,comment.body)
    if search_result != None and comment.id not in posts_replied_to:
        comment.reply("http://warframe.wikia.com/wiki/"+search_result.group(1))
        print("http://warframe.wikia.com/wiki/"+search_result.group(1))
        posts_replied_to.add(comment.id)
        print(comment)

with open("posts_replied_to.txt", "w") as f:
    for post_id in posts_replied_to:
        f.write(post_id + "\n")
