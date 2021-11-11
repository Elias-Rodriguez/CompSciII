import pandas as pd

def greet_player():
    player_data = {}

    #dict_from_csv = pd.read_csv('player_file.csv', header=None, index_col=0, squeeze=True).to_dict()
    player_data = pd.read_csv('player_file.csv').to_dict()
    print(player_data)
    print('it is nice to meet you,', player_data['name'])


def no_connection(coin):
    print("\nNo connection found. Go explore the shuttle.")
    answer1 = input("\nYou are currently in the control room. Would you like to explore:\n"
                    "a.The room you are in.\n"
                    "b.The break room.\n"
                    "c.The engine room.\n"
                    "d.Put on space suit and explore the moon.\n")
    return answer1

def wake_up(coin):
    print("You wake up in a space shuttle on the moon with a month's worth oxygen and no fuel to go home.")
    print("a.Check coms to see if theres connection.\nb. Explore shuttle")
    answer = input("What would you like to do?")
    return answer
