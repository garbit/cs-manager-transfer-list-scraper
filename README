# CS-Manager Transfer List Scraper
This tool allows you to download a .csv of all players currently listed on the transfer list on [https://cs-manager.com](https://cs-manager.com) in csv format. The script will look through all pages on the transfer list and create a .csv file containing the player information.

## Setup
Before you run this script you need to configure your ```.env``` file so that the script can log into your account.

### Configure .env
Make a copy of the ```.env.example``` and rename the file to ```.env```.

```
.env.example contains the following lines that need to be configured before you run this script
LANG=ENTER_EN_VALUE
LOGIN=ENTER_LOGIN_VALUE
PHPSESSID=ENTER_PHPSESSID_VALUE
PREFS=ENTER_PREFS_VALUE
SESSION_TEST=ENTER_SESSION_TEST_VALUE
SID=ENTER_SID_VALUE
```

You must first login to your account on [https://cs-manager.com](https://cs-manager.com) and retrieve your cookie information. 

Once you've logged into your account you need to find your cookie information. To do this, open the inspector (right click page > inspect element), head over to the 'network tab' and refresh the page. In the new list of network events look for the first GET request and click on the row. Now select the 'Cookies' tab to inspect the request. Add the cookie values to your ```.env``` file before you run the script.

### Install requirements
This tool runs using Python 3.x. Make sure you install the required packages before you run the script using:

```
pip install -r requirements.txt
```

## Run
To run the script just run:

```
python scrape.py
```

## Data
The script will create a ```.csv``` file under ```/data``` and contain the following fields:

```
name, age, birthday, salary, value, weapon, aim, teamplay, handling, playing_iq, quickness, determination, awareness, creativity, patience, calmness, total, leadership, experience, stamina, talent
Bob flemming, 19, 12, 1036, 49445, M4A4, 71, 27, 74, 19, 88, 71, 63, 28, 25, 33, 499, 0, 9, 3, 4
Joe Carson, 29, 35, 2182, 80409, Galil AR, 90, 80, 93, 56, 90, 95, 91, 79, 81, 77, 832, 0, 15, 1, 3
```

