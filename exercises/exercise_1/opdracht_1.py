def likes(team: list) -> str:
    if len(team) > 3:
        print("Error: max 2 names allowed")
    elif len(team) == 1:
        print("{} likes this!".format(team[0]))
    elif len(team) == 2:
        print("{} and {} like this!".format(team[0], team[1]))
    elif len(team) == 3:
        print("{}, {} and {} like this!".format(team[0], team[1], team[2]))
    else:
        print("no one likes this!!")

