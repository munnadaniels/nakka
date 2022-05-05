import os, sys
import argparse
import subprocess

arguments = argparse.ArgumentParser()
arguments.add_argument("-i", "--id", dest="id", help="content id ")
arguments.add_argument("-o", "--Name", dest="Name", help="quality") 
args = arguments.parse_args()

link = args.id
filename = args.Name


def trackname():
     os.system('ffmpeg -i {link} -map 0:v -map 0:a -map 0:s? -metadata title="@TROOPORIGINALS" -metadata:s:v title="TroopOriginals" -metadata:s:a title="TroopOriginals" -metadata:s:s title="TroopOriginals" -codec copy {filename}')
     output = f"{filename}"
     subprocess.run(['rclone', output,'Rose:'])

trackname()
