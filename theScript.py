import nltk
import operator


# def getNounFreqMap():
# 	f = open("freq.txt", "r")
# 	f.readline()

# 	nounFrequency = dict()
# 	for line in f:
# 		attributes = line.split()
# 		rank = attributes[0]
# 		word = attributes[1]
# 		wordType = attributes[2]
# 		freq = attributes[3]
# 		dispersion = attributes[4]
# 		if wordType == 'n':
# 			nounFrequency[word] = freq

# 	return nounFrequency

# def getFreqMap():
# 	f = open("20k.txt", "r")

# 	nounFrequency = dict()
# 	counter = 0
# 	for word in f:
# 		counter += 1
# 		nounFrequency[word.strip("\n!@#$%^&*()-_=+[]{}<>,.?;:'\"\\")] = counter

# 	return nounFrequency

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
				# print word + " " + str(nounFrequencyMap[word])

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
	# print nltk.pos_tag(open("sample.txt", "r").read())

	# nounFrequencyMap = getNounFreqMap()
	# nounFrequencyMap = getFreqMap()
	frequencyMap = getBigFreqMap()

	filename = "sample.txt"
	keywords = genKeyWords(frequencyMap, filename)
	print "Keywords found:"
	print keywords
	# for word in keywords:
	# 	print word
	# keywords = genKeyWords(nounFrequencyMap)
	# keywords_sorted = sorted(keywords.items(), key = operator.itemgetter(1), reverse = True)
	# MAX_KEYWORDS = 50

	# for word in keywords_sorted

	# keywords_sorted = sorted(keywords.items(), key = operator.itemgetter(1))
	# for word in keywords_sorted:
	# 	print word# + " " + str(keywords[frequency])
	# print "there are " + str(len(keywords)) + " matched words"


	# for word, frequency in nounFrequencyMap.iteritems():
	# 	print word + " " + str(frequency)
	# print "There is a total of " + str(len(nounFrequencyMap)) + " nouns."

main()