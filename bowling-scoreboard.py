#!/usr/bin/env python

import sys

def main():
    rolls = sys.argv[1:]

	# Print the header row of the scoreboard
    headers = ['FR', 'R1', 'R2', 'R3', 'Score']
    print '\t'.join(headers) 
    print '-------------------------------------'

    # Given the input, print the rest of the scoreboard
    frame = 0
    total_score = 0
    while rolls and frame < 11:
        frame += 1
        R1 = safe_pop(rolls)

        # Check for one or consecutive strikes
        while R1 == 10:
            if frame == 10: # last frame
                R2 = safe_pop(rolls)
                R3 = safe_pop(rolls)
                total_score = update_score(total_score, R2, R3, 10)
                print_row(frame, 'X', R2, R3, total_score)
                return
            else:
                total_score = update_score(total_score, safe_peek(rolls, 0), safe_peek(rolls, 1), 10)
                print_row(frame, 'X', None, None, total_score)
                R1 = safe_pop(rolls)
            frame += 1

        # Check for a spare or open frame
        R2 = safe_pop(rolls)
        if frame_sum(R1, R2) == 10: # spare
            total_score = update_score(total_score, R1, R2, safe_peek(rolls, 0))
            print_row(frame, R1, '/', None, total_score)
        else:
            total_score = update_score(total_score, R1, R2, 0)
            print_row(frame, R1, R2, None, total_score)


# Finds the sum of pins knocked down in a frame (two rolls)
def frame_sum(R1, R2):
    total = 0
    if R1 != None:
        total += R1
    if R2 != None:
        total += R2
    return total


# Checks that each roll score is between 1-10
def in_bounds(score):
    if score != None and (score < 0 or score > 10):
        sys.exit("Error: Scores must be between 0-10")


# Prints the tab-separated scores for rolls in each frame
def print_row(frame, R1, R2, R3, total_score):
    in_bounds(R1), in_bounds(R2), in_bounds(R3)
    if (R1 == None) and (R2 == None) and (R3 == None):
        return

    if R1 == None:
        R1 = ' '
    if R2 == None:
        R2 = ' '
    if R3 == None:
        R3 = ' '
    print frame, '\t', R1, '\t', R2, '\t', R3, '\t', total_score


# Removes and returns the int value of given index, otherwise returns None
def safe_pop(rolls):
    if rolls: 
        return int(rolls.pop(0))
    else:
        return None


# Returns the int value of given index, otherwise returns None
def safe_peek(rolls, index):
    if index < len(rolls):
        return int(rolls[index])
    else:
        return None


# Returns new score, accounting for strike/spare bonus points
def update_score(total_score, R1, R2, bonus):
    if R1 != None:
        total_score += R1
    if R2 != None:
        total_score += R2
    if bonus != None:
        total_score += bonus
    return total_score


# Call the main function
if __name__ == '__main__':
    main()