#!/usr/bin/env python3
from helpers import Map, load_map
from math import sqrt
from heapq import heappush, heappop


class Route:
    """A class capture a route through the map.

    Attributes:
        path (list): The series of intersections visited on the route from the starting intersection.

    """
    def __init__(self, start: int, start_x: float, start_y: float, goal_x: float, goal_y: float):
        """The object initialization.

        Args:
            start (int): The start of the Route
        """
        self.path = [start]
        self.g = 0
        self.h = sqrt((start_x - goal_x)**2 + (start_y - goal_y)**2)
        self.f = self.g + self.h
        self.x = start_x
        self.y = start_y
        self.goal_x = goal_x
        self.goal_y = goal_y

    def add(self, intersection: int, x: float, y: float):
        """Add an intersection to the route.

        Args:
            intersection (int): The new intersection.
            x (float): The X coordinate of the new intersection.
            y (float): The Y coordinate of the new intersection.
        """
        self.path.append(intersection)
        self.g += sqrt((x - self.x)**2 + (y - self.y)**2)
        self.h = sqrt((x - self.goal_x)**2 + (y - self.goal_y)**2)
        self.f = self.g + self.h
        self.x = x
        self.y = y

    def copy(self):
        """Returns a copy of the current object.

        Returns:
            Route: A copy of the current route.
        """

        new_route = Route(self.path[0], self.x, self.y, self.goal_x, self.goal_y)
        new_route.path = self.path.copy()
        new_route.g = self.g
        new_route.h = self.h
        new_route.f = self.f

        return new_route

    def get_f(self) -> float:
        """Returns the total cost function f.

        Returns:
            float: The total cost function f.
        """
        return self.f

    def get_last_intersection(self) -> int:
        """Returns the last intersection on the Route.

        Returns:
            int: The last intersection on the Route.
        """
        return self.path[-1]

    def get_path(self) -> list:
        """Returns the Route.

        Returns:
            list of int: The list of intersections representing the Route.
        """
        return self.path


def shortest_path(graph: Map, start: int, goal: int) -> list:
    """Determines the shortest path with the start and goal nodes of the given map.

    If no path is possible, an empty list is returned.
    If the start and goal are the same, the list only includes the single value, not both start and end.

    Args:
        graph (Map): The Map object that defines the intersections and connecting roads.
        start (int): The starting intersection.
        goal (int): The desired ending intersection.

    Returns:
        list of int: The intersection numbers from the start to the goal, including both the start and end.

    Raises:
        AttributeError: If the given graph is not a Map object.
        AttributeError: If the start and goal are not integers list in the given graph intersections list attribute.
    """

    # Check arguments
    if not isinstance(graph, Map):
        raise AttributeError("The given graph is not as Map object defined in helpers.py.")
    intersections = graph.intersections
    for arg, name in [(start, "start"), (goal, "goal")]:
        if not isinstance(arg, int):
            raise AttributeError(f"The {name} intersection must be an integer.")
        if arg not in intersections:
            raise AttributeError(f"The {name} intersection has a value of {arg} that isn't given graph.")

    # If the start and goal are the same, no need to use the A* algorithm
    if start == goal:
        return [start]

    # "visited" is the set of nodes that have already been visited, so do not need to be searched again
    visited = set()

    # Initialize the starting route, which is simply the starting intersection
    start_route = Route(start=start, start_x=graph.intersections[start][0], start_y=graph.intersections[start][1],
                        goal_x=graph.intersections[goal][0], goal_y=graph.intersections[goal][1])

    # "queue" is the search queue containing the list of routes on the frontier initialized with the start intersection
    # The queue is sorted by the f value with Python's min-heap heapq package.
    queue = []
    heappush(queue, (start_route.get_f(), start_route))

    # "best" is the route that has reached the goal with the best "f" value
    best = None

    # Keep searching until the queue is exhausted
    while len(queue) > 0:
        current_f, current_route = heappop(queue)
        current_intersection = current_route.get_last_intersection()
        visited.add(current_intersection)
        for intersection in [i for i in graph.roads[current_intersection] if i not in visited]:
            new_route = current_route.copy()
            new_route.add(intersection=intersection, x=graph.intersections[intersection][0],
                          y=graph.intersections[intersection][1])

            # Save the route if it reached the goal
            if intersection == goal:
                if best is None:
                    best = new_route
                elif new_route.get_f() < best.get_f():
                    best = new_route

            # Add the new route to the queue if not at the goal and f is less than the best f value
            else:
                if best is None:
                    heappush(queue, (new_route.get_f(), new_route))
                elif new_route.get_f() < best.get_f():
                    heappush(queue, (new_route.get_f(), new_route))

    # best == None, the goal was not reached and an empty list is returned
    if best is None:
        return []

    return best.get_path()


