import re

def S_Translation(IN):
	Aminos=\
		{'Ala':['GCT','GCC','GCA','GCG'],\
		 'Arg':['CGT','CGC','CGA','CGG','AGA','AGG'],\
		 'Asn':['AAT','AAC'],\
		 'Asp':['GAT','GAC'],\
		 'Cys':['TGT','TGC'],\
		 'Glu':['GAA','GAG'],\
		 'Gln':['CAA','CAG'],\
		 'Gly':['GGT','GGC','GGA','GGG'],\
		 'His':['CAT','CAC'],\
		 'Ile':['ATT','ATC','ATA'],\
		 'Leu':['TTA','TTG','CTT','CTC','CTA','CTG'],\
		 'Lys':['AAA','AAG'],\
		 'Met(start)':['ATG'],\
		 'Phe':['TTT','TTC'],\
		 'Pro':['CCT','CCC','CCA','CCG'],\
		 'Ser':['TCT','TCC','TCA','TCG','AGT','AGC'],\
		 'Thr':['ACT','ACC','ACA','ACG'],\
		 'Tyr':['TAT','TAC'],\
		 'Trp':['TGG'],\
		 'Val':['GTT','GTC','GTA','GTG'],\
		 'STOP':['TAA','TAG','TGA']}
	Abv_Abv=\
		{'Ala':'A',\
		'Arg':'R',\
		'Asn':'N',\
		'Asp':'D',\
		'Cys':'C',\
		'Glu':'E',\
		'Gln':'Q',\
		'Gly':'G',\
		'His':'H',\
		'Ile':'I',\
		'Leu':'L',\
		'Lys':'K',\
		'Phe':'F',\
		'Pro':'P',\
		'Ser':'S',\
		'Thr':'T',\
		'Tyr':'Y',\
		'Trp':'W',\
		'Val':'V',\
		'Met(start)':'M',\
		'STOP':'*'}
	#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
	#

	# IN = input("Input DNA Sequence for amino acid sequence\n>")

	DNA = IN.upper()

	bp=['A','G','C','T']

	seg=[]         # These rows clean up user input, raises Error if N != a,t,g,c

	aa_seq=[]

	aa_seq_single=[]

	for nt in DNA:
		if nt not in bp:
		   print("ERROR, INPUT SEQUENCE CONTAINED UNIDENTIFIED BASE")
	seg = re.split("([A-Z]{3})", DNA)
	for obj in seg:
		if obj == '':
			seg.remove(obj)
		elif len(obj) < 3:
			seg.remove(obj)
	
	def aa(seg, list):              # <– Matches codon to AA {AA=key,codon=value}   
		for codon in seg:           #   Make Sure the Input(DNA->seg)Loops First{e.g. if "for k, v … " came first, then the final append order would be wrong
			for k, v in Aminos.items():
				if codon in v:
					list.append(k)  #<– directs the AA abrv. to a new list
	aa(seg, aa_seq)                 

	AA = '-'.join(aa_seq)       #<–Links the AA chain with "–"

	def smol_boi(aa_seq, list):
		for Amino in aa_seq:
			for k, v in Abv_Abv.items():
				if Amino == k:
					list.append(v)

	smol_boi(aa_seq, aa_seq_single)

	AA_s = ''.join(aa_seq_single)
	return AA_s
