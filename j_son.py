import os
import json

teams_dict = {}

path_json = (r'C:\Users\Usec\Desktop\prog\json\Stats_version_1_seas_20_21.json')
with open(path_json, 'r') as file_read:

    data_dict = json.load(file_read)
    
for match in data_dict['matches']:
    home_teams_id_name = match['homeTeam']
    print(home_teams_id_name)
    away_teams_id_name = match['awayTeam']
    print(away_teams_id_name)
    if home_teams_id_name['id'] not in teams_dict.keys():
        teams_dict[home_teams_id_name['id']] = home_teams_id_name['name']
    if away_teams_id_name['id'] not in teams_dict.keys():
        teams_dict[away_teams_id_name['id']] = away_teams_id_name['name']


    # home_team = match['homeTeam']['name']
    
    # away_team = match['awayTeam']['name']
    
    # home_score = match['score']['fullTime']['homeTeam']

    # away_score = match['score']['fullTime']['awayTeam']

    # match_info = 'Команда Дома:{},Счет Домашей команды:{} === Команда Гостей:{},Счет Гостей:{}'.format(home_team,home_score,away_team,away_score)
    # print(match_info)

print(teams_dict)
print('x' * 100) 
print('x' * 35 , 'PROGRAM FINISH', 'x' * 49 )
print('x' * 100)