def test_invalid_arguments() -> int:
    """Test the top level methods with invalid arguments.

    Returns:
        int: The number of errors
    """
    test = 0
    n_errors = 0
    for graph in [3.5, 2, [], None]:
        test += 1
        try:
            # noinspection PyTypeChecker
            shortest_path(graph=graph, start=1, goal=3)
        except AttributeError:
            print(f"Test {test} passed.")
        else:
            print(f"Error test {test}: expected an AttributeError exception.")
            n_errors += 1

    map_10 = load_map('map-10.pickle')
    for bad_intersection in [3.5, 10, [2], None, ""]:
        test += 1
        try:
            # noinspection PyTypeChecker
            shortest_path(graph=map_10, start=1, goal=bad_intersection)
        except AttributeError:
            print(f"Test {test} passed.")
        else:
            print(f"Error test {test}: expected an AttributeError exception.")
            n_errors += 1

    test += 1
    try:
        # noinspection PyTypeChecker
        shortest_path(graph=map_10, start=bad_intersection, goal=3)
    except AttributeError:
        print(f"Test {test} passed.")
    else:
        print(f"Error test {test}: expected an AttributeError exception.")
        n_errors += 1

    return n_errors


def test_map_10() -> int:
    """Test simple map with only 10 intersections.

    Returns:
        int: The number of errors
    """

    test = 0
    n_errors = 0
    map_10 = load_map('map-10.pickle')
    for start, goal, expected in [(6, 4, [6, 0, 5, 3, 4]), (3, 3, [3]), (8, 6, []), (8, 9, [8, 9])]:
        test += 1
        actual = shortest_path(graph=map_10, start=start, goal=goal)
        if actual == expected:
            print(f"Test {test} passed.")
        else:
            print(f"Test {test} failed: actual={actual}, expected={expected}.")
            n_errors += 1

    return n_errors


def test_map_40() -> int:
    """Test larger map with only 40 intersections.

    Returns:
        int: The number of errors
    """

    test = 0
    n_errors = 0
    map_40 = load_map('map-40.pickle')
    for start, goal, expected in [(5, 34, [5, 16, 37, 12, 34]), (5, 5,  [5]), (8, 24, [8, 14, 16, 37, 12, 17, 10, 24])]:
        test += 1
        actual = shortest_path(graph=map_40, start=start, goal=goal)
        if actual == expected:
            print(f"Test {test} passed.")
        else:
            print(f"Test {test} failed: actual={actual}, expected={expected}.")
            n_errors += 1

    return n_errors


def unit_tests() -> int:
    """This is a set of unit tests to aid in development and debugging.

    Note that pyTest or another framework is not used to allow the tests to be included in the Udacity submission."""

    n_errors = 0

    # Invalid arguments
    print("\nInvalid arguments.")
    n_errors += test_invalid_arguments()

    # Map 10
    print("\nMap 10.")
    n_errors += test_map_10()

    # Map 40
    print("\nMap 40.")
    n_errors += test_map_40()

    return n_errors


# **********************************************************
if __name__ == '__main__':
    n_total_errors = 0
    n_total_errors += unit_tests()

    print("\n*******************")
    if n_total_errors > 0:
        raise RuntimeError(f"BOO HOO, {n_total_errors} errors detected.\n")
    else:
        print("WOO HOO, No errors detected.\n")
