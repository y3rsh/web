Title: Work Setup
Date: 2019-05-04 8:00
Modified: 2019-05-04 8:00
Category: Python, cron, crontab, brew
Tags: Python, fun, mic, headphones
Slug: setup
Authors: Josh McVey
Summary: Nice scripts and tools

I recently updated my local setup to include a [nice mic and some fabulous headphones.](https://www.amazon.com/hz/wishlist/ls/33G80B4QPE61K)  I totally recommend everything on the list.  Paired with my 2015 Macbook Pro my coworkers say I sound like I am on the radio in Zoom meetings.

**BUT** the headphones work almost too well at shutting out the world!  I used my Google home to alert me 1 minute before meetings.  When I am playing music I can't hear the Google home go off... at max volume....... half a meter away...........

#### [Cron with Crontab](https://opensource.com/article/17/11/how-use-cron-linux)

So I decided to play play an alert a few times _in_ the headphones, at least for recurring meetings.

```shell
crontab -e
```

Then I added this line

```
29 09 * * 1,2,3,4,5 for i in {1..4}; do afplay /path/to/alert_sound.mp3; done
```

Now every weekday at 9:29 AM I get an alert in my headphones and jump into standup.

I also added a couple other tasks to [crontab.](https://opensource.com/article/17/11/how-use-cron-linux)  I have a nice script to automatically install the latest chromedriver and I like to keep brew up to date.

- At 8:00 AM everyday, [if my machine is awake](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/ScheduledJobs.html) brew will upgrade.
- At 8:01 AM everyday, [if my machine is awake](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/ScheduledJobs.html) this couple of commands will navigate to a repo I have for scripts, pipenv run to use my dependencies, and run the script.

```
00 08 * * * brew upgrade
01 08 * * * cd /directory/where/you/put/the/file && pipenv run python ./getchromedriver.py
```

#### Here is the getchromedriver.py
<script src="https://gist.github.com/y3rsh/b55d5c8daaac7fb1632cc5a3380aec93.js"></script>
