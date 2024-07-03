"""Документация для кода ID115760654."""


def find_number_platforms(
        weight_robots: list[int], limit_platform: int) -> int:
    """Обявляем функцию для подсчёта тележек."""
    sort_weight_robots = sorted(weight_robots)
    light_robot: int = 0
    heavy_robot: int = len(sort_weight_robots) - 1
    counter: int = 0
    while light_robot <= heavy_robot:
        weight_two_robots: int = sort_weight_robots[
            light_robot] + sort_weight_robots[heavy_robot]
        if weight_two_robots <= limit_platform:
            counter += 1
            light_robot += 1
            heavy_robot -= 1
        else:
            counter += 1
            heavy_robot -= 1
    return counter


# weight_robots = [int(x) for x in input().split()]
# limit_platform = int(input())
# weight_robots = [1, 2]
# limit_platform = 3
weight_robots = [3, 5, 3, 4]
# limit_platform = 5weight_robots = [50, 50, 50, 50]
limit_platform = 5
if __name__ == '__main__':
    print(find_number_platforms(weight_robots, limit_platform))