def T_Translation(IN):
	Aminos=\
		{'Ala':['GCT','GCC','GCA','GCG'],\
		 'Arg':['CGT','CGC','CGA','CGG','AGA','AGG'],\
		 'Asn':['AAT','AAC'],\
		 'Asp':['GAT','GAC'],\
		 'Cys':['TGT','TGC'],\
		 'Glu':['GAA','GAG'],\
		 'Gln':['CAA','CAG'],\
		 'Gly':['GGT','GGC','GGA','GGG'],\
		 'His':['CAT','CAC'],\
		 'Ile':['ATT','ATC','ATA'],\
		 'Leu':['TTA','TTG','CTT','CTC','CTA','CTG'],\
		 'Lys':['AAA','AAG'],\
		 'Met(start)':['ATG'],\
		 'Phe':['TTT','TTC'],\
		 'Pro':['CCT','CCC','CCA','CCG'],\
		 'Ser':['TCT','TCC','TCA','TCG','AGT','AGC'],\
		 'Thr':['ACT','ACC','ACA','ACG'],\
		 'Tyr':['TAT','TAC'],\
		 'Trp':['TGG'],\
		 'Val':['GTT','GTC','GTA','GTG'],\
		 'STOP':['TAA','TAG','TGA']}
	Abv_Abv=\
		{'Ala':'A',\
		'Arg':'R',\
		'Asn':'N',\
		'Asp':'D',\
		'Cys':'C',\
		'Glu':'E',\
		'Gln':'Q',\
		'Gly':'G',\
		'His':'H',\
		'Ile':'I',\
		'Leu':'L',\
		'Lys':'K',\
		'Phe':'F',\
		'Pro':'P',\
		'Ser':'S',\
		'Thr':'T',\
		'Tyr':'Y',\
		'Trp':'W',\
		'Val':'V',\
		'Met(start)':'M',\
		'STOP':'*'}
	#–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––
	#

	# IN = input("Input DNA Sequence for amino acid sequence\n>")

	DNA = IN.upper()

	bp=['A','G','C','T']

	seg=[]         # These rows clean up user input, raises Error if N != a,t,g,c

	aa_seq=[]

	aa_seq_single=[]

	for nt in DNA:
		if nt not in bp:
		   print("ERROR, INPUT SEQUENCE CONTAINED UNIDENTIFIED BASE")
	seg = re.split("([A-Z]{3})", DNA)
	for obj in seg:
		if obj == '':
			seg.remove(obj)
		elif len(obj) < 3:
			seg.remove(obj)
	
	def aa(seg, list):              # <– Matches codon to AA {AA=key,codon=value}   
		for codon in seg:           #   Make Sure the Input(DNA->seg)Loops First{e.g. if "for k, v … " came first, then the final append order would be wrong
			for k, v in Aminos.items():
				if codon in v:
					list.append(k)  #<– directs the AA abrv. to a new list
	aa(seg, aa_seq)                 

	AA = '-'.join(aa_seq)       #<–Links the AA chain with "–"

	def smol_boi(aa_seq, list):
		for Amino in aa_seq:
			for k, v in Abv_Abv.items():
				if Amino == k:
					list.append(v)

	smol_boi(aa_seq, aa_seq_single)

	AA_s = ''.join(aa_seq_single)
	return AA
def REVERSE_COMP(IN):
	# IN = input("Enter DNA sequence:" '\n')
	Tev = IN[::-1]
	rev = Tev.upper()
	revcomp = ''
	for nt in rev:
		if nt == 'A':
			revcomp = revcomp + 'T'
		elif nt == 'T':
			revcomp = revcomp + 'A'
		elif nt == 'G':
			revcomp = revcomp + 'C'
		elif nt == 'C':
			revcomp = revcomp + 'G'
		elif nt == 'N':
			revcomp = revcomp + nt
	return revcomp
def FW_TRANSCRIPTION(IN):
	# IN = input("Enter sequence:  " )
	seq = IN.upper()
	NTS = ''
	for nt in seq:
		if nt == 'T':
			NTS = NTS + 'U'
		else:
			NTS = NTS + nt
	return NTS
def RV_TRANSCRIPTION(IN):
	# IN = input("Enter sequence:  " )
	seq = IN.upper()
	NTS = ''
	for nt in seq:
		if nt == 'U':
			NTS = NTS + 'T'
		else:
			NTS = NTS + nt
	return NTS
# def TRIMMER(IN):
# 	NI = str(IN).upper()
# 	preseq = ''
# 	for nt in NI:
# 		if nt == "U":
# 			preseq = preseq + "T"
# 		else:
# 			preseq = preseq + nt
# 	sequence = preseq
# 	import re
# 	start = re.compile("ATG")
# 	search_str = sequence
# 	seqsearch = start.search(search_str)
# 	seqstart = seqsearch.start()
# 	seq = sequence[seqstart:-1]
# 	def trimmed(start, seq):
# 		stops = re.compile("TAA|TAG|TGA")
# 		search_str = seq
# 		matchedEND = stops.search(search_str)
# 		endex = matchedEND.start() + 3
# 		NTS = seq[0:endex]
# 	trimmed(start, seq)
# 	NtS = str(NTS)
# 	return NtS
