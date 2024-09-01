def count_word_frequencies(text):
    # Convert the text to lowercase to ensure case-insensitive counting
    text = text.lower()

    # Split the text into words using spaces and remove any extra punctuation
    words = [word.strip('.,!?;"\'()[]{}') for word in text.split()]

    # Use a dictionary comprehension to count the frequency of each word
    word_freq = {word: words.count(word) for word in words if word}

    return word_freq


def display_word_frequencies(word_freq):
    if not word_freq:
        print("No words to display. The text was empty or contained only punctuation.")
    else:
        print("\n--- Word Frequencies ---")
        for word, freq in word_freq.items():
            print(f"{word}: {freq}")


if __name__ == "_main_":
    # Sample text input
    text = input("Enter a text: ").strip()

    # Handle edge case where the input text is empty
    if not text:
        print("No text entered.")
    else:
        # Count the word frequencies
        word_frequencies = count_word_frequencies(text)

        # Display the word frequencies
        display_word_frequencies(word_frequencies)