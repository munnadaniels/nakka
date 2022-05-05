import os, sys
import argparse
import subprocess

arguments = argparse.ArgumentParser()
arguments.add_argument("-i", "--id", dest="id", help="content id ")
arguments.add_argument("-o", "--Name", dest="Name", help="quality") 
args = arguments.parse_args()

 


def trackname():
     os.system('ffmpeg -i -map 0:v -map 0:a -map 0:s? -metadata title="@TROOPORIGINALS" -metadata:s:v title="TroopOriginals" -metadata:s:a title="TroopOriginals" -metadata:s:s title="TroopOriginals" -codec copy test.mkv'%link)
     output = f"{filename}"
     subprocess.run(['rclone', output,'Rose:'])

link = str(args.id) 
filename = str(args.Name)
trackname()
