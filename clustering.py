# Function to calculate if two strings are "matches"
# Match defined by two sentences that differ by only one word
# Position matters
def comp_sentences(str1, str2):
	str1_idx = 0
	str2_idx = 0
	str1_size = len(str1)
	str2_size = len(str2)

	if str1_size != str2_size:
		return False

	if str1 == str2:
		return False

	count = 0
	
	while (str1_idx < str1_size) and (str2_idx < str2_size):

		if (str1[str1_idx] != str2[str2_idx]):

			# Already found one differing word
			if count != 0:
				return False

			count += 1
			str1_word = str1[str1_idx]
			str2_word = str2[str2_idx]

		str1_idx += 1
		str2_idx += 1

	return True, str1_word, str2_word

input_file = open('test_file.txt', 'r')

strings = input_file.readlines()
input_file.close()

output_file = open("clustering_output.txt", "w")
output_file.write("=====")
timestamps = []
phrases = []

# Store timestamps and phrases
for string in strings:
	timestamp = string[0:19]
	phrase = string[20:]
	timestamps.append(timestamp)
	phrases.append(phrase.rstrip())

length = len(phrases)

# O(N^2) algorithm to check if sentences differ by one word with other
# sentences. Only checks each pair of sentences once
for i in range(length):
	phrase1 = phrases[i]
	
	for j in range(i+1, length):
		phrase2 = phrases[j]
		phrase_comp = comp_sentences(phrase1.split(), phrase2.split())

		if phrase_comp:

			full_phrase1 = timestamps[i] + " " + phrase1
			full_phrase2 = timestamps[j] + " " + phrase2

			output_file.write("\n"+full_phrase1+"\n")
			output_file.write(full_phrase2+"\n")
			output_file.write("The changing word was: " + phrase_comp[1] + ", " + phrase_comp[2]+"\n")

output_file.write("=====")
output_file.close()

