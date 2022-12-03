with open("2.txt") as f:
    data = f.read().split()
    points = {"X": 1, "Y": 2, "Z": 3}
    beats = {"X": "C", "Y": "A", "Z": "B", "A": "Z", "B": "X", "C": "Y"}
    total = 0
    for i in range(0, len(data), 2):
        opponent = data[i]
        you = data[i + 1]
        if beats[you] == opponent:
            total += 6
        elif beats[opponent] == you:
            total += 0
        else:
            total += 3
        total += points[you]
    print(total)

    draws = {"X": "A", "Y": "B", "Z": "C", "A": "X", "B": "Y", "C": "Z"}
    loses = dict((v, k) for k, v in beats.items())
    total = 0
    for i in range(0, len(data), 2):
        opponent = data[i]
        outcome = data[i + 1]
        if outcome == "X":
            you = beats[opponent]
        elif outcome == "Y":
            you = draws[opponent]
        else:
            you = loses[opponent]

        if beats[you] == opponent:
            total += 6
        elif beats[opponent] == you:
            total += 0
        else:
            total += 3
        total += points[you]
    print(total)
