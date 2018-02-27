import random
import subprocess
import os
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
    if path.isdir("F:\\") or path.isdir('/media/rohit/Seagate Backup Plus Drive/'):
        print("S{}E{}".format(season, episode))
        if os.name == 'nt':
            folder_path = "F:\\Rohit\\TV Shows\\Friends\\Season {}\\Friends - {}x{} - *.mkv"
        else:
            folder_path = "/media/rohit/Seagate Backup Plus Drive/Rohit/TV Shows/Friends/Season {}/Friends - {}x{} - *.mkv"
        # Uses glob module to complete the filename by adding the episode title in place of the asterisk.
        path_to_episode = glob(folder_path.format(season, season, episode))
        print(path_to_episode[0])
        if os.name == 'nt':
            os.startfile(path_to_episode[0])
        else:
            subprocess.call(['xdg-open', path_to_episode[0]])
    else:
        print("Media source not found. Please check if drive is connected and mounted.")

