# Input: Two paragraphs
para1 = input("Enter first paragraph:\n")
para2 = input("Enter second paragraph:\n")



# Function to extract unique words from a paragraph
def get_unique_words(paragraph):
    words = paragraph.lower().split()


    # Remove punctuation from words
    words = [word.strip('.,!?;:"\'()[]{}') for word in words]
    return set(words)



# Get unique words for each paragraph
unique_words_para1 = get_unique_words(para1)
unique_words_para2 = get_unique_words(para2)



# Find common words
common_words = unique_words_para1 & unique_words_para2



# Find total unique words in both paragraphs
total_unique_words = unique_words_para1 | unique_words_para2



print("\nUnique words in Paragraph 1:")
print(unique_words_para1)


print("\nUnique words in Paragraph 2:")
print(unique_words_para2)


print("\nCommon words between both paragraphs:")
print(common_words)


print("\nTotal count of unique words in both paragraphs:", len(total_unique_words))