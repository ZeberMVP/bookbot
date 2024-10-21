def sort_on(item):
    return item["num"]


def num_characters(book: str):
    letters = {}

    for letter in book.lower():
        if letter.isalpha():
            letters[letter] = letters.get(letter, 0) + 1

    listOfLetters = [{"letter": key, "num": value} for key, value in letters.items()]

    listOfLetters.sort(reverse=True, key=sort_on)

    return listOfLetters


def main():
    with open("books/frankenstein.txt", "r") as book:
        sorted_letters = num_characters(book.read())
        for item in sorted_letters:
            print(f"The '{item['letter']}' character was found {item['num']} times")


if __name__ == "__main__":
    main()
