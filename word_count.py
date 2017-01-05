def wordcount(happy):

	words = happy.split()

	counts = {}
	for word in words:
		counts[word] = counts.get(word, 0) + 1
	
	
	print("The word frecuency of your phrase is: ")
	print(counts)

def main():
	
	happy = input("Enter a phrase to word count: ")
	wordcount(happy)
