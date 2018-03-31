#sorts from holdingTank to music
import os
#a-c
aclist = []
acfiles = os.listdir('/media/usbDrive/holdingTank')
for ac in acfiles:
	if ac.startswith('a') or ac.startswith('b') or ac.startswith('c'):
		aclist.append(ac)
aclen = len(aclist)
while aclen > 0:
	os.system('sudo mv ../holdingTank/a* ../music/a-c')
	os.system('sudo mv ../holdingTank/b* ../music/a-c')
	os.system('sudo mv ../holdingTank/c* ../music/a-c')
	os.system('ls ../music/a-c | less')
	acnew = input('newArtist?(n/artistName):')
	if acnew != 'n':
		os.system('sudo mkdir ../music/a-c/' + acnew)
	acart = input('(re)enterArtist:')
	acalb = input('enterAlbum:')
	os.system('sudo mv ../music/a-c/*-' + acalb + ' ../music/a-c/' + acart)
	os.system('sudo mv ../music/a-c/' + acart + '/*-' + acalb + ' ../music/a-c/' + acart + '/' + acalb)
	aclen -= 1

#d-f
dflist = []
dffiles = os.listdir('/media/usbDrive/holdingTank')
for df in dffiles:
	if df.startswith('d') or df.startswith('e') or df.startswith('f'):
		dflist.append(df)
dflen = len(dflist)
while dflen > 0:
	os.system('sudo mv ../holdingTank/d* ../music/d-f')
	os.system('sudo mv ../holdingTank/e* ../music/d-f')
	os.system('sudo mv ../holdingTank/f* ../music/d-f')
	os.system('ls ../music/d-f | less')
	dfnew = input('newArtist?(n/artistName):')
	if dfnew != 'n':
		os.system('sudo mkdir ../music/d-f/' + dfnew)
	dfart = input('(re)enterArtist:')
	dfalb = input('enterAlbum:')
	os.system('sudo mv ../music/d-f/*-' + dfalb + ' ../music/d-f/' + dfart)
	os.system('sudo mv ../music/d-f/' + dfart + '/*-' + dfalb + ' ../music/d-f/' + dfart + '/' + dfalb)
	dflen -= 1

#g-i
gilist = []
gifiles = os.listdir('/media/usbDrive/holdingTank')
for gi in gifiles:
	if gi.startswith('g') or gi.startswith('h') or gi.startswith('i'):
		gilist.append(gi)
gilen = len(gilist)
while gilen > 0:
	os.system('sudo mv ../holdingTank/g* ../music/g-i')
	os.system('sudo mv ../holdingTank/h* ../music/g-i')
	os.system('sudo mv ../holdingTank/i* ../music/g-i')
	os.system('ls ../music/g-i | less')
	ginew = input('newArtist?(n/artistName):')
	if ginew != 'n':
		os.system('sudo mkdir ../music/g-i/' + ginew)
	giart = input('(re)enterArtist:')
	gialb = input('enterAlbum:')
	os.system('sudo mv ../music/g-i/*-' + gialb + ' ../music/g-i/' + giart)
	os.system('sudo mv ../music/g-i/' + giart + '/*-' + gialb + ' ../music/g-i/' + giart + '/' + gialb)
	gilen -= 1

#j-l
jllist = []
jlfiles = os.listdir('/media/usbDrive/holdingTank')
for jl in jlfiles:
	if jl.startswith('j') or jl.startswith('k') or jl.startswith('l'):
		jllist.append(jl)
jllen = len(jllist)
while jllen > 0:
	os.system('sudo mv ../holdingTank/j* ../music/j-l')
	os.system('sudo mv ../holdingTank/k* ../music/j-l')
	os.system('sudo mv ../holdingTank/l* ../music/j-l')
	os.system('ls ../music/j-l | less')
	jlnew = input('newArtist?(n/artistName):')
	if jlnew != 'n':
		os.system('sudo mkdir ../music/j-l/' + jlnew)
	jlart = input('(re)enterArtist:')
	jlalb = input('enterAlbum:')
	os.system('sudo mv ../music/j-l/*-' + jlalb + ' ../music/j-l/' + jlart)
	os.system('sudo mv ../music/j-l/' + jlart + '/*-' + jlalb + ' ../music/j-l/' + jlart + '/' + jlalb)
	jllen -= 1

