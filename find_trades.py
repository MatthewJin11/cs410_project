import pandas as pd
import numpy as np
import argparse

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MinMaxScaler

current_nba_teams = ['ATL', 'BOS', 'BRK', 'CHI', 'CHO', 'CLE', 'DAL', 'DEN', 'DET', 'GSW', 'HOU', 'IND', 'LAC', 
                    'LAL', 'MEM', 'MIA', 'MIL', 'MIN', 'NOP', 'NYK', 'OKC', 'ORL', 'PHI', 'PHO', 'POR', 'SAC',
                    'SAS', 'TOR', 'UTA', 'WAS']

parser = argparse.ArgumentParser()
parser.add_argument('--player', type=str, required=True, help="Player you want to trade!")
parser.add_argument('--team', type=str, required=True, help="The abbreviation of the current team that player is on! Choose from the following: {}".format(current_nba_teams))
parser.add_argument('--k', type=int, default=5, help="How many trades do you want!")

args = parser.parse_args()

input_player = args.player
input_team = args.team
k = args.k

print("The player you want to trade is {}".format(input_player))

player_stats = pd.read_csv('stats.csv')
player_salaries = pd.read_csv('salaries.csv')

player_stats = player_stats.set_index('Player-additional')
player_salaries = player_salaries.set_index('Player-additional')

player_stats = player_stats.drop(['Rk'], axis=1)
player_salaries = player_salaries.drop(['Rk', 'Tm', 'Player', 'Guaranteed', '2023-24', '2024-25', '2025-26', '2026-27', '2027-28'], axis=1)

player_info = player_stats.join(player_salaries)

if not player_info[(player_info['Tm'] == input_team) & (player_info['Player'] == input_player)].empty:
    p_idx = player_info[(player_info['Tm'] == input_team) & (player_info['Player'] == input_player)].index.item()

    player_info.rename(columns={'2022-23': 'Salary'}, inplace=True)
    player_info['Salary'] = player_info['Salary'].apply(lambda row: int(row[1:]) if not pd.isna(row) else None)

    player_info = player_info[~player_info.index.duplicated(keep='first')]

    scaler = MinMaxScaler()

    player_info['Salary'] = scaler.fit_transform(np.array(player_info['Salary']).reshape(-1, 1))
    player_info['PTS'] = scaler.fit_transform(np.array(player_info['PTS']).reshape(-1, 1))
    player_info['AST'] = scaler.fit_transform(np.array(player_info['AST']).reshape(-1, 1))
    player_info['TRB'] = scaler.fit_transform(np.array(player_info['TRB']).reshape(-1, 1))
    player_info['STL'] = scaler.fit_transform(np.array(player_info['PTS']).reshape(-1, 1))
    player_info['BLK'] = scaler.fit_transform(np.array(player_info['AST']).reshape(-1, 1))
    player_info = player_info.fillna(0)

    ranked_list = cosine_similarity(np.array(player_info.loc[p_idx, ['Salary', 'PTS', 'AST', 'TRB', 'STL', 'BLK', 'eFG%', '3P%']]).reshape(1, -1), 
                                    np.array(player_info.loc[:, ['Salary', 'PTS', 'AST', 'TRB', 'STL', 'BLK', 'eFG%', '3P%']])).argsort()

    top_k = player_stats.iloc[ranked_list[0][-k - 1:-1][::-1], :]

    print("Top {} Suggested Trades:".format(k))

    [print(i + 1, player) for i, player in enumerate(list(top_k['Player']))]

else:
    print("Sadly, this player does not exist in my database... Could you check again the player's name and team?")