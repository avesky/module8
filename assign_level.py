"""
Program: average_scores.py
Author: Andy Volesky
Last date modified: 10/20/2021

The purpose of this program:

Create a file assign_level.py
Write switch_level() to assign points to a level
Include the cases outlined above
Write main()
call switch_level() for various levels and print the results

"""
levels = {"Novice": 50, "Beginner": 150, "Experienced": 300, "Advanced": 500}


def switch_level(new_level):
    player_pts = 0
    if new_level in levels:
        player_pts = player_pts + levels.get(new_level)
    print(player_pts)


if __name__ == "__main__":
    new_level = "Novice"
    switch_level(new_level)
    new_level = "Beginner"
    switch_level(new_level)
    new_level = "Experienced"
    switch_level(new_level)
