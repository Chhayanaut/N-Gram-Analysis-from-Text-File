import requests #pip install requests
import string

# Function to download the book from a URL and save it to a file
def download_book(url, filename):
    response = requests.get(url)
    if response.status_code == 200:
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(response.text)
        print(f"Book downloaded and saved as {filename}")
    else:
        print("Failed to download the book")

# URL of the book and filename to save it
url = "https://raw.githubusercontent.com/amephraim/nlp/refs/heads/master/texts/J.%20K.%20Rowling%20-%20Harry%20Potter%201%20-%20Sorcerer's%20Stone.txt"
filename = "Sorcerers_Stone.txt"

# Download the book (if you haven't already)
download_book(url, filename)

# Load and preprocess the text: convert to lowercase and remove punctuation
with open(filename, 'r', encoding='utf-8') as f:
    text = f.read().lower()

translator = str.maketrans("", "", string.punctuation)
cleaned_text = text.translate(translator)

# Split the cleaned text into words
words = cleaned_text.split()

# Function to generate n-grams from a list of words
def generate_ngrams(words, n):
    """
    Generate a list of n-grams from the provided list of words.
    Each n-gram is returned as a string of words separated by spaces.
    """
    return [" ".join(words[i:i+n]) for i in range(len(words) - n + 1)]

# Function to count frequencies of n-grams in a list
def count_ngrams(ngrams):
    counts = {}
    for ngram in ngrams:
        counts[ngram] = counts.get(ngram, 0) + 1
    return counts

# Function to get the top N n-grams by frequency
def get_top_ngrams(counts, top_n=5):
    sorted_items = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return sorted_items[:top_n]

# Generate bigrams (2-grams)
bigrams = generate_ngrams(words, 2)
bigram_counts = count_ngrams(bigrams)
top5_bigrams = get_top_ngrams(bigram_counts, 5)

print("Top 5 Bigrams:")
for ngram, count in top5_bigrams:
    print(f"{ngram}: {count}")

# Extra Task: Generalize to N-Grams (for example, trigrams when n = 3)
n = 3  # Change this to any n for n-grams
trigrams = generate_ngrams(words, n)
trigram_counts = count_ngrams(trigrams)
top5_trigrams = get_top_ngrams(trigram_counts, 5)

print("\nTop 5 Trigrams:")
for ngram, count in top5_trigrams:
    print(f"{ngram}: {count}")
