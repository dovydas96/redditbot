import praw,os,re
reddit = praw.Reddit("bot1")

def main():
    if not os.path.isfile("posts_replied_to.txt"):
        posts_replied_to = []
    else:
        with open("posts_replied_to.txt","r") as f:
            posts_replied_to = f.read()
            posts_replied_to = posts_replied_to.split("\n")
            posts_replied_to = list(filter(None,posts_replied_to))

    subreddit = reddit.subreddit("dovydas")
    for sub in subreddit.hot(limit=5):
        if sub.id not in posts_replied_to:
            if re.search("Test",sub.title,re.IGNORECASE):
                sub.reply("Hello,This was an automated respose")
                print("bot replying to: ",sub.title)
                posts_replied_to.append(sub.id)

    with open("posts_replied_to.txt", "w") as f:
        for post_id in posts_replied_to:
            f.write(post_id + "\n")


if __name__ == '__main__':
    main()
