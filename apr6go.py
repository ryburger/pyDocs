import os
import requests
import re
artist = input('artist: ')
album = input('album: ')

link = 'https://www.google.com/search?q=' + 'genius+' + artist.replace(' ', '+') + '+' + album.replace(' ', '+') + '&oq=' + 'genius+' + artist.replace(' ', '+') + '+' + album.replace(' ', '+') + '&aqs=chrome..69i57.13775j0j4&client=ms-android-a1-motorola&sourceid=chrome-mobile&ie=UTF-8'
req = requests.get(link)
url = req.text
start = url.find('https://genius.com/albums')
end = (url[start:].find('&amp')) + start
link = (url[start:end])
req = requests.get(link)
url = req.text
end = url.index('.jpg') + 4
start = end - 100
picture = (url[start:end])
if picture.find('https://') != -1:
 junk, picture = picture.split('https://')
 os.system('wget -q https://' + picture)
elif picture.find('http://') != -1:
 junk, picture = picture.split('http://')
 os.system('wget -q http://' + picture)
discography = re.findall('(?<=chart_row-content-title)(.*)', url)
down = ((len(discography)/2))
tracks = []
while down != 0:
 songIndex = url.index('chart_row-content-title')
 url = url[songIndex:]
 songIndex = url.index('<')
 song = (url[:songIndex])
 junk, song = song.split('>')
 song = ' '.join(song.split())
 song = song.replace('\'', '')
 song = song.replace('\"', '')
 song = song.replace(')', '')
 song = song.replace('(', '')
 song = song.replace('&', '')
 song = song.replace('#', 'number ')
 song = song.replace('@', 'at')
 song = song.replace('/', '')
 song = song.replace(':', '')
 song = song.replace('*', '')
 song = song.replace('[', '')
 song = song.replace(']', '')
 song = song.replace('+', '')
 tracks.append(song)
 songIndex += 100
 url = url[songIndex:]
 down -= 1
up = 0
while up != len(tracks):
 tempLink = 'https://www.youtube.com/results?search_query=' + artist.replace(' ', '+') + '+' + tracks[up].replace(' ', '+')
 req = requests.get(tempLink)
 url = req.text
 start = url.find('data-context-item-id=\"')
 end = url[start:].find('data-visibility') + start - 2
 start = url[start:end].find('\"') + start + 1
 subLink = 'https://youtu.be/' + (url[start:end])
 url = url[end:]
 if up+1 < 10:
  numStr = '0' + str(up+1) + '. '
 else:
  numStr = str(up+1) + '. '
 if up > 0 and subLink != 'https://youtu.be/':
  link += ' ' + subLink
  print (numStr + tracks[up])
#  print (subLink)
  up += 1
 elif up < 1 and subLink != 'https://youtu.be/':
  link = subLink
  print (numStr + tracks[up])
#  print (subLink)
  up += 1
link = 'youtube-dl -q -o "%(autonumber)s-%(title)s.%(ext)s" -f 18 ' + link
toast = ('termux-toast Downloading ' + str(len(tracks)) + ' songs:')
os.system(toast)
os.system(link)
total = len(tracks)
tik = total
count = 0
dracula = 1
os.system('termux-toast Converting Music')
while tik != 0:
 if dracula < 10:
  num = '0' + str(dracula)
 else:
  num = str(dracula)
 title = tracks[count]
 unTitle = title.replace(' ', '_') + '.mp3'
# print (num + '. ' + title)
 mp3 = 'ffmpeg -loglevel panic -i ' + '000' + num + '*.mp4 -metadata title=\'' + title + '\'' + ' -metadata artist=\'' + artist + '\'' + ' -metadata album=\'' + album + '\'' + ' -metadata track=\'' + num + '\'' + ' -metadata encoded_by=\'burger\' ' +  unTitle
 os.system(mp3)
 pic = 'ffmpeg -loglevel panic -i ' + unTitle + ' -i *.jpg -map_metadata 0 -map 0 -map 1 -acodec copy ' + num + '.' + unTitle
 os.system(pic)
 count += 1
 dracula += 1
 tik -= 1
 rm = 'rm ' + unTitle
 os.system(rm)
 per = (1 - (tik/total))*100
 toast = str(round(per)) + '% Completed'
 os.system('termux-toast ' + toast)

rm = 'rm *.mp4 *.jpg'
os.system(rm)
mkdir = 'mkdir ' + album.replace(' ', '')
os.system(mkdir)
mv = 'mv *.mp3 ' + album.replace(' ', '')
os.system(mv)
mv = 'mv ' + album.replace(' ', '') + ' hold'
os.system(mv)