#m-o
molist = []
mofiles = os.listdir('/media/usbDrive/holdingTank')
for mo in mofiles:
	if mo.startswith('m') or mo.startswith('n') or mo.startswith('o'):
		molist.append(mo)
molen = len(molist)
while molen > 0:
	os.system('sudo mv ../holdingTank/m* ../music/m-o')
	os.system('sudo mv ../holdingTank/n* ../music/m-o')
	os.system('sudo mv ../holdingTank/o* ../music/m-o')
	os.system('ls ../music/m-o | less')
	monew = input('newArtist?(n/artistName):')
	if monew != 'n':
		os.system('sudo mkdir ../music/m-o/' + monew)
	moart = input('(re)enterArtist:')
	moalb = input('enterAlbum:')
	os.system('sudo mv ../music/m-o/*-' + moalb + ' ../music/m-o/' + moart)
	os.system('sudo mv ../music/m-o/' + moart + '/*-' + moalb + ' ../music/m-o/' + moart + '/' + moalb)
	molen -= 1

#p-r
prlist = []
prfiles = os.listdir('/media/usbDrive/holdingTank')
for pr in prfiles:
	if pr.startswith('p') or pr.startswith('q') or pr.startswith('r'):
		prlist.append(pr)
prlen = len(prlist)
while prlen > 0:
	os.system('sudo mv ../holdingTank/p* ../music/p-r')
	os.system('sudo mv ../holdingTank/q* ../music/p-r')
	os.system('sudo mv ../holdingTank/r* ../music/p-r')
	os.system('ls ../music/p-r | less')
	prnew = input('newArtist?(n/artistName):')
	if prnew != 'n':
		os.system('sudo mkdir ../music/p-r/' + prnew)
	prart = input('(re)enterArtist:')
	pralb = input('enterAlbum:')
	os.system('sudo mv ../music/p-r/*-' + pralb + ' ../music/p-r/' + prart)
	os.system('sudo mv ../music/p-r/' + prart + '/*-' + pralb + ' ../music/p-r/' + prart + '/' + pralb)
	prlen -= 1
#s-u
sulist = []
sufiles = os.listdir('/media/usbDrive/holdingTank')
for su in sufiles:
	if su.startswith('s') or su.startswith('t') or su.startswith('u'):
		sulist.append(su)
sulen = len(sulist)
while sulen > 0:
	os.system('sudo mv ../holdingTank/s* ../music/s-u')
	os.system('sudo mv ../holdingTank/t* ../music/s-u')
	os.system('sudo mv ../holdingTank/u* ../music/s-u')
	os.system('ls ../music/s-u | less')
	sunew = input('newArtist?(n/artistName):')
	if sunew != 'n':
		os.system('sudo mkdir ../music/s-u/' + sunew)
	suart = input('(re)enterArtist:')
	sualb = input('enterAlbum:')
	os.system('sudo mv ../music/s-u/*-' + sualb + ' ../music/s-u/' + suart)
	os.system('sudo mv ../music/s-u/' + suart + '/*-' + sualb + ' ../music/s-u/' + suart + '/' + sualb)
	sulen -= 1

#v-z
vzlist = []
vzfiles = os.listdir('/media/usbDrive/holdingTank')
for vz in vzfiles:
	if vz.startswith('v') or vz.startswith('w') or vz.startswith('x') or vz.startswith('y') or vz.startswith('z'):
		vzlist.append(vz)
vzlen = len(vzlist)
while vzlen > 0:
	os.system('sudo mv ../holdingTank/v* ../music/v-z')
	os.system('sudo mv ../holdingTank/w* ../music/v-z')
	os.system('sudo mv ../holdingTank/x* ../music/v-z')
	os.system('sudo mv ../holdingTank/y* ../music/v-z')
	os.system('sudo mv ../holdingTank/z* ../music/v-z')
	os.system('ls ../music/v-z | less')
	vznew = input('newArtist?(n/artistName):')
	if vznew != 'n':
		os.system('sudo mkdir ../music/v-z/' + vznew)
	vzart = input('(re)enterArtist:')
	vzalb = input('enterAlbum:')
	os.system('sudo mv ../music/v-z/*-' + vzalb + ' ../music/v-z/' + vzart)
	os.system('sudo mv ../music/v-z/' + vzart + '/*-' + vzalb + ' ../music/v-z/' + vzart + '/' + vzalb)
	vzlen -= 1

