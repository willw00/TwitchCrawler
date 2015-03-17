import operator
import json
import csv

file_name = "Twitch_data_snapshot.json"
csv_file = open("Twitch_snapshot.csv", 'wb')

game_list = {}

for line in open(file_name):
	line_json = json.loads(line)
	for game in line_json["games"]:
		game_list.setdefault(game, 0)
		game_list[game] += 1

first_line = "Year,Month,Day,Hour,Minute,Second,Top Viewers,"
games = list(game_list.keys())
for game in games:
	first_line += str(game)
	if games[-1] != game:
		first_line += ","

with open("Twitch_snapshot.csv", 'a') as f:
	f.write(first_line +"\n")

	for line in open(file_name):
		line_json = json.loads(line)
		year = str(line_json["year"])
		month = str(line_json["month"])
		day = str(line_json["day"])
		hour = str(line_json["hour"])
		minute = str(line_json["minute"])
		second = str(line_json["second"])
		top_viewers = str(line_json["top_viewers"])
		data = [year,month,day,hour,minute,second,top_viewers]
		for game in games:
			data.append(str(line_json["games"].get(game)))

		data_line = ",".join(data)
		f.write(data_line+"\n")

sorted_list = sorted(game_list.items(), key=operator.itemgetter(1), reverse=True)

print("Number of times in top 12:")
for game in sorted_list:
	print(str(game[0]) + ": " + str(game[1]))


