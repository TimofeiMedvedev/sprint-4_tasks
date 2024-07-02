"""Документация для кода ID115760654."""


def find_number_platforms(
        weight_robots: list[int], limit_platform: int) -> int:
    """Обявляем функцию для подсчёта тележек."""
    list.sort(weight_robots)
    left_pointer: int = 0
    right_pointer: int = len(weight_robots) - 1
    counter: int = 0
    while left_pointer <= right_pointer:
        s: int = weight_robots[left_pointer] + weight_robots[right_pointer]
        if s <= limit_platform:
            counter += 1
            left_pointer += 1
            right_pointer -= 1
        if s > limit_platform:
            counter += 1
            right_pointer -= 1
    return counter


weight_robots = [int(x) for x in input().split()]
limit_platform = int(input())
# weight_robots = [1, 2]
# limit_platform = 3
# weight_robots = [3, 5, 3, 4]
# limit_platform = 5
# weight_robots = [50, 50, 50, 50]
# limit_platform = 100
if __name__ == '__main__':
    print(find_number_platforms(weight_robots, limit_platform))
