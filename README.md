Twitch Crawler
=======
These scripts were created to pull data from the Twitch.tv video game-streaming website. On the main page, a list is displayed showing the 12 games with the most current viewers. This is the data pulled by Twitch Crawler.

Setup
------------
You must install the [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/) package for this program to work. Beautiful soup is a Python library for extracting data from HTML (or XML). It makes this project possible, as parsing HTML can be a nightmare. Seriously. To install, from the command line type:
```
easy_install beautifulsoup4
```
or
```
pip install beautifulsoup4
```
I personally use the pip package manager. To install [pip](https://pip.pypa.io/en/latest/index.html) or [easy_install](https://pypi.python.org/pypi/setuptools), see the appropriate documentation. 

How to Run the Script
-----
To begin pulling data from Twitch.tv, from the command line run: 

```
python3 crawler.py
```   
The script should run forever until manually killed.  So every ~30 seconds, a line of JSON should be added to a file called 'data.json'.

How to Convert JSON to CSV
------------------
The data is initially collected as a JSON file because you never know when new games make it to the top 12. So creating a CSV initially wouldn't make sense, as you'd have to constantly be appending lines, adding null values, etc. The next script finds all of the games that were in the top 12 while the program ran and creates a CSV output file. If you want to start analyzing while still crawling, you can take a "snapshot" of the data by typing
```
cp data.json Twitch_data_snapshot.json
```
You can then create a CSV from this JSON file by typing

```
python3 twitch_json_to_csv.py
```   


Now you can look at the data in R or Excel or whatever CSV-opening program you want! I added an R file to load the CSV file, change the factor values to integers, and create an absolute time based on the day,hour,minute,and second columns.

Optional: Restart program automatically
---------------------
I used a [Raspberry Pi](http://www.raspberrypi.org/) to run the script over a few days.  Occasionally it can stop by itself.  To automatically restart in Ubuntu (or variant thereof), you can download a utility called [UpStart](http://upstart.ubuntu.com/download.html). I created a file in /etc/init/ called pythonWebCrawler.conf and typed:
```
description "Python web crawler for Twitch.tv"

start on net-device-up
stop on shutdown

respawn

setuid [your_user_id]
chdir /home/[your_home_file] #wherever your scripts are
exec python3 crawler.py
```
To start the process, instead of executing the Python program from the command line, type:
```
sudo start pythonWebCrawler
```
