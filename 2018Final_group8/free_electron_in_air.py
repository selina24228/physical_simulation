from visual import *
ball1 = sphere(pos=vector(-0.5,0,0), radius=0.15,
              color=vector(0.2,0.2,1))
ball2 = sphere(pos=vector(0.5,0,0), radius=0.15,
              color=vector(1,0.2,0.2))
N=15
mass=1
Qn=50
Qp=50
Q=50
cn=1
cp=1
Atoms = []
Ion = []
p = []
d = []
pause = []
last = vec(-0.35,0,0)
px =0
py =0
pz =0
dt=0.1
q=1

for i in range(N):
        next = last+0.05*vector(1,0,0)
        Atoms.append(sphere(pos=next, radius=0.01,
                  color=vector(1,0.2,0.2)))
        Ion.append(sphere(pos=next+vector(0.01,0,0), radius=0.01,
                  color=vector(0.2,0.2,0.2)))
        last = next
        p.append(vector(px,py,pz))
        d.append(0)
        pause.append(0)
E=Qn*Qp*vector(1,0,0)/100000
F=q*E
k=0
judge=0
for j in range(1000):
    rate(50)
    for i in range(N): 
        if pause[i] <= 0:
            Atoms[i].color = vector(1,0.2,0.2)
            Ion[i].color = vector(0.2,0.2,0.2)
            p[i]+=(F*dt)
            Atoms[i].pos = Atoms[i].pos + (p[i]/mass)*dt
            #print((p[i]/mass)*dt)
            d[i]+=(p[i].x/mass)*dt
        else:
            Atoms[i].color = vector(1,1,1)
            Ion[i].color = vector(1,1,1)
            p[i]=vector(0,0,0)
        if d[i] >= 0.05:
            d[i]=d[i]%0.05
            pause[i]=10
        if Atoms[i].pos.x > 0.05*N-0.35:
            Atoms[i].pos=vec(-0.3,0,0)
            if cn>0.2:
                Qn-=1
                Qp-=1
                cn=Qn/Q
                cp=Qp/Q
            else:
                cn=0.2
                cp=0.2
            E=Qn*Qp*vector(1,0,0)/100000
            ball1.color=vector(0.2,0.2,cn)
            ball2.color=vector(cp,0.2,0.2)
    for i in range(N): 
        if pause[i] > 0:
            pause[i] -= 1
