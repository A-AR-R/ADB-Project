from bs4 import BeautifulSoup
from lxml import html


NUM_WORDS = 5000
def convert_raw_table(raw_filename, converted_filename):
    
    with open(raw_filename) as input_file:
        tree = BeautifulSoup(input_file, 'lxml')

    cnt = 0
    for row in tree.find_all('table')[0].tbody.find_all('tr'):
        if cnt == NUM_WORDS + 1:
            extra_rows = [row]
            extra_rows.extend(row.find_all_next())
            break
        fifth_to_end_cols = row.find_all('td')[3].find_next_siblings()
        for col in fifth_to_end_cols:
            col.decompose()
        
        cnt += 1
    for extra_row in extra_rows:
        extra_row.decompose()

    with open(converted_filename, 'w') as output_file:
        output_file.write(str(tree))

def get_length_freq(converted_filename):
    length_freq = {}

    with open(converted_filename) as input_file:
        tree = BeautifulSoup(input_file, 'lxml')
    
    tree.find('tr').decompose()
    max_length_word = ''
    max_length_word_length = len(max_length_word)
    for row in tree.find_all('tr'):
        word = row.find_all('td')[1].string
        word_length = len(word)
        #if word_length > max_length_word_length:
        #    max_length_word = word
        #    max_length_word_length = word_length
        freq = row.find_all('td')[3].string
        if word_length not in length_freq:
            length_freq[word_length] = int(freq)
        else:
            length_freq[word_length] += int(freq)

    #print(max_length_word, '   ' , max_length_word_length)
    return length_freq
