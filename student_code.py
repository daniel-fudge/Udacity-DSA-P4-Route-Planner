#!/usr/bin/env python3
from helpers import Map, load_map


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

    path = []

    # Check arguments
    if not isinstance(graph, Map):
        raise AttributeError("The given graph is not as Map object defined in helpers.py.")
    intersections = graph.intersections
    for arg, name in [(start, "start"), (goal, "goal")]:
        if not isinstance(arg, int):
            raise AttributeError(f"The {name} intersection must be an integer.")
        if arg not in intersections:
            raise AttributeError(f"The {name} intersection has a value of {arg} that isn't given graph.")

    return path


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


def unit_tests() -> int:
    """This is a set of unit tests to aid in development and debugging.

    Note that pyTest or another framework is not used to allow the tests to be included in the Udacity submission."""

    n_errors = 0

    # Test set 1 - Invalid arguments
    print("\nUser test set 1 - Invalid arguments.")
    n_errors += test_invalid_arguments()

    return n_errors


# **********************************************************
if __name__ == '__main__':
    n_total_errors = 0
    # n_total_errors += given_tests()
    n_total_errors += unit_tests()

    print("\n*******************")
    if n_total_errors > 0:
        raise RuntimeError(f"BOO HOO, {n_total_errors} errors detected.\n")
    else:
        print("WOO HOO, No errors detected.\n")
