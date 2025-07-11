"""
Authors: Ruth Perjuste 
Consulted:
Date: 10-15-2024
Purpose: mazePolicies task: policies for helping a robot to solve a maze.
"""

# Lets us access functions and variables from the maze module.
import maze

# Extra import for random decisions, which might be used in customPolicy
import random


#------------------#
# Helper functions #
#------------------#

# Use these to check if one of the four policy arguments is a wall or
# whether it counts as "open."

def isNotWall(tile):
    """
    Returns True if the given tile is NOT a wall.
    """
    return tile != '#'


def isNotVisited(tile):
    """
    Returns True if the given tile is not a wall and hasn't been visited
    (either it's blank or it's the goal).
    """
    return tile == ' ' or tile == 'G'


# This function is one way to incorporate randomness, but you don't have
# to use it.
def randomDirection():
    """
    Returns a random direction.
    """
    return random.choice([
        maze.LEFT,
        maze.RIGHT,
        maze.FORWARD,
        maze.BACKWARD
    ])


#-----------------#
# Simple policies #
#-----------------#

# Use these as reference for your policies.

def goForwardPolicy(ahead, right, behind, left, fuel):
    """
    The goForwardPolicy is the simplest possible policy: it just tries to
    go forward no matter what.
    """
    return maze.FORWARD


def turnAroundPolicy(ahead, right, behind, left, fuel):
    """
    The turnAroundPolicy always moves forward unless there's a wall ahead,
    in which case it turns around. It is very bad at solving mazes.

    Note that we don't have to use all of the arguments: we can ignore
    some if we want, but we can't add or delete or any.
    """
    if isNotWall(ahead): # there's no wall in front of us: go forward
        return maze.FORWARD # keep going forward
    else: # otherwise turn around
        return maze.BACKWARD # tell the robot to go backwards


#-------------------#
# Required policies #
#-------------------#

# Implement the required policies here (just fill out the functions where
# it says "TODO" and remove those comments). Remember that every policy
# must return one of the four direction variables: maze.FORWARD,
# maze.LEFT, maze.RIGHT, or maze.BACKWARD.

def bouncePolicy(ahead, right, behind, left, fuel):
    """
    The bouncePolicy bounces left (or right) when it hits a wall but keeps
    going straight otherwise. It isn't very good at solving mazes, but it
    can solve labyrinths (mazes with no branches).
    """
    # TODO: implement this policy!
    """Turns left if there is not wall near bye"""
    if isNotWall(left):
        return maze.LEFT
    if isNotWall(right):
        return maze.RIGHT
    else:
        return maze.FORWARD

def leftWallPolicy(ahead, right, behind, left, fuel):
    """
    The leftWallPolicy follows the left-hand wall: turning left when it
    can, going forward if it can't, turning right if forward and left are
    blocked, and giving up and going backwards if that's the only option.
    """
    # TODO: implement this policy!
    if isNotWall(left):
        return maze.LEFT
    
    if (not isNotWall(left)) and isNotWall(ahead):
        return maze.FORWARD 
        
    if (not isNotWall(left)) and (isNotWall(right)):
        return maze.RIGHT
    if (not isNotWall(left)) and (not isNotWall(right)) and (not isNotWall(ahead)):
        return maze.LEFT
    

def customPolicy(ahead, right, behind, left, fuel):
    """
    """
    # TODO: implement this policy and describe what it does!
    random=randomDirection()
    
    if isNotWall(ahead) and isNotWall(behind):
        return maze.FORWARD 
    if isNotWall(right) and isNotWall(left):
        return maze.RIGHT and maze.FORWARD
    if isNotWall(left) or isNotRight(right):
        return maze.LEFT and maze.FORWARD
        
    
  
