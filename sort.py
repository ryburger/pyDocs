#move and sort from holdingTank to music
import os
#a-c
os.system('sudo mv ../holdingTank/a* ../holdingTank/b* ../holdingTank/c* ../music/a-c')
yn = 'n'
while yn != 'y':
	os.system('ls ../music/a-c | less')
	mor = input('newArtist(y/n):')
	if mor == 'y':
		dir = input('newArtist:')
		os.system('sudo mkdir ' + dir)
		os.system('sudo mv ' + dir + ' ../music/a-c')
	art = input('enterArtist:')
	alb = input('enterAlbum:')
	os.system('sudo mv ../music/a-c/*' + alb + ' ../music/a-c/' + art)
	os.system('sudo mv ../music/a-c/' + art + '/*' + alb + ' ../music/a-c/' + art + '/' + alb)
	yn = input('quit(y/n):')
#d-f
os.system('sudo mv ../holdingTank/d* ../holdingTank/e* ../holdingTank/f* ../music/d-f')
yn = 'n'
while yn != 'y':
	os.system('ls ../music/d-f | less')
	mor = input('newArtist(y/n):')
	if mor == 'y':
		dir = input('newArtist:')
		os.system('sudo mkdir ' + dir)
		os.system('sudo mv ' + dir + ' ../music/d-f')
	art = input('enterArtist:')
	alb = input('enterAlbum:')
	os.system('sudo mv ../music/d-f/*' + alb + ' ../music/d-f/' + art)
	os.system('sudo mv ../music/d-f/' + art + '/*' + alb + ' ../music/d-f/' + art + '/' + alb)
	yn = input('quit(y/n):')
#g-i
os.system('sudo mv ../holdingTank/g* ../holdingTank/h* ../holdingTank/i* ../music/g-i')
yn = 'n'
while yn != 'y':
	os.system('ls ../music/g-i | less')
	mor = input('newArtist(y/n):')
	if mor == 'y':
		dir = input('newArtist:')
		os.system('sudo mkdir ' + dir)
		os.system('sudo mv ' + dir + ' ../music/g-i')
	art = input('enterArtist:')
	alb = input('enterAlbum:')
	os.system('sudo mv ../music/g-i/*' + alb + ' ../music/g-i/' + art)
	os.system('sudo mv ../music/g-i/' + art + '/*' + alb + ' ../music/g-i/' + art + '/' + alb)
	yn = input('quit(y/n):')
#j-l
os.system('sudo mv ../holdingTank/j* ../holdingTank/k* ../holdingTank/l* ../music/j-l')
yn = 'n'
while yn != 'y':
	os.system('ls ../music/j-l | less')
	mor = input('newArtist(y/n):')
	if mor == 'y':
		dir = input('newArtist:')
		os.system('sudo mkdir ' + dir)
		os.system('sudo mv ' + dir + ' ../music/j-l')
	art = input('enterArtist:')
	alb = input('enterAlbum:')
	os.system('sudo mv ../music/j-l/*' + alb + ' ../music/j-l/' + art)
	os.system('sudo mv ../music/j-l/' + art + '/*' + alb + ' ../music/j-l/' + art + '/' + alb)
	yn = input('quit(y/n):')
#m-o
os.system('sudo mv ../holdingTank/m* ../holdingTank/n* ../holdingTank/o* ../music/m-o')
yn = 'n'
while yn != 'y':
	os.system('ls ../music/m-o | less')
	mor = input('newArtist(y/n):')
	if mor == 'y':
		dir = input('newArtist:')
		os.system('sudo mkdir ' + dir)
		os.system('sudo mv ' + dir + ' ../music/m-o')
	art = input('enterArtist:')
	alb = input('enterAlbum:')
	os.system('sudo mv ../music/m-o/*' + alb + ' ../music/m-o/' + art)
	os.system('sudo mv ../music/m-o/' + art + '/*' + alb + ' ../music/m-o/' + art + '/' + alb)
	yn = input('quit(y/n):')
#p-r
os.system('sudo mv ../holdingTank/p* ../holdingTank/q* ../holdingTank/r* ../music/p-r')
yn = 'n'
while yn != 'y':
	os.system('ls ../music/p-r | less')
	mor = input('newArtist(y/n):')
	if mor == 'y':
		dir = input('newArtist:')
		os.system('sudo mkdir ' + dir)
		os.system('sudo mv ' + dir + ' ../music/p-r')
	art = input('enterArtist:')
	alb = input('enterAlbum:')
	os.system('sudo mv ../music/p-r/*' + alb + ' ../music/p-r/' + art)
	os.system('sudo mv ../music/p-r/' + art + '/*' + alb + ' ../music/p-r/' + art + '/' + alb)
	yn = input('quit(y/n):')
#s-u
os.system('sudo mv ../holdingTank/s* ../holdingTank/t* ../holdingTank/u* ../music/s-u')
yn = 'n'
while yn != 'y':
	os.system('ls ../music/s-u | less')
	mor = input('newArtist(y/n):')
	if mor == 'y':
		dir = input('newArtist:')
		os.system('sudo mkdir ' + dir)
		os.system('sudo mv ' + dir + ' ../music/s-u')
	art = input('enterArtist:')
	alb = input('enterAlbum:')
	os.system('sudo mv ../music/s-u/*' + alb + ' ../music/s-u/' + art)
	os.system('sudo mv ../music/s-u/' + art + '/*' + alb + ' ../music/s-u/' + art + '/' + alb)
	yn = input('quit(y/n):')
#v-z
os.system('sudo mv ../holdingTank/v* ../holdingTank/w* ../holdingTank/x* ../holdingTank/y* ../holdingTank/z* ../music/v-z')
yn = 'n'
while yn != 'y':
	os.system('ls ../music/v-z | less')
	mor = input('newArtist(y/n):')
	if mor == 'y':
		dir = input('newArtist:')
		os.system('sudo mkdir ' + dir)
		os.system('sudo mv ' + dir + ' ../music/v-z')
	art = input('enterArtist:')
	alb = input('enterAlbum:')
	os.system('sudo mv ../music/v-z/*' + alb + ' ../music/v-z/' + art)
	os.system('sudo mv ../music/v-z/' + art + '/*' + alb + ' ../music/v-z/' + art + '/' + alb)
	yn = input('quit(y/n):')
