import pandas as pd

dat = pd.read_csv('baseball.csv')

temp = dat.loc[:, ['id','year','stint']].groupby(by=['id','year']).count()
temp = temp.rename(columns={'stint': 'teams'})
temp = temp.reset_index()
most_teams = temp.loc[temp['teams'] == temp['teams'].max(), 'id':'year']

print(most_teams)