"""
Usage:
- command line:
python3 elo_test.py winner_rank loser_rank
- output:
new_winner_rank new_loser_rank

Example:
python3 elo_test.py 1200 1200
1216 1184
"""
import math
import sys


def calculate_elo_rank(winner_rank, loser_rank, penalize_loser=True):
    """
    Usage example:
    >>> calculate_elo_rank(1200, 1200)
    (1216, 1184)
    """
    rank_diff = winner_rank - loser_rank
    exp = (rank_diff * -1) / 400
    odds = 1 / (1 + math.pow(10, exp))
    if winner_rank < 2100:
        k = 32
    elif winner_rank >= 2100 and winner_rank < 2400:
        k = 24
    else:
        k = 16
    new_winner_rank = round(winner_rank + (k * (1 - odds)))
    if penalize_loser:
        new_rank_diff = new_winner_rank - winner_rank
        new_loser_rank = loser_rank - new_rank_diff
    else:
        new_loser_rank = loser_rank
    if new_loser_rank < 1:
        new_loser_rank = 1
    return (new_winner_rank, new_loser_rank)


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    winner_rank, loser_rank = calculate_elo_rank(int(sys.argv[1]),
                                                 int(sys.argv[2]))
    print(winner_rank, loser_rank)
