import os, sys
import argparse
import subprocess

arguments = argparse.ArgumentParser()
arguments.add_argument("-i", "--id", dest="id", help="content id ")
arguments.add_argument("-o", "--Name", dest="Name", help="quality") 
args = arguments.parse_args()

 


def trackname(link):
     os.system('ffmpeg -i https://www.movie-zone.cf/0:/Moon%20Knight%20S01%201080p%20DS4K%20SDR%20DSNP%20WEBRip%20x265%2010Bit%20%28DD%2B%205.1%20-%20192Kbps%29%20%5BTel%20%2B%20Tam%20%2B%20Hin%20%2B%20Mal%20%2B%20Eng%5D%20MSub%20_TeamHTP_.mkv -map 0:v -map 0:a -map 0:s? -metadata title="@TROOPORIGINALS" -metadata:s:v title="TroopOriginals" -metadata:s:a title="TroopOriginals" -metadata:s:s title="TroopOriginals" -codec copy {filename}')
     output = f"{filename}"
     subprocess.run(['rclone', output,'Rose:'])

link = str(args.id) 
filename = str(args.Name)
trackname(link)
