from vpython import *
#GlowScript 3.2 VPython

scene = canvas(background=color.white)

#constants
k = 9e9
c = 1.6021766e-19

#malleable constants
r = .04 #radius of electron from nucleus
rev = 1.83 #number of electron revolutions around nucleus

#particle masses (adjustments here will adjust the charges accordingly)
nmass = 0
pmass = 1.6726219e-27
emass = 9.1093835e-31
echarge = c*emass/9.10938356e-31
pcharge = c*pmass/1.6726219e-27
evel = c/sqrt((1/k)*r*emass)    

#scalars
vscale = .1*r/evel #scales for default vectors
escale = 1e6*r/evel #scales for placed vectors 

#initiaties particles
nucleus = sphere(pos = vector(0,0,0), radius = 0.03*r, velocity = vector(0,0,0), mass = pmass+nmass, charge = pcharge, color = color.red)
electron = sphere(pos = vector(r,0,0), radius = 0.01*r, velocity = vector(0,evel,0), mass = emass, charge = echarge, color = color.yellow)

#default electric field vectors - commented out since these crowd the simulation
#earrow = [arrow(pos = electron.pos, axis = vscale*vector(0,evel,0), color = color.yellow), arrow(pos = electron.pos, axis = vscale*vector(0,-evel,0), color = color.yellow), 
#arrow(pos = electron.pos, axis = vscale*vector(evel,0,0), color = color.yellow), arrow(pos = electron.pos, axis = vscale*vector(-evel,0,0), color = color.yellow), 
#arrow(pos = electron.pos, axis = vscale*vector(evel/sqrt(2),evel/sqrt(2),0), color = color.yellow), arrow(pos = electron.pos, axis = vscale*vector(-evel/sqrt(2),evel/sqrt(2),0), color = color.yellow), 
#arrow(pos = electron.pos, axis = vscale*vector(evel/sqrt(2),-evel/sqrt(2),0), color = color.yellow), arrow(pos = electron.pos, axis = vscale*vector(-evel/sqrt(2),-evel/sqrt(2),0), color = color.yellow)]
#reorient default vectors
#for i in range(len(earrow)):
#    earrow[i].rotate(angle = pi, axis = vector(0,0,-1), origin = electron.pos)
#narrow = [arrow(pos = nucleus.pos, axis = vscale*vector(0,evel,0), color = color.red), arrow(pos = nucleus.pos, axis = vscale*vector(0,-evel,0), color = color.red), 
#arrow(pos = nucleus.pos, axis = vscale*vector(evel,0,0), color = color.red), arrow(pos = nucleus.pos, axis = vscale*vector(-evel,0,0), color = color.red), 
#arrow(pos = nucleus.pos, axis = vscale*vector(evel/sqrt(2),evel/sqrt(2),0), color = color.red), arrow(pos = nucleus.pos, axis = vscale*vector(-evel/sqrt(2),evel/sqrt(2),0), color = color.red), 
#arrow(pos = nucleus.pos, axis = vscale*vector(evel/sqrt(2),-evel/sqrt(2),0), color = color.red), arrow(pos = nucleus.pos, axis = vscale*vector(-evel/sqrt(2),-evel/sqrt(2),0), color = color.red)]

#description
print("Model of an eletron's movement around a nucleus with an interactive display of electric field vectors.")
print("\nValues relevant to electron movement: ")
print("Radius = ",r, "m")
print("Electron Velocity = ", evel, "m/s")
print("\nValues relevant to electric field generation: ")
print("Electron Charge = ", echarge, "C")
print("Proton Charge = ", pcharge, "C")
print("\nThe yellow arrows represent the electron's electric field.")
print("The red arrows represent the nucleus's electric field.")
print("Click on the simulation to find the electric field at a location (represented by a blue vector).")
print("Charge values (and default electric field values) can be altered by inputting the desired proton, neutron, and electron masses.")

#calculates electron movement
def acc():
  dr = electron.pos - nucleus.pos
  f = k*norm(dr)*-(c**2)/(mag(dr)**2)
  return f/emass

#sets time frame for loop
t = 0
dt = (2.*pi*r/evel)/1000.

#displays electron movement
while (t<(rev*2.)*pi*r/evel):
  rate(500)
  electron.velocity = electron.velocity + acc()*dt
  electron.pos = electron.pos + electron.velocity*dt
  t = t+dt
#  for i in range(len(earrow)):
#      earrow[i].pos = electron.pos + electron.velocity*dt

#displays the system's electric field vector where clicked
def showVector(evt):
    loc = evt.pos
    ed = loc-electron.pos
    pd = loc-nucleus.pos
    Et = k*c*norm(ed)/mag(ed)**2
    Pt = k*c*norm(pd)/mag(pd)**2
    arrow(pos = loc, axis = escale*(Pt-Et), color = color.blue)

scene.bind('click', showVector)