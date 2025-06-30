# 🧠 Maze Solver Policies

**Author:** Ruth Perjuste  
**Date:** Dec 15, 2024  

## 🔍 Overview

This project explores different navigation policies for a robot navigating a maze environment. Written in **Python**, it simulates decision-making strategies that a robot might use to reach a goal efficiently while avoiding walls and revisiting paths. The project leverages a custom `maze` module and tests various approaches including random choice, wall-following, and direction-based logic.

## 📁 Features

- **Modular Policy Functions**:
  - `goForwardPolicy`: Always moves forward, ignoring obstacles.
  - `turnAroundPolicy`: Moves forward unless a wall is ahead, then turns back.
  - `bouncePolicy`: Turns left or right when hitting a wall, otherwise continues forward.
  - `leftWallPolicy`: Implements a classic left-hand rule maze-solving algorithm.
  - `customPolicy`: Experiments with random movement and dual-directional choices (WIP).

- **Helper Functions**:
  - `isNotWall(tile)`: Determines whether a tile is navigable.
  - `isNotVisited(tile)`: Checks for previously visited paths.
  - `randomDirection()`: Introduces stochastic behavior to simulate uncertainty.

## 🎯 Purpose

Designed as part of a computer science exercise to test **AI-style movement policies**, this project encourages exploration of how simple decision rules can affect maze-solving success rates. The structure also prepares students for more advanced topics in **pathfinding**, **autonomous agents**, and **reinforcement learning**.

## ⚙️ Technologies Used

- **Python 3**
- **Custom Maze Simulator Module (`maze.py`)**
- **Random module** for introducing non-deterministic decisions



