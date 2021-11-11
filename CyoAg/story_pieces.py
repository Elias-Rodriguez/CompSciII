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
