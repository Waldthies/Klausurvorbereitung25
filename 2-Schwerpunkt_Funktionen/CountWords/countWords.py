def count_words(text):
    # Convert text to lowercase
    text = text.lower()
    
    # Manually remove punctuation
    punctuation = ".,!?;:"
    for char in punctuation:
        text = text.replace(char, "")
    
    # Split text into words
    words = text.split()
    
    # Count the words
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

def most_frequent_word(word_count):
    # Find the most frequent word
    most_frequent = None
    max_count = 0
    for word, count in word_count.items():
        if count > max_count:
            most_frequent = word
            max_count = count
    return most_frequent, max_count

def alphabetical_words(word_count):
    # Sort words alphabetically
    sorted_words = list(word_count.keys())
    sorted_words.sort()
    return sorted_words

def long_words(word_count, length):
    # Filter words longer than the given length
    long_words_list = []
    for word in word_count:
        if len(word) > length:
            long_words_list.append(word)
    return long_words_list

# Read text from a file
file_path = "shrek_skript.txt"
try:
    with open(file_path, 'r') as file:
        text = file.read()
    
    word_count = count_words(text)
    print("Word count:", word_count)
    print()

    most_frequent = most_frequent_word(word_count)
    print(f"The most frequent word is '{most_frequent[0]}' with {most_frequent[1]} occurrences.")
    print()

    sorted_words = alphabetical_words(word_count)
    print("Words in alphabetical order:", sorted_words)
    print()
    
    long_words_list = long_words(word_count, 4)
    print("Words longer than 4 characters:", long_words_list)
    print()

except FileNotFoundError:
    print(f"The file at {file_path} was not found.")
