#ultimate music download
import os
import requests
import re
#constants
os.system('rm -fr /data/data/com.termux/files/home/mp3/wrk/*')
art = input('artist: ')
alb = input('album: ')
gen = input('genre: ')
enc = 'burger'
ash = 'youtube-dl -q -i -f \'bestaudio[ext=m4a]\' -o \"%(autonumber)s-%(title)s.%(ext)s\" '
htp = 'https://www.youtube.com/playlist?'
plusArt = art.replace(' ', '+')
plusAlb = alb.replace(' ', '+')
underArt = art.replace(' ', '_')
underAlb = alb.replace(' ', '_')
num1 = 0
num2 = 0
picNum = 0
tgs = -1
tks = -1
lizard = 0
tags = []
tracks = []
picList = []
#track/image search
allQuest = requests.get('https://www.allmusic.com/search/albums/' + plusAlb, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/41.0.2228.0 Safari/537.36'})
allString = allQuest.text
#print(allString)
#holdingHere = input('hold')
allMatch = re.findall('(?<=<a class=\"album-cover-link crop-image-borders\" href=\")(.*)', allString)
yn = 'n'
matchTik = 0
while yn == 'n':
	albArt, trashBaby = allMatch[matchTik].split('\"', 1)
#	print(albArt)
	brawlQuest = requests.get('https://www.allmusic.com/' + albArt, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, likeGecko) Chrome/41.0.2228.0 Safari/537.36'})
	brawlString = brawlQuest.text
	brawlMatch = re.findall('(?<=https://www.allmusic.com/artist/)(.*)', brawlString)
#	print(brawlMatch[0])
	artCheck = brawlMatch[0].split('alt=\"')
	fartCheck, dumpsterBaby = artCheck[0].split('-mn00')
#	print(fartCheck)
#	yn = input('stop')
	lassie = allMatch[matchTik]
	discUrl, gus = lassie.split('\"', 1)
	unwated, wanted = discUrl.split('album/')
	theGood, theBad = wanted.split('-mw00')
#	print(theGood)
	artistCheck = fartCheck.replace('-', ' ')
	albumCheck = theGood.replace('-', ' ')
	print('Artist: ' + artistCheck)
	print('Album: ' + albumCheck)
	yn = input('match? (y/n): ')
	fallMatch = re.search('(?<=data-original=\")(.*)', lassie)
	john = fallMatch.groups()
	jimmy = john[0]
	jack, jill = jimmy.split('\"', 1)
	jorge = jack.replace('170/', '500/')
	os.system('curl -s ' + jorge + ' > albumImg.jpg')
#	os.system('fbi albumImg.jpg')
#	yn = 'y'
#	yn = input('is this your album cover?(y/n): ')
	if yn == 'n':
		matchTik += 1
	elif yn == 'error':
		os.system('rm -f albumImg.jpg')
		jorge = jack.replace('170/','400/')
		os.system('curl -s ' + jorge + ' > albumImg.jpg')
		os.system('fbi albumImg.jpg')
		yn = input('is this your album cover?(y/n): ')
		if yn == 'n':
			matchTik += 1

art = artistCheck
alb = albumCheck
discList = []
ytdlList = []
curry = 0
discQuest = requests.get('https://www.allmusic.com' + discUrl, headers={'User-Agent': 'Mozilla/5.0 (X11;Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'})
discString = discQuest.text
discMatch = re.findall('(?<=https://www.allmusic.com/song/)(.*)', discString)
#print(len(discMatch))
discLen = len(discMatch)
while discLen != 0:
	cry = discMatch[curry]
	high, guy = cry.split('\"', 1)
	underTrack, mountain = high.split('-mt00', 1)
	lye = underTrack.replace('-', ' ')
#	print(lye)
	discList.append(lye)
	discLen -= 1
	curry +=1
#youtube fetch and download
ytQuest = requests.get('https://youtube.com/results?sp=EgIQAw%253D%253D&search_query=' + plusArt + '+' + plusAlb)
ytString = ytQuest.text
ytMatch = re.findall('(?<=aria-hidden=\"true\"><a) (.*)', ytString)
ytyn = 'n'
while ytyn == 'n':
	dolphin = ytMatch[lizard]
	crab, shark = dolphin.split(';')
	url, krill = shark.split('\"', 1)
	go = ash + htp + url
	got = 'youtube-dl -i --get-title ' + htp + url
	print('Fetching Songs...')
	os.system(got + ' > songs.txt')
	musicFile = open('songs.txt', 'r')
	for line in musicFile:
		ytdlList.append(line)
	timerOne = len(discList)
	timerTwo = len(ytdlList)
	timerThree = 0
	timerFour = 0
#	print(len(ytdlList), len(discList))
	while timerOne != 0 and timerTwo != 0:
		timerFour += 1
		print(str(timerFour) + '. ' + ytdlList[timerThree] + '-' + discList[timerThree])
		timerOne -= 1
		timerTwo -= 1
		timerThree += 1
	ytyn = input('good?(y/n): ')
	if ytyn == 'n':
		os.system('rm songs.txt')
		ytdlList = []
		lizard += 1
print('Downloading Songs...')
os.system(go)
#song info
num1 = len(discList)
num3 = 0
num4 = len(ytdlList)
misTitle = []
misNumber = []
misOrder = 0
os.system('ls')
while num1 != 0:
	misOrder += 1
	lp1tks = discList[num2]
	lp1tgs = input('(' + lp1tks + ') last 2# (n/d/c): ')
	if lp1tgs == 'n':
		num1 -= 1
		num2 += 1
		misTitle.append(lp1tks)
		misNumber.append(misOrder)
	elif lp1tgs == 'd':
		num1 = 0
	elif  lp1tgs == 'c':
		lp1tgs = input('last 2#: ')
		lp1tks = input('new name: ')
		tags.append(lp1tgs)
		tracks.append(lp1tks)
		num1 -= 1
		num2 += 1
		num3 += 1

	else:
		tags.append(lp1tgs)
		tracks.append(lp1tks)
		num1 -= 1
		num2 += 1
		num3 += 1
#add missing songs
simba = 0
snickers = len(misTitle)
if snickers > 0:
	print('There are ' + str(snickers) + ' missing song(s)')
	missingSongsYN = input('Do you want to find them? (y/n): ')
else:
	misNumber.append(9999)
while snickers != 0 and missingSongsYN == 'y':
	misLizard = 0
	misyn = 'n'
	misSong = misTitle[simba]
	misNum = misNumber[simba]
	plusMisSong = misSong.replace(' ', '+')
	misQuest = requests.get('https://www.youtube.com/results?sp=EgIQAUIECAESAA%253D%253D&search_query=' + plusArt + '+' + plusMisSong)
	misString = misQuest.text
	misMatch = re.findall('(?<=class=\"yt-lockup-title \"><a href=\")(.*)', misString)
	while misyn != 'y' and misyn != 's' and len(misMatch) > 1:
#		misList = []
		print('Searching...')
#		misSong = misTitle[simba]
#		misNum = misNumber[simba]
#		plusMisSong = misSong.replace(' ', '+')
#		misQuest = requests.get('https://www.youtube.com/results?sp=EgIQAUIECAESAA%253D%253D&search_query=' + plusArt + '+' + plusMisSong)
#		misString = misQuest.text
#		misMatch = re.findall('(?<=class=\"yt-lockup-title \"><a href=\")(.*)', misString)
		misHref = misMatch[misLizard]
		href, rest = misHref.split('\"', 1)
		os.system('youtube-dl --get-title https://www.youtube.com' + href)
		print(misSong)
		misyn = input('good?(y/n/r/s): ')
		misLizard += 1
		if misyn == 's':
			print('Skipping track')
		if misyn == 'r':
			misLizard = 0
	if misNum < 10:
		misBorder = '0' + str(misNum)
	else:
		misBorder = str(misNum)
	shrew = misBorder + '. ' + misSong
	if misyn == 'y':
		print('Downloading and converting ' + shrew)
		os.system('youtube-dl -q -f 18 http://www.youtube.com' + href)
		os.system('ffmpeg -loglevel panic -i *.mp4 -vn -metadata album=\"' + alb + '\" -metadata genre=\"' + gen + '\" -metadata artist=\"' + art + '\" -metadata encoded_by=\"' + enc + '\" -metadata title=\"' + misSong + '\" -metadata track=\"' + misBorder + '\" \"' + shrew + '\".mp3')
		os.system('rm *.mp4')
	snickers -= 1
	simba += 1
#ffmpeg loop
order = 0
ordering = 0
vulture = len(misNumber)
while num3 != 0:
	tgs += 1
	tks += 1
	order += 1
	#no overlapping numbers
	while order == misNumber[ordering]:
		order += 1
		ordering += 1
		vulture -= 1
		if vulture == 0:
			ordering = 0
	if order < 10:
		border = '0' + str(order)
	else:
		border = str(order)
	lp2tgs = tags[tgs]
	lp2tks = tracks[tks]
	new = border + '. ' + lp2tks
	print('Converting ' + new)
	get = 'ffmpeg -loglevel panic -i 000' + lp2tgs + '*.m4a -vn -metadata album=\"' + alb + '\" -metadata genre=\"' + gen + '\" -metadata artist=\"' + art + '\" -metadata encoded_by=\"' + enc + '\" -metadata title=\"' + lp2tks + '\" -metadata track=\"' + border + '\" \"' + new + '\".mp3'
	os.system(get)
	os.system('rm -f 000' + lp2tgs + '*.m4a')
	num3 -= 1
#add art
os.system('rm -f *.m4a')
picFiles = os.listdir()
for picture in picFiles:
	if picture.endswith('.mp3'):
		picList.append(picture)
picLen = len(picList)
print('Adding Art')
while picLen != 0:
	picSong = picList[picNum]
	quoteSong = ('\"' + picSong + '\"')
	newSong = ('0\"' + picSong + '\"')
	os.system('ffmpeg -loglevel panic -i ' + quoteSong + ' -i albumImg.jpg -map_metadata 0 -map 0 -map 1 -acodec copy ' + newSong)
	picNum += 1
	picLen -= 1
os.system('rm *.jpg ??.* songs.txt')
#file away music
os.system('mkdir ' + underArt + '_-_' + underAlb)
os.system('mv *.mp3 ' + underArt + '_-_' + underAlb)
os.system('mv ' + underArt + '_-_' + underAlb + ' ../hold')
os.system('python3 ../docs/sort.py')
#os.system('python3 ../docs/sync.py')
print('Done!')
