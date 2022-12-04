with open("4.txt") as f:
    pairs = map(
        lambda pair: map(
            lambda range: tuple(map(lambda num: int(num), range.split("-"))),
            pair.split(","),
        ),
        f.read().split("\n"),
    )

    containing_other = 0
    any_overlap = 0
    for pair in pairs:
        a, b = pair
        if a[0] >= b[0] and a[1] <= b[1] or b[0] >= a[0] and b[1] <= a[1]:
            containing_other += 1
        if b[0] <= a[1] and a[0] <= b[0] or a[0] <= b[1] and b[0] <= a[0]:
            any_overlap += 1
    print(containing_other)
    print(any_overlap)
