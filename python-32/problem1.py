
def text_analysis(text):
    # 1. Count total number of words
    words = text.split()
    total_words = len(words)


    # 2. Count total number of spaces
    total_spaces = text.count(' ')


    # 3. Count frequency of each word
    from collections import Counter
    word_freq = Counter(words)


    # 4. Identify & display top 3 most frequent words
    top_3 = word_freq.most_common(3)


    # 5. Count the number of vowels in the entire text
    vowels = 'aeiouAEIOU'
    vowel_count = sum(1 for char in text if char in vowels)


    # # 6. Sort the string with conversion of original string into reverse ascending order
    # sorted_reversed = ''.join(sorted(text, reverse=True))


    # Display results
    print("Total number of words:", total_words)


    print("Total number of spaces:", total_spaces)


    print("Word frequency:", dict(word_freq))


    print("Top 3 most frequent words:", top_3)


    print("Number of vowels:", vowel_count)


    # print("String sorted in reverse ascending order:", sorted_reversed)

input_text = input("Enter your text: ")
text_analysis(input_text)