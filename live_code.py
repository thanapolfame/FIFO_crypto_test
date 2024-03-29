"""
problem:
intersect time

result:

process:

"""

list_input = [
    (3, 7),
    (4, 9),
    (12, 14),
    (4, 5)
]


def main():
    list_new = []

    for pair in list_input:
        list_new.append([pair[0], "start"])
        list_new.append([pair[1], "end"])

    print(list_new)
    list_new.sort(key=lambda x: x[0])
    print(list_new)

    list_result = []
    n = 0
    for order, value in enumerate(list_new):
        current_value = value[0]
        value_type = value[1]
        # print(f"order: {order}")
        # print(f"value: {value}")

        if order != 0 and n > 0:
            previous_value = list_new[order - 1][0]
            # print(f"pre-value: {previous_value}")
            if current_value != previous_value:
                list_result.append([previous_value, current_value, n])

        if value_type == "start":
            n += 1
        elif value_type == "end":
            n -= 1
        # print(f"n: {n}")

        # print(f"result: {list_result}")

    return list_result


if __name__ == "__main__":
    """
    3 4 5 6 7 8 9 10 11 12 13 14
    x x x x x
      x x x x x x 
                         x x x
      x x                        
    list_input = [
    (3, 7),
    (4, 9),
    (12, 14),
    (4, 5)
    ]
    output = [
    [3, 4, 1],
    [4, 5, 3],
    [5, 7, 2],
    [7, 9, 1],
    [12, 14, 1]
    ]
    """
    print(main())
