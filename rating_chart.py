from collections import namedtuple
import datetime
import math
import os
import sys
import asciichartpy as ac
import requests

USERNAME = 'sciencepal'
TIME_CLASS = 'blitz'
RULES = 'chess' #chess960 and other variants possible here
NGAMES = 100
ARCHIVES_URL = 'https://api.chess.com/pub/player/{user}/games/archives'

def get_archives() -> list:
    archives_dict = requests.get(ARCHIVES_URL.format(user=USERNAME)).json()
    monthly_archives = archives_dict.get('archives')
    if monthly_archives is None:
        return 
    return monthly_archives[::-1]


def get_filtered_games(monthly_archive_url: str) -> list:
    games_dict = requests.get(monthly_archive_url).json()
    monthly_games = games_dict.get('games')
    if monthly_games is None:
        return
    _filtered_games = list(filter(lambda game: game['time_class'] == TIME_CLASS, monthly_games))
    filtered_games = list(filter(lambda game: game['rules'] == RULES, _filtered_games))
    return filtered_games[::-1]

def get_ratings_from_games(games: list) -> list:
    ratings = []
    for game in games:
        if game['white']['username'] == USERNAME:
            ratings.append(game['white']['rating'])
        else:
            ratings.append(game['black']['rating'])
    return ratings

def get_current_rating() -> int:
    pass


def main():
    final_games = []
    archives = get_archives()
    for archive in archives:
        final_games += get_filtered_games(archive)
        if len(final_games) >= NGAMES:
            break
    final_games = final_games[:NGAMES]
    ratings_list = get_ratings_from_games(final_games)[::-1]
    return (ac.plot(ratings_list, {'height': 20}))


if __name__ == "__main__":

    plot = main()
    print (plot)
