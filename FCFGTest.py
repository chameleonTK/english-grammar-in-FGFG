import nltk
from nltk import FeatureChartParser

fcfg = nltk.data.load('P2.fcfg')
parser = FeatureChartParser(fcfg)

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def parse_text(text, expected):
	examples = text.splitlines()
	for sent in examples:
		print(sent)
		parses = parser.parse(sent.split())
		p = list(parses)
		# print(p)
		if (len(p) > 0 and expected) or (len(p) == 0 and (not expected)):
			print(bcolors.OKGREEN + "Pass" + bcolors.ENDC)
		else:
			print(bcolors.FAIL + "Fail" + bcolors.ENDC)
			for pp in p:
				print(pp)

		# for tree in parses:
		# 	print(tree)

def parse_file(name, expected):
	f = open(name, 'r')
	text = f.read()
	f.close()
	parse_text(text, expected)

print("================ Positive examples ================")
parse_file('P2.pos', True)
print("================ Negative examples ================")
parse_file('P2.neg', False)