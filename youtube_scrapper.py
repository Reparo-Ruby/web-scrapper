import urllib.request
import webbrowser
import re

input = input("which video do you want to watch? ")
video = input.replace(" ", "")
html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + video)
video_ids = re.findall(r"watch\?v=(\S{11})",html.read().decode())
watch = "https://www.youtube.com/watch?v="+video_ids[0]
webbrowser.open(watch)
# print(watch)