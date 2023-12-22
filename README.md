# Sutom Solver

## Scope

Creation of an app for helping [Sutom](https://sutom.nocle.fr/) users to solve their daily challenge.

The app has been deployed on [Render](https://sutom-solver.onrender.com/) and can be used for any other word game **in French** ([Wordle](https://wordle.louan.me/), crossword...)

## Workflow

The user gives the current state of their finding in the game:
- Validated letters (red)
- Correct letters but in wrong position (yellow)
- Incorrect letters (grey)

Based on the input the app does a lookup in the reference dictionary and displays all the possible solutions.

## Usage

- Install [Docker](https://docs.docker.com/get-docker/)
- `docker-compose build`
- `docker-compose up`

## Author

Louis de Viron - [DataText SRL](https://www.datatext.eu)

## Credentials

This tool is based on reverse-engineering from the [SUTOM project](https://framagit.org/JonathanMM/sutom). The list of words is downloaded from the code repository of the project.
