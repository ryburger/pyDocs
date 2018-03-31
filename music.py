#ultimate music download
import os
import requests
import re
#constants
art = input('artist(like This):')
alb = input('album(like This):')
gen = input('genre:')
enc = 'burger'
ash = 'sudo youtube-dl -i -f 18 -o \"%(autonumber)s-%(title)s.%(ext)s\" '
htp = 'https://www.youtube.com/playlist?'
plusArt = art.replace(' ', '+')
plusAlb = alb.replace(' ', '+')
camelArt = art.replace(' ', '')
camelAlb = alb.replace(' ', '')
num1 = 0
num2 = 0
picNum = 0
tgs = -1
tks = -1
#lists
tags = []
tracks = []
picList = []
#playlist search
ytQuest = requests.get('https://youtube.com/results?sp=EgIQAw%253D%253D&search_query=' + plusArt + '+' + plusAlb)
ytString = ytQuest.text
ytMatch = re.search('(?<=aria-hidden=\"true\"><a) (.*)', ytString)
dolphin = ytMatch.groups()
humpback = dolphin[0]
crab, shark = humpback.split(';')
url, krill = shark.split('\"', 1)
#get art alpha
alphaQuest = requests.get('https://en.wikipedia.org/w/index.php?search=' + plusArt + '+' + plusAlb)
alphaString = alphaQuest.text
alphaMatch = re.search('(?<=<ul class=\'mw-search-results\'><li><div class=\'mw-search-result-heading\'><a href=\")(.*)', alphaString)
gorilla = alphaMatch.groups()
gibbon = gorilla[0]
pgUrl, bonobo = gibbon.split('\"', 1)
#get art beta
betaQuest = requests.get('https://en.wikipedia.org' + pgUrl)
betaString = betaQuest.text
betaMatch = re.search('(?<=<meta property=\"og:image\" content=\")(.*)', betaString)
gazelle = betaMatch.groups()
ibex = gazelle[0]
imgUrl = ibex[:-3]
os.system('sudo curl ' + imgUrl + ' > albumArt.jpg')
os.system('fbi albumArt.jpg')
#youtube-dl
go = ash + htp + url
os.system(go)
os.system('ls | less')
#song info
num1 = int(input('#-of-songs:'))
num2 = num1
while num1 != 0:
	os.system('ls | less')
	lp1tgs = input('last-2-#:')
	lp1tks = input('title:')
	tags.append(lp1tgs)
	tracks.append(lp1tks)
	num1 -= 1
#ffmpeg loop
while num2 != 0:
	tgs += 1
	tks += 1
	lp2tgs = tags[tgs]
	lp2tks = tracks[tks]
	new = lp2tgs + '_' + lp2tks
	get = 'sudo ffmpeg -i 000' + lp2tgs + '*.mp4 -vn -metadata album=\"' + camelAlb + '\" -metadata genre=\"' + gen + '\" -metadata artist=\"' + camelArt + '\" -metadata encoded_by=\"' + enc + '\" -metadata title=\"' + lp2tks + '\" -metadata track=\"' + lp2tgs + '\" ' + new + '.mp3'
	os.system(get)
	os.system('sudo rm 000' + lp2tgs + '*.mp4')
	num2 -= 1
	os.system('/opt/vc/bin/vcgencmd measure_temp')
#add art
os.system('sudo rm -r *.mp4')
picFiles = os.listdir()
for picture in picFiles:
	if picture.endswith('.mp3'):
		picList.append(picture)
picLen = len(picList)
while picLen != 0:
	picSong = picList[picNum]
	os.system('sudo ffmpeg -i *' + picSong + ' -i *.jpg -map_metadata 0 -map 0 -map 1 -acodec copy 0' + picSong)
	picNum += 1
	picLen -= 1
os.system('sudo rm -r ??_*.mp3 *.jpg')
#file away music
os.system('sudo mkdir ' + camelArt + '-' + camelAlb)
os.system('sudo mv *.mp3 ' + camelArt + '-' + camelAlb)
os.system('sudo mv ' + camelArt + '-' + camelAlb + ' ../holdingTank')
