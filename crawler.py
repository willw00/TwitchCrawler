import urllib.request as request
from bs4 import BeautifulSoup as bs 
import re, time, json


base_url = "http://www.twitch.tv"

def htmlByte2String(url):
		response = request.urlopen(url)
		codec = response.info().get_param('charset', 'utf8')
		return response.read().decode(codec)

def parseViewers():

	current_page = htmlByte2String(base_url)
	parsed_page = bs(current_page)
	game_links = parsed_page.body.find_all("div", class_="meta")


	local_time = time.localtime()
	yr = local_time[0]
	mon = local_time[1]
	day = local_time[2]
	hr = local_time[3]
	mn = local_time[4]
	sec = local_time[5]

	viewer_data = {
		'year': yr,
		'month': mon,
		'day': day,
		'hour': hr,
		'minute': mn,
		'second': sec
	}
	viewer_data.setdefault('games', {})

	watching_top_games = 0
	for game in game_links:
		title = game.contents[1].text
		viewer_string = game.contents[3].text
		viewers = viewer_string.split()[0].replace(',', '')
		viewer_data['games'].setdefault(title, [])
		viewer_data['games'][title] = viewers
		watching_top_games += int(viewers)

	
	viewer_data['top_viewers'] = watching_top_games

	with open('data.json', 'a') as f:
		json.dump(viewer_data, f)
		f.write('\n')

	#print(str(mon)+"/"+str(day)+"/"+str(yr)+" "+str(hr)+":"+str(mn)+":"+str(sec))
	#print(str(watching_top_games) + " watching the top " + str(len(game_links)) + " games.")

if __name__ == "__main__":
	while 1:
		parseViewers()
		time.sleep(5)