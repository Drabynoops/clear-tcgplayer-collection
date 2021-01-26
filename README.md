# clear-tcgplayer-collection
A simple script to automate the emptying out of large tcgplayer.com collections.

Written using Python version 3.9.0 so you'll need to install that.
Might work using earlier versions, haven't tested.

Need the chromedriver for your particular version of Chrome

Required libraries:
Selenium

Variables:
chrome_driver_path - The location of the chromedriver file
TCGPLAYER_EMAIL - The email you use to log into tcgplayer.com
TCGPLAYER_PASSWORD = Your password
MAX_CLICK = the largest number for a card in your collection. Ex. I *supposedly* had 48 Obzedat's Aid, so I just set the number to 50, to be sure
SLEEP_TIME = The amount (in seconds) to wait for the page to load/accept input. Likes to lag especially on the log in screen

What is does:
Logs you in using the link that will bring you straight to your TCGPlayer collection tracker
Finds all the down arrows on that page and clicks each of them the number of times you specify

Note:
If you have multiple pages or something didn't load correctly, it won't completely empty out your collection that happened to me.

Potential improvements:
Grabbing the number of cards in each box and clicking only that many times or that many +1 (just to be sure)
In fact, probably going to do that after I eat.
