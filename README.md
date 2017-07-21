# DownCloud

I created this because there is a ton of good music on some discreet subs (made this for /r/futurefunk initially) that have a lot of great music I don't know where to find anywhere else, and the threatening SoundCloud closure makes me want to archive all of it.

It needs 4 things:

[Python](https://www.python.org/downloads/)

[Praw (pip install praw)](https://praw.readthedocs.io/en/latest/)

[Youtube-dl (pip install youtube_dl)](https://rg3.github.io/youtube-dl/)

[Reddit API Key](https://github.com/reddit/reddit/wiki/OAuth2)


Usage:
```
python music.py subreddit_name

python music.py futurefunk
```

Details:

Searches through a subreddit for artist's SoundCloud links, then downloads all of the music from that artst's profile. First it finds the artist name and creates a directory for the music and dumps it in there. If a directory already exists for that artist, it is skipped.
