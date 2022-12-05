import re


with open("5.txt") as f:
    state, instructions = f.read().split("\n\n")
    total_stacks = int(state.split("\n")[-1].split()[-1])
    cratemover9000 = [[] for _ in range(total_stacks)]
    cratemover9001 = [[] for _ in range(total_stacks)]

    for line in reversed(state.split("\n")):
        for idx, char in enumerate(line):
            if re.match(r"[A-Z]", char):
                cratemover9000[idx // 4].append(char)
                cratemover9001[idx // 4].append(char)

    for instr in instructions.split("\n"):
        count, source, dest = list(map(lambda x: int(x), re.findall(r"\d+", instr)))
        moved_crates = []
        for _ in range(count):
            moved_crates.append(cratemover9001[source - 1].pop())
            cratemover9000[dest - 1].append(cratemover9000[source - 1].pop())
        cratemover9001[dest - 1].extend(reversed(moved_crates))

    print("".join(map(lambda x: x[-1], cratemover9000)))
    print("".join(map(lambda x: x[-1], cratemover9001)))

