import csv
import random


# CSV header
header = ["column1", "column2", "column3", "freetext1", "column5", "freetext2"]


# Make the words list
with open("words.txt") as f:
    words_list = [line.rstrip('\n') for line in f]


def get_n_random_words_list(n):
    """Gets n number of random words from the words list and returns
    a list of those words
    """
    
    num_words = random.randint(1, n)
    text = [
        words_list[random.randint(0, len(words_list) - 1)] for num in range(num_words)
    ]
    return text


def text_for_normal_column():
    """Creates text for a normal column."""

    text = get_n_random_words_list(5)
    print('made normal text: {}'.format(' '.join(text)))
    return ' '.join(text)


def text_for_malformed_column():
    """Creates text for a malformed column.
    Randomly picks if there is a newline or not
    """

    text = get_n_random_words_list(3)

    # Randomly add a \n
    if random.randint(0, 4) == 0:
        text.append("\n")
    
    text += get_n_random_words_list(3)
    print('made malformed text: {}'.format(' '.join(text)))
    return ' '.join(text)


def create_row():
    """Creates 1 row of the csv"""

    row = [
        text_for_normal_column() if 'freetext' not in column else text_for_malformed_column() for column in header
    ]
    return row

with open('example-malformed.csv', 'w') as csv_file:
    example_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    # Write the header
    example_writer.writerow(header)

    # Write 100 rows
    for _ in range(100):
        row = create_row()
        example_writer.writerow(row)
