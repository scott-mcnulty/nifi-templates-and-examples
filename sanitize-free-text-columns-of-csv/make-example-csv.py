import csv
import random


# CSV header
header = ["column1", "column2", "column3", "freetext1", "column5", "freetext2"]

# Words
with open("words.txt") as f:
    words_list = [line.rstrip('\n') for line in f]

def text_for_normal_column():

    num_words = random.randint(1, 5)
    text = [
        words_list[random.randint(0, len(words_list) - 1)] for num in range(num_words)
    ]

    print('made normal text: {}'.format(' '.join(text)))
    return ' '.join(text)

def text_for_malformed_column():
    """Creates text for a malformed column.
    Randomly picks if there is a newline or not
    """

    num_words = random.randint(1, 3)
    text = [
        words_list[random.randint(0, len(words_list) - 1)] for num in range(num_words)
    ]

    # Randomly add a \n
    if random.randint(0, 4) == 0:
        text.append("\n")
    

    num_words = random.randint(1, 3)
    text += [
        words_list[random.randint(0, len(words_list) - 1)] for num in range(num_words)
    ]

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
