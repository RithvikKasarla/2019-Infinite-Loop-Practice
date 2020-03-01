from typing import NamedTuple, List, Optional, Union, Tuple


class Point(NamedTuple):
    """Represents an (x, y) coordinate"""

    x: float
    y: float


class Line(NamedTuple):
    """Represents a line in y = mx + b form"""

    slope: Union[float, str]
    y_intercept: float


def points_to_line(point_one: Point, point_two: Point) -> Line:
    if point_one.x == point_two.x:
        return Line("undefined", point_one.x)  # Return x coordinate of vertical line

    slope = (point_two.y - point_one.y) / (point_two.x - point_one.x)
    y_intercept = point_two.y - slope * point_two.x

    return Line(slope, y_intercept)


def get_intersection(line_of_sight: Line, wall: Line) -> Optional[Point]:
    if isinstance(line_of_sight.slope, str):
        if isinstance(wall.slope, str):
            # Parallel vertical lines
            return None

        intersection_y = wall.slope * line_of_sight.y_intercept + wall.y_intercept
        return Point(line_of_sight.y_intercept, intersection_y)

    if isinstance(wall.slope, str):
        intersection_y = (
            line_of_sight.slope * wall.y_intercept + line_of_sight.y_intercept
        )
        return Point(wall.y_intercept, intersection_y)

    if line_of_sight.slope == wall.slope:
        # Parallel lines
        return None

    intersection_x = (wall.y_intercept - line_of_sight.y_intercept) / (
        line_of_sight.slope - wall.slope
    )
    intersection_y = line_of_sight.slope * intersection_x + line_of_sight.y_intercept
    return Point(intersection_x, intersection_y)


def intersection_within_bounds(
    intersection: Point,
    line_of_sight_start: Point,
    line_of_sight_end: Point,
    wall_start: Point,
    wall_end: Point,
) -> bool:
    return (
        min(line_of_sight_start.x, line_of_sight_end.x)
        <= intersection.x
        <= max(line_of_sight_start.x, line_of_sight_end.x)
        and min(line_of_sight_start.y, line_of_sight_end.y)
        <= intersection.y
        <= max(line_of_sight_start.y, line_of_sight_end.y)
        and min(wall_start.x, wall_end.x)
        <= intersection.x
        <= max(wall_start.x, wall_end.x)
        and min(wall_start.y, wall_end.y)
        <= intersection.y
        <= max(wall_start.y, wall_end.y)
    )


def main():
    test_cases = int(input())

    for _ in range(test_cases):
        x_spy, y_spy, x_camera, y_camera, num_walls = map(int, input().split())

        line_of_sight = points_to_line(Point(x_spy, y_spy), Point(x_camera, y_camera))

        walls: List[Tuple[Line, Point, Point]] = []
        for _ in range(num_walls):
            x_start, y_start, x_end, y_end = map(int, input().split())
            wall_start = Point(x_start, y_start)
            wall_end = Point(x_end, y_end)
            walls.append((points_to_line(wall_start, wall_end), wall_start, wall_end))

        found_intersection = False
        for wall in walls:
            intersection = get_intersection(line_of_sight, wall[0])
            if intersection is None:
                continue
            if intersection_within_bounds(
                intersection,
                Point(x_spy, y_spy),
                Point(x_camera, y_camera),
                wall[1],
                wall[2],
            ):
                found_intersection = True
                break

        if found_intersection:
            print("NO")
        else:
            print("YES")


if __name__ == "__main__":
    main()
