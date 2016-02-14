import praw
import time

r = praw.Reddit(user_agent = "TutorialBot by ripDig /u/Def_Correct")
# r.login with no arguments will prompt the user to login
print("Logging in...")
r.login("misc_bot", "989898")

words_to_match = ["definately", "definatly", "definantly", "definetly", "definently", "defiantly"]
cache = []

def run_bot():
    print("Grabbing subreddit...")
    # The arguments of the r.get_subrredit will be the sub we want to work with
    subreddit = r.get_subreddit("test")
    print("Grabbing comments...")
    comments = subreddit.get_comments(limit = 25)
    for comment in comments:
        comment_text = comment.body.lower()
        isMatch = any(string in comment_text for string in words_to_match)
        if isMatch and comment.id not in cache:
            print("Match found! Comment ID: " + comment.id)
            comment.reply('I think you meant to say "definitely."')
            print("Reply succesful!")
            cache.append(comment.id)
    print("Comments loop finished, time to sleep")
            
while True:
    run_bot()
    time.sleep(10)