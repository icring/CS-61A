"""The Game of Hog."""
# Kuriakose Theakanath cs61a-ach
# Nik Mathur cs61a-acg

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100 # The goal of Hog is to score 100 points.

######################
# Phase 1: Simulator #
######################

def roll_dice(num_rolls, dice=six_sided):
    """Roll DICE for NUM_ROLLS times.  Return either the sum of the outcomes,
    or 1 if a 1 is rolled (Pig out). This calls DICE exactly NUM_ROLLS times.

    num_rolls:  The number of dice rolls that will be made; at least 1.
    dice:       A zero-argument function that returns an integer outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    "*** YOUR CODE HERE ***"
    counter, total, dice_rolled_one = 0, 0, False
    while counter < num_rolls:
        curr_roll, counter = dice(), counter + 1
        if curr_roll == 1:
            dice_rolled_one = True
        else:
            total += curr_roll
    return 1 if dice_rolled_one else total


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    "*** YOUR CODE HERE ***"
    if num_rolls == 0:
        first_digit, second_digit = opponent_score // 10, opponent_score % 10
        return abs(second_digit - first_digit) + 1
    else:
        return roll_dice(num_rolls, dice)

def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    "*** YOUR CODE HERE ***"
    if (score + opponent_score) % 7 == 0:
        return four_sided
    else:
        return six_sided


def bid_for_start(bid0, bid1, goal=GOAL_SCORE):
    """Given the bids BID0 and BID1 of each player, returns three values:

    - the starting score of player 0
    - the starting score of player 1
    - the number of the player who rolls first (0 or 1)
    """
    assert bid0 >= 0 and bid1 >= 0, "Bids should be non-negative!"
    assert type(bid0) == int and type(bid1) == int, "Bids should be integers!"

    if bid0 == bid1:
        return goal, goal, 0
    elif bid1 - bid0 == 5:
        return 0, 10, 1
    elif bid0 - bid1 == 5:
        return 10, 0, 0
    else:
        if bid0 > bid1:
            return bid1, bid0, 0
        else:
            return bid1, bid0, 1

def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who

def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    "*** YOUR CODE HERE ***"
    while score0 < goal and score1 < goal:
        if who == 0:
            score0 += take_turn(strategy0(score0, score1), score1, select_dice(score0, score1))
        else:
            score1 += take_turn(strategy1(score1, score0), score0, select_dice(score0, score1))
        who = other(who)
        if score0 == 2*score1 or score1 == 2*score0:
            score0, score1 = score1, score0
    return score0, score1  # You may want to change this line.

#######################
# Phase 2: Strategies #
#######################

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n
    return strategy

# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    >>> make_averaged(roll_dice, 1000)(2, dice)
    6.0

    In this last example, two different turn scenarios are averaged.
    - In the first, the player rolls a 3 then a 1, receiving a score of 1.
    - In the other, the player rolls a 5 and 6, scoring 11.
    Thus, the average value is 6.0.
    """
    "*** YOUR CODE HERE ***"
    def avg(*args):
        counter, total = 0, 0
        while counter < num_samples:
            total, counter = total + fn(*args), counter + 1
        return total/num_samples
    return avg

def max_scoring_num_rolls(dice=six_sided):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE.  Print all averages as in
    the doctest below.  Assume that dice always returns positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    "*** YOUR CODE HERE ***"
    counter, score, curr_avg_roll, roll = 1, 0, 0, 0
    while counter <= 10: 
         curr_avg_roll = make_averaged(roll_dice)(counter, dice)
         if curr_avg_roll > score:
             score, roll = curr_avg_roll, counter
         counter += 1
    return roll


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1

def average_win_rate(strategy, baseline=always_roll(5)):
    """Return the average win rate (0 to 1) of STRATEGY against BASELINE."""
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)
    return (win_rate_as_player_0 + win_rate_as_player_1) / 2 # Average results

def run_experiments():
    """Run a series of strategy experiments and report results."""
    if False: # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if False: # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if False: # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if False: # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    if True: # Change to True to test final_strategy
        print('final_strategy win rate:', average_win_rate(final_strategy))
    "*** You may add additional experiments as you wish ***"

# Strategies

def bacon_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    "*** YOUR CODE HERE ***"
    if take_turn(0, opponent_score) >= margin:
        return 0
    else:
        return num_rolls

