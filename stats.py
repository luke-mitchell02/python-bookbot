def get_word_count(book_text) -> int:
    return len(book_text.split())


def count_letter_count(book_text) -> dict:
    characters = {}

    for word in book_text.split():
        for character in word:
            lowercase_char = character.lower()
            if lowercase_char not in characters:
                characters[lowercase_char] = 0
            
            characters[lowercase_char] += 1
    
    return characters