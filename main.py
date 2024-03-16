import operator
def word_count(text):
    text = text.split()
    words = len(text)
    return words


def letter_count_report(letter_counts):
    sort = []
    for k, v in letter_counts.items():
        sort.append({"letter": k, "count": v})
    sort.sort(reverse=True, key=operator.itemgetter('count'))
    for item in sort:
        print(f"The letter '{item['letter']}' appears {item['count']} times in the text.")


def letter_count(text):
    entries = [[chr(x), 0] for x in range(ord("a"), ord("z") + 1)]
    counts = {k: v for k, v in entries}
    letters = [chr(x) for x in range(ord("a"), ord("z") + 1)]

    text = text.split()

    for word in text:
        word = word.lower()

        for letter in word:
            if letter in letters:
                counts[letter] += 1

    return counts


def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()

        print(file_contents)
        count = word_count(file_contents)
        print(f"Word Count: {count}")
        letter_counts = letter_count(file_contents)
        letter_count_report(letter_counts)


main()
