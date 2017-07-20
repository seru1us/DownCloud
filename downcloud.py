import os
import praw
import subprocess
import sys

reddit = praw.Reddit(client_id='YOUR_CLIENT ID',
                     client_secret='YOUR_SECRET',
                     password='YOUR_PASS',
                     user_agent='/u/will_work_for_twerk is a sexy b',
                     username='YOUR_USER')

subarg = reddit.subreddit(sys.argv[1])

slash = "/"

for submission in reddit.subreddit(str(subarg)).search('site:soundcloud.com', limit=None):
    dalink = slash.join(submission.url.split(slash)[:4])
    print(dalink)

    try:
        directory = submission.secure_media['oembed']['author_name']
    except Exception:
        directory = dalink.split(slash)[-1]

    odirectory = directory.strip() + '/%(title)s.%(ext)s'

    if not os.path.exists(directory):
        os.makedirs(directory)
        subprocess.call(['/usr/local/bin/youtube-dl', '-o', odirectory,  dalink])
    else:
        print('Artist ' + directory + ' already exists, skipping...')
