import random
from os import startfile
from os import path
from glob import glob


def play_episode():
    season = random.randrange(1, 11)
    # Dictionary of season and number of episodes it contains.
    season_data = {1: 24, 2: 24, 3: 25, 4: 24, 5: 24, 6: 25, 7: 24, 8: 24, 9: 23, 10: 17}
    episode_int = random.randrange(1, season_data[season])
    if episode_int < 10:
        episode = "0"+str(episode_int)
        # Prefixes a '0' to the episode number if it is just a single digit because that's how my library is named.
    else:
        episode = str(episode_int)
    if path.isdir("F:\\"):
        print("S{}E{}".format(season, episode))
        # Uses glob module to complete the filename by adding the episode title in place of the asterisk.
        path_to_episode = glob("F:\\Rohit\\TV Shows\\Friends\\Season {}\\Friends - {}x{} - *.mkv".format(season, season, episode))
        startfile(path_to_episode[0])
    else:
        print("Media source not found. Please check if drive is connected and mounted.")
