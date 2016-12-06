# ELO
Elo rank calculations for office foosball

### Usage
command line:
>python3 elo_test.py winner_rank loser_rank

output:
>new_winner_rank new_loser_rank

Example:
>python3 elo_test.py 1200 1200

>1216 1184

### In the DB (for Ilan)
1. Init everyone's rank to 1200
2. Every time you insert a new game, use the api:
`python3 elo_test.py winner_rank loser_rank`
and update the ranks according to the output
3. When a new player joins the DB, give him the rank 1200