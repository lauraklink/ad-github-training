def likes(team: list) -> str:
    if len(team) > 2:
        print("Error: max 2 names allowed")
    elif len(team) == 1:
        print("{} likes this!".format(team[0]))
    elif len(team) == 2:
        print("{} and {} like this!".format(team[0], team[1]))
    else:
        print("no one likes this")

