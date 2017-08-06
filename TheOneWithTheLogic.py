import random
from os import startfile
from os import path
from glob import glob

season = random.randrange(1, 11)
# Dictionary of season and number of episodes it contains.
seasonData = {1: 24, 2: 24, 3: 25, 4: 24, 5: 24, 6: 25, 7: 24, 8: 24, 9: 23, 10: 17}
episodeInt = random.randrange(1, seasonData[season])
if episodeInt < 10:
    episode = "0"+str(episodeInt)
    # Prefixes a '0' to the episode number if its just a single digit because that's how my library is named.
else:
    episode = str(episodeInt)
if path.isdir("F:\\"):
    print("S{}E{}".format(season, episode))
    # Uses glob module to complete the filename by adding the episode title in place of the asterisk.
    path = glob("F:\\Rohit\\TV Shows\\Friends\\Season {}\\Friends - {}x{} - *.mkv".format(season, season, episode))
    startfile(path[0])
else:
    print("Media source not found. Please check if drive is connected and mounted.")
