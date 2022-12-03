from string import ascii_letters

with open("3.txt") as f:
    data = f.read().split("\n")
    letter_to_priority = {val: idx + 1 for idx, val in enumerate(ascii_letters)}

    part_one_priorities = 0
    for rucksack in data:
        duplicate_item = set(rucksack[: int(len(rucksack) / 2)]) & set(
            rucksack[int(len(rucksack) / 2) :]
        )
        part_one_priorities += letter_to_priority[next(iter(duplicate_item))]
    print(part_one_priorities)

    part_two_priorities = 0
    for i in range(0, len(data), 3):
        duplicate_item = set(data[i]) & set(data[i + 1]) & set(data[i + 2])
        part_two_priorities += letter_to_priority[next(iter(duplicate_item))]
    print(part_two_priorities)
