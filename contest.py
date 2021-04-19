import pandas as pd

current_teams=['CSK','DC','KKR','MI','PBKS','RCB','RR','SRH']

team_players_dict={}

for team in current_teams:
    team_players_dict[team] =pd.DataFrame(pd.read_csv('./current-list/'+team+'.csv'))
    


for team in current_teams:
    print(team+' : '+str(team_players_dict[team].shape))
    # print(team_players_dict[team])
# print(csk_players.shape)
