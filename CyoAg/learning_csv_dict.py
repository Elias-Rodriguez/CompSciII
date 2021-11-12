import pandas as pd
coin = 42
# Help with dictionary
# https://www.programiz.com/python-programming/dictionary
player_data = {}
player_data['coin'] = coin
#print('your coin toss was:', player_data['coin'])
name = 'jeremy'
player_data['name'] = name

print('original dictionary:', player_data)

df = pd.DataFrame.from_dict(player_data, orient='index', columns = ['Value'])
df.to_csv (r'gen.csv', index=player_data.keys())

dt = pd.read_csv('gen.csv', index_col=1, skiprows=1).to_dict()
print('new dictionary is:')
print(dt)
print('name?', dt['name'])
