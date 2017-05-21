import operator

def getBigFreqMap():
	f = open("bigFreq.txt", "r")
	f.readline()

	nounFrequency = dict()
	for line in f:
		attributes = line.split()
		word = attributes[0]
		rank = int(attributes[1])
		nounFrequency[word] = rank

	return nounFrequency

def genKeyWords(nounFrequencyMap, filename):
	f = open(filename, "r")

	keywords = dict()
	for line in f:
		words = line.split()
		for word in words:
			if word in nounFrequencyMap:
				keywords[word] = nounFrequencyMap[word]
	keywords_sorted = sorted(keywords.items(), key = operator.itemgetter(1), reverse = False)
	MAX_KEYWORDS = 100

	keywords_short = list()
	counter = 0
	for word in keywords_sorted:
		keywords_short.append(word[0])
		counter += 1
		if counter == MAX_KEYWORDS:
			break;

	return keywords_short


def main():
	frequencyMap = getBigFreqMap()

	filename = "sample.txt"
	keywords = genKeyWords(frequencyMap, filename)
	print "Keywords found:"
	print keywords

main()