import pandas as pd

global assignment_final, game_names, team_names, game_times, df, game_rnd, game_and_score_string

game_rnd = 0
game_and_score_string = ''

assignment_final = [[2, 1, 0, 5, 4], [2, 0, 3, 5, 4], [3, 4, 2, 0, 1], [1, 2, 5, 3, 0], [4, 3, 5, 2, 1], [5, 4, 1, 3, 2], [5, 1, 4, 2, 3], [1, 5, 2, 4, 3], [4, 5, 3, 1, 2], [0, 3, 1, 4, 5], [3, 2, 4, 1, 5]]

team_names = ['USA', 'Venezuela', 'Netherlands', 'Afghanistan', 'Japan', 'Russian Olympic Committee', 'Iceland', 'Mexico', 'Germany', 'Jamaica', 'Scotland']

game_names = ['Ladder Golf','Flimsee','Molkky','First-N-Ten','Bucket Pong']

game_times = ['1:00 PM', '1:30 PM', '2:00 PM', '2:30 PM', '3:00 PM']


team_names_df = pd.DataFrame(team_names)
team_names_df.columns = ['team_names' for col_name in team_names_df.columns]

team_seeds = [i for i in range(1, len(team_names) + 1)]
team_seeds_df = pd.DataFrame(team_seeds)
team_seeds_df.columns = ['seed' for col_name in team_seeds_df.columns]

assignment_final_df = pd.DataFrame(assignment_final)
assignment_final_df.columns = ['round_' + str(col_name) for col_name in assignment_final_df.columns]

df = pd.concat([team_names_df, assignment_final_df,team_seeds_df], axis='columns')

if len(team_names) % 2:
    games = {0:['Bye']}
    games.update({i: [game_names[i-1]] for i in range(1, len(game_names) + 1)})
else:
    games = {i: [game_names[i-1]] for i in range(1, len(game_names) + 1)}

for i in range(len(game_names)):
    var_name = 'round_' + str(i)
    df2 = df[['team_names',var_name,'seed']]
    df = pd.merge(df,df2, how='inner', left_on=[var_name], right_on=[var_name], suffixes=["","2_" + var_name])
    keep_logic = df[var_name].eq(0) | df['team_names'].ne(df['team_names2_' + var_name])
    df = df[keep_logic]
    df[var_name] = df[var_name].replace(games)

df['score'] = ['0-5-10' for i in range(len(df))]
