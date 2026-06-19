from typing import TypeAlias

GameTree: TypeAlias = int | list["GameTree"]

def sample_tree() -> GameTree:
    """Returns a small tree for classroom demonstration."""
    return [
        [3, 5],
        [2, 9],
    ]

def medium_tree() -> GameTree:
    """Returns a medium-sized tree where Alpha-Beta can prune branches."""
    return [
        [[3, 5], [6, 9]], 
        [[1, 2], [0, -1]],
        [[7, 4], [8, 6]],
    ]

def ordered_tree_for_pruning() -> GameTree:
    """Tree intentionally ordered to help Alpha-Beta prune more effectively."""
    return [
        [[10, 9], [8, 7]],
        [[6, 5], [4, 3]],
        [[2, 1], [0, -1]],
    ]