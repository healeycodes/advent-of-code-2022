with open("1.txt") as f:
    contents = f.read().split("\n\n")
    ordered = sorted(
        [sum(map(lambda x: int(x), elf.split())) for elf in contents], reverse=True,
    )
    print(ordered[0])
    print(sum(ordered[:3]))
