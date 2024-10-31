from quote import quote
import re
from collections import Counter
from typing import List, Tuple, Dict, Any

# Fetch 30 quotes from Edgar Allan Poe using the quote library
def fetch_quotes(author: str, limit: int) -> List[Dict[str, Any]]:
    """
    Fetches quotes from the specified author using the quote library.
    """
    return quote(author, limit=limit)

# Task 1: Inventory of book titles

def extract_titles(quotes_data: List[Dict[str, Any]]) -> List[str]:
    """
    Extracts and returns a list of book titles from the quotes data.
    """
    # titles = [item['book'] for item in quotes_data]
    
    titles = [item['book'] for item in quotes_data if item['book']]
    return titles

def count_and_sort_titles(titles: List[str]) -> List[Tuple[str, int]]:
    """
    Counts the frequency of each title and returns a sorted list of tuples.
    """
    
    title_counts = Counter(titles)
    sorted_titles = title_counts.most_common()
    
    return sorted_titles

# Task 2: Inventory of words

def clean(quotes_data: List[Dict[str, Any]]) -> List[str]:
    """
    Cleans punctuation from quotes and tokenizes them into words.
    """
    
    all_words = []
    for item in quotes_data:
        quote_text = item['quote']
        
        # Remove punctuation using regular expressions
        cleaned_quote = re.sub(r'[^\w\s]', '', quote_text)
        
        # Convert to lowercase and split into words
        words = cleaned_quote.lower().split()
        all_words.extend(words)
        
    return all_words

def count_and_sort_words(words: List[str]) -> List[Tuple[str, int]]:
    """
    Counts the frequency of each word, filters words with frequency >= 5,
    and returns a sorted list of tuples.
    """
    
    word_counts = Counter(words)
    sorted_words = []

    for word, count in word_counts.most_common():
        if count >= 5:
            sorted_words.append((word, count))
    
    return sorted_words

# Main execution
if __name__ == "__main__":
    author_name = "Edgar Allan Poe"
    quote_limit = 30

    # Fetch quotes
    quotes_data = fetch_quotes(author_name, quote_limit)

    # Task 1: Process titles
    titles = extract_titles(quotes_data)
    sorted_title_counts = count_and_sort_titles(titles)

    # Display the sorted titles
    print("Inventory of Book Titles by Frequency:")
    for title, count in sorted_title_counts:
        print(f"{title}: {count}")

    # Task 2: Process words
    words = clean(quotes_data)
    sorted_word_counts = count_and_sort_words(words)

    # Display the sorted words
    print("\nInventory of Words by Frequency (Appear at least 5 times):")
    for word, count in sorted_word_counts:
        print(f"{word}: {count}")