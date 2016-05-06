import os
import sys

# Twitch Variables
source = "best" if len(sys.argv) == 2 else sys.argv[2]
username = str(sys.argv[1])

# Print Stream Info
if len(sys.argv) == 2:
	print("Now Streaming: " + sys.argv[1])	
else:
	print("Now Streaming: " + sys.argv[1])
	print("Quality: " + sys.argv[2])

# Concat livestreamer statement
str = "livestreamer twitch.tv/" + username + " " + source  + " -np  'omxplayer -o hdmi'"

os.system(str)
