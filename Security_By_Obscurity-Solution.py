import os
stringX = "password.x.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.a.b.c.d.e.f.g.h.i.j.k.l.m.n.o.p.p.o.n.m.l.k.j.i.h.g.f.e.d.c.b.a.a.b"
i = len(stringX)

#stringY = stringX[0:i]
#cmd = "echo %s"%(stringY)
#os.system(cmd)


while(i >= 10):
	#print(i)
	stringY = stringX[0:i]
	cmd = "7z e %s"%(stringY)
	os.system(cmd)
	i = i - 2

