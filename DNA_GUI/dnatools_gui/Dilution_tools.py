import math
norm = 1
m = 10**-3
u = 10**-6
n = 10**-9
# M = mol/L	mM = millimole/L	uM = micromole/L	....
def Known_mol(A,C,D):
	#M1V1=M2V2
	a = float(A)
	c = float(C)
	d = float(D)
	b = (d * c)/a
	return round(b, 4)
def Concentration(mass, volume, MW):
	x = float(mass)
	V = float(volume)
	mw = float(MW)
	#[C] = g/(vol * MW)
	C = x/(V*mw)
	return C
def resuspension(mass, molar_out):
	x = float(mass)
	C = float(molar_out)
	V = x/C
	return V
'''

#### 	HOW WILL I ADJUST FOR UNIT SELECTION?!?!?!?!?!	#####
	
	> MAKE ADJUSTMENT IN GUI CLASS FUNCTION FOR DILUTION TOOLS!!!
	
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

'''
