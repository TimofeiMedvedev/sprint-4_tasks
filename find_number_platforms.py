"""Документация для кода 115795162."""


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
        light_robot += 1
        counter += 1
        heavy_robot -= 1
        if weight_two_robots > limit_platform:
            light_robot -= 1
    return counter


if __name__ == '__main__':
    weight_robots = [int(x) for x in input().split()]
    limit_platform = int(input())
    print(find_number_platforms(weight_robots, limit_platform))
