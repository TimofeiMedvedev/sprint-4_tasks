"""Документация для кода ID115803099."""


def find_number_platforms(
        weight_robots: list[int], limit_platform: int) -> int:
    """Обявляем функцию для подсчёта тележек."""
    sort_weight_robots = sorted(weight_robots)
    left_index: int = 0
    right_index: int = len(sort_weight_robots) - 1
    counter: int = 0
    while left_index <= right_index:
        weight_two_robots: int = sort_weight_robots[
            left_index] + sort_weight_robots[right_index]
        right_index -= 1
        counter += 1
        if weight_two_robots <= limit_platform:
            left_index += 1
    return counter

def main():
    with open("input.txt", "r") as file_in:
        weight_robots = [int(x) for x in file_in.readline().rstrip().split()]
        limit_platform = int(file_in.readline().rstrip())
    result = find_number_platforms(weight_robots, limit_platform)
    with open("output.txt", "w") as file_out:
        file_out.write(str(result))


if __name__ == '__main__':
    main()
