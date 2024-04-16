import unittest
import src.concordance as concordance


class TestConcordance(unittest.TestCase):
    def test_with_text_1(self):
        word_frequency = {}
        with open('test1.txt') as f:
            text = f.read()
            concordance.find_word_frequency(word_frequency, text)

        assert 'i.e.' in word_frequency
        assert 'appeared.' not in word_frequency
        assert 'bonus' in word_frequency
        assert word_frequency['word']['num'] == 3
        assert word_frequency['word']['sentences'] == '1,1,2'

    def test_with_text_2(self):
        word_frequency = {}
        with open('test2.txt') as f:
            text = f.read()
            concordance.find_word_frequency(word_frequency, text)

        assert 'text' in word_frequency
        assert 'it\'s' in word_frequency
        assert 'double' in word_frequency
        assert 'more' in word_frequency
        assert word_frequency['it']['num'] == 2


if __name__ == '__main__':
    unittest.main()