def swap_strategy(score, opponent_score, margin=8, num_rolls=5):
    """This strategy rolls 0 dice when it would result in a beneficial swap and
    rolls NUM_ROLLS if it would result in a harmful swap. It also rolls
    0 dice if that gives at least MARGIN points and rolls
    NUM_ROLLS otherwise.
    """
    "*** YOUR CODE HERE ***"
    after_score = score + take_turn(0, opponent_score)
    if after_score == 2*opponent_score:
        return num_rolls
    elif after_score == opponent_score/2:
        return 0
    else: 
        return bacon_strategy(score, opponent_score, margin, num_rolls)

scores_for_person = []
scores_for_opponent = []
counter = 0

def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.
        
        Rolling 5 is the safest roll with highest average, based on 1000 tests.
        First checks if play can do Swine Swap (first three conditionals), as it
        has the greatest damage (to yourself or opponent). Rolls 5 to stay safe, 0
        or 10 if future total initiates Swine Swap. Next strategy tries to trap opponent
        with a 4 sided dice, if Free Bacon is used. Lastly (last conditional),
        variation of bacon strategy is called, based on if user is rolling 4 or 6
        sided die.
        """
    
    """Implementation"""
def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.
        
        *** YOUR DESCRIPTION HERE ***
        """
    "*** YOUR CODE HERE ***"
    extra = score + 1 + abs(opponent_score//10 - opponent_score%10)
    if (score == 2*(opponent_score+1)): #if opponent rolls die of 1 (pigout) and score is equal to 2 times that (bad bc thats a swine swap)
        return 0
    elif (opponent_score == (score+1)*2): #if score + 1 times 2 equals opponent score, it'll be a swine swap, so roll as many die as possible (10) to trigger pigout (1) and swine swap
        return 9
    elif ((score+1) == (2*opponent_score)): #if score+1 equals 2 times opponent score, that's bad bc swine swap, so roll less -> 0
        return 4
    baconpoints = take_turn(0, opponent_score) #compute points of rolling 0 die
    score = score + baconpoints #add these to score
    dice = select_dice(score, opponent_score)
    if (dice == four_sided): # if result of rolling 0 die is a 4 sided die for next player, return 0 bc you want him/her to have 4 sided die bc greater chance of rolling 1
        return 0
    score = score - baconpoints  #get back to original score
    dice = select_dice(score, opponent_score)
    if (extra*2 == opponent_score):
        return 0
    if (dice == four_sided): #these conditions/num_rolls are taken in consideration of a 4 sided die - generally less rolls wanted than if we had 6 sided die (bc > chance of rolling 1)
        if (score < opponent_score):
            score = score + baconpoints
            if (opponent_score == 2*score): #what we want
                return 0
            score = score - baconpoints
            if (score*1.5<opponent_score): #return more die if curr player is really behind
                return 5
            elif (baconpoints>= 8): #8 points of baconpoints (rolling 0 die) is a lot, so just roll 0 for those points
                return 0
            elif (baconpoints< 8) : # less than 8 points isnt good, so return a decent # of die
                return 5

elif (score> opponent_score):
    
    score = score + baconpoints
        if (score == 2*opponent_score): #not what we want
            return 3
            score = score - baconpoints
            if (score > 1.5*opponent_score): #return less rolls if you're far ahead
                return 3
        elif (baconpoints>= 8): # same logic as before; free bacon pts > 8 are good enough, else return decent # of rolls
            return 0
            elif (baconpoints< 8) :
                return 4
                    elif (score == opponent_score):

if (baconpoints>= 8):
    return 0
        elif (baconpoints< 8) :
            return 4
    if (dice == six_sided): #same logic as with previous conditionals of 4 sided die, but more rolls bc less chance of rolling 1
        if (score < opponent_score):
            score = score + baconpoints
            if (opponent_score == 2*score): #what we want
                return 0
            score = score - baconpoints
            if (score*1.5<opponent_score):
                return 7
            elif (baconpoints>= 8):
                return 0
            elif (baconpoints< 8) :
                return 6

    elif (score > opponent_score):
        score = score + baconpoints
            if (score == 2*opponent_score): #not what we want
                return 4
                score = score - baconpoints
                if (score > 1.5*opponent_score):
                    return 4
            elif (baconpoints>= 8):
                return 0
                elif (baconpoints< 8) :
                    return 4
                        elif (score == opponent_score):
                            if (baconpoints>= 8):
                                return 0
            elif (baconpoints< 8) :
                return 5





##########################
# Command Line Interface #
##########################

# Note: Functions in this section do not need to be changed.  They use features
#       of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')
    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
