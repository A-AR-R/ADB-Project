from keyword_utilities import convert_raw_table, get_length_freq
import numpy as np
import string

RAW_FILENAME = 'RawWords.html'
FREQ_FILENAME = 'WordsFreq.html'
NUM_KEYWORDS = 1000000

convert_raw_table(RAW_FILENAME, FREQ_FILENAME)
length_freq_dict = get_length_freq(FREQ_FILENAME)
freq_list = list(length_freq_dict.values())
length_list = list(length_freq_dict.keys())
total_freq = sum(freq_list)

length_probability = []
keywords = []
for freq in freq_list:
    length_probability.append(freq / total_freq)
gen_lenghts = np.random.choice(length_list, NUM_KEYWORDS, p = length_probability)
for gen_length in gen_lenghts:
    
    keywords.append(''.join(np.random.choice(list(string.ascii_lowercase)) for x in range(gen_length)) + '\n')
with open('keywords', 'w') as keywords_file:
        keywords_file.writelines(keywords)

