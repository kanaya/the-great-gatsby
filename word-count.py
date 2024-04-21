import sys
import re

filename = sys.argv[1]
fp = open(filename)
data = fp.read()
words = data.split()
fp.close()

word_freq = {}
for raw_word in words:
	word = re.sub('[^A-Za-z]', '', raw_word).lower()
	if word not in word_freq:
		word_freq[word] = 0
	word_freq[word] += 1

word_sorted = sorted(word_freq.items(), key=lambda x:x[1], reverse=True)

for word in word_sorted:
	print("{} {}".format(word[1], word[0]))
