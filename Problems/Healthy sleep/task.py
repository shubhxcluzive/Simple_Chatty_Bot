
recommend_limit = int(input())
over_limit = int(input())
Ann_sleeps = int(input())

if over_limit >= Ann_sleeps >= recommend_limit:
    print("Normal")
else:
    if Ann_sleeps < recommend_limit:
        print("Deficiency")
    else:
        print("Excess")