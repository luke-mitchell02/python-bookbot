import sys

from stats import get_word_count, count_letter_count

def get_book_text(filepath) -> dict:
    with open(filepath) as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    print("============ BOOKBOT ============")
    book_path = sys.argv[1]
    print(f"Analyzing book found at {book_path}...")
    book_content = get_book_text(book_path)
    num_words = get_word_count(book_content)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    print("--------- Character Count -------")
    letter_count = count_letter_count(book_content)
    
    for i in sorted(letter_count, reverse=True, key=letter_count.get):
        val = letter_count[i]
        print(f"{i}: {val}")


main()