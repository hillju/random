import sys
import re


def update_word_frequency(word_frequency, words, sentence_num):
    for word in words:
        # Ignore empty strings, if the previous splitting included them
        if len(word) == 0:
            continue
        word_lc = word.lower()
        if word_lc in word_frequency:
            occur_dict = word_frequency[word_lc]
            occur_dict['num'] += 1
            occur_dict['sentences'] += ',{}'.format(sentence_num)
        else:
            word_frequency[word_lc] = {
                'num': 1,
                'sentences': '{}'.format(sentence_num)
            }


def find_word_frequency(word_frequency, text):
    sentence_num = 1
    # Split on any "." or "?" that is followed by a capital letter
    # Sub out the match with a '.*', so we don't lose the capital letter in the split
    temp_str = re.sub(r'[.?]\W*([A-Z])', '.*\\1', text)
    sentences = re.split(r'\.\*|[.?]$', temp_str)
    for sentence in sentences:
        # Don't split on "." or "'", so we keep abbreviations and concat
        words = re.split(r'[^.\'\w]', sentence)
        update_word_frequency(word_frequency, words, sentence_num)
        sentence_num += 1


def print_word_frequency(word_frequency):
    sorted_words = sorted(word_frequency.keys())
    for word in sorted_words:
        padding = ' ' * (20 - len(word))
        frequency = word_frequency[word]['num']
        sentence_nums = word_frequency[word]['sentences']
        print('{}{}{{{}:{}}}'.format(word, padding, frequency, sentence_nums))


def main(args):
    filename = args[1]
    word_frequency = {}

    with open(filename) as f:
        text = f.read()
        find_word_frequency(word_frequency, text)

    print_word_frequency(word_frequency)


if __name__ == '__main__':
    main(sys.argv)
