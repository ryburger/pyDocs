#ultimate music download
import os
#constants
art = input('artist:')
alb = input('album:')
gen = input('genre:')
enc = 'burger'
ash = 'sudo youtube-dl -i -f 18 -o \"%(autonumber)s-%(title)s.%(ext)s\" '
htp = 'https://www.youtube.com/playlist?list=PL'
url = input('url:')
num1 = 0
num2 = 0
tgs = -1
tks = -1
#lists
tags = []
tracks = []
#ytdl
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
	get = 'sudo ffmpeg -i 000' + lp2tgs + '*.mp4 -vn -metadata album=\"' + alb + '\" -metadata genre=\"' + gen + '\" -metadata artist=\"' + art + '\" -metadata encoded_by=\"' + enc + '\" -metadata title=\"' + lp2tks + '\" -metadata track=\"' + lp2tgs + '\" ' + new + '.mp3'
	os.system(get)
	os.system('sudo rm 000' + lp2tgs + '*.mp4')
	num2 -= 1
	os.system('/opt/vc/bin/vcgencmd measure_temp')
#file away music
os.system('sudo rm *.mp4')
os.system('sudo mkdir ' + art + '-' + alb)
os.system('sudo mv *.mp3 ' + art + '-' + alb)
os.system('sudo mv ' + art + '-' + alb + ' ../holdingTank')
