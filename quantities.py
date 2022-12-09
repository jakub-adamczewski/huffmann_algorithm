def get_x_chars_quantities(file, x):
    with open(file=file, mode="r") as f:
        all_x_chars_count = 0
        x_chars_counts = {}
        for line in f.readlines():
            for index, c in enumerate(line):
                if index < x - 1:
                    continue
                x_chars = line[index - x + 1: index + 1]
                all_x_chars_count += 1
                if x_chars in x_chars_counts:
                    x_chars_counts[x_chars] += 1
                else:
                    x_chars_counts[x_chars] = 1
    return x_chars_counts, all_x_chars_count
