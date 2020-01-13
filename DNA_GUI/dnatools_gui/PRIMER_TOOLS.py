import math, statistics
from decimal import Decimal
one={'AA':['-9.1', '-0.0240'],
'TT':['-9.1', '-0.0240'],
'AT':['-8.6', '-0.0239'], 
'TA':['-6.0', '-0.0169'],
'CA':['-5.8', '-0.0129'],
'GT':['-6.5', '-0.0173'],
'CT':['-7.8', '-0.0208'],
'GA':['-5.6', '-0.0135'],
'CG':['-11.9', '-0.0278'],
'GC':['-11.1', '-0.0267'],
'GG':['-11.0', '-0.0266'],
'CC':['-11.0', '-0.0266'],
'AC':['-6.5', '-0.0173'],
'AG':['-7.8', '-0.0208'],
'TC':['-5.6', '-0.0135'],
'TG':['-5.8', '-0.0129']}

def l_nearneigh(x, C, NA):
	R = 0.00199 # gas constant of 0.00199 kcal K-1 ᐧ mol-1 (constant that scales energy to temperature)
	A = -0.0108 # Constant (kcal K-1 ᐧ mol-1) for Helix initiations when annealing
	con = C * 10**-6
	q = con/4
	Na = NA/1000
	X = x.replace(" ","")
	seq = X.upper()
	BP_len = len(seq)
	Gcount = seq.count('G')
	Ccount = seq.count('C')
	Tcount = seq.count('T')
	Acount = seq.count('A')
	Gc = ((Gcount + Ccount)/len(seq))*100
	GC = round(Gc, 1)
	# approx_MW = (len(seq)*308.7) - 57
	Mw = (Acount * 313.2) + (Tcount * 304.2) + (Ccount * 289.2) + (Gcount * 329.2) - 61.94
	MW = round(Mw, 1)
	a = [seq[i] for i in range(0, len(seq), 3)]
	b = [seq[i] for i in range(1, len(seq), 3)]
	c = [seq[i] for i in range(2, len(seq), 3)]
	d = [seq[i] for i in range(3, len(seq), 3)]
	ab = [i + j for i, j in zip(a, b)] 
	bc = [i + j for i, j in zip(b, c)] 
	cd = [i + j for i, j in zip(c, d)] 
	paired_seq = ab + bc + cd
	H = []
	S = []
	for K in one:
		for item in paired_seq:
			if item == K:
				H.append(one[K][0])
				S.append(one[K][1])
	delta_H = list(map(float, H))
	delta_S = list(map(float, S))
	dH = sum(delta_H)
	dS = sum(delta_S) ############ NOW NEED TO ADD TM FORMULA!!
	TM = (dH)/((A) + (dS) + (R)*math.log(q)) - 273.15 +( 16.6*(math.log(Na,10)))
	Tm = round(TM, 2)
	TA = Tm - 5
	return f"nt length:   {BP_len}                GC%:   {GC}            Molecular Weight:    {MW} g/mol\n\nTM(celsius): {Tm}\n\nAnnealing Temp. recommendation: {TA}"

def s_nearneigh(x, C, NA):
	R = 0.00199 # gas constant of 0.00199 kcal K-1 ᐧ mol-1 (constant that scales energy to temperature)
	A = -0.0108 # Constant (kcal K-1 ᐧ mol-1) for Helix initiations when annealing
	con = C * 10**-6
	q = con/4
	Na = NA/1000
	seq = x.upper()
	BP_len = len(seq)
	Gcount = seq.count('G')
	Ccount = seq.count('C')
	Tcount = seq.count('T')
	Acount = seq.count('A')
	Gc = ((Gcount + Ccount)/len(seq))*100
	GC = round(Gc, 1)
	# approx_MW = (len(seq)*308.7) - 57
	Mw = (Acount * 313.2) + (Tcount * 304.2) + (Ccount * 289.2) + (Gcount * 329.2) - 61.94
	MW = round(Mw,1)
	a = [seq[i] for i in range(0, len(seq), 3)]
	b = [seq[i] for i in range(1, len(seq), 3)]
	c = [seq[i] for i in range(2, len(seq), 3)]
	d = [seq[i] for i in range(3, len(seq), 3)]
	ab = [i + j for i, j in zip(a, b)] 
	bc = [i + j for i, j in zip(b, c)] 
	cd = [i + j for i, j in zip(c, d)] 
	paired_seq = ab + bc + cd
	H = []
	S = []
	for K in one:
		for item in paired_seq:
			if item == K:
				H.append(one[K][0])
				S.append(one[K][1])
	delta_H = list(map(float, H))
	delta_S = list(map(float, S))
	dH = sum(delta_H)
	dS = sum(delta_S) ############ NOW NEED TO ADD TM FORMULA!!
	TM = (2*(Acount+Tcount) + (Gcount+Ccount)*4) + 16.6*(math.log(Na,10)) - 16.6*(math.log(0.05,10))
	Tm = round(TM, 2)
	TA = Tm - 5
	return f"nt length:   {BP_len}                GC%:   {GC}            Molecular Weight:    {MW} g/mol\n\nTM(celsius): {Tm}\n\nAnnealing Temp. recommendation: {TA}"

#TM and Nearest Neighbor citations:
#Freier SM, Kierzek R, Jaeger JA, Sugimoto N, Caruthers MH, Neilson T, & Turner DH (1986). Improved free-energy parameters for predictions of RNA duplex stability. Proc Natl Acad Sci, 83, 9373-9377.
#Breslauer KJ, Frank R, Blocker H, & Marky LA (1986). Predicting DNA duplex stability from the base sequence. Proc Natl Acad Sci, 83, 3746-3750.