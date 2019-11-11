# coding=utf-8
"""N-Gram modeling using Markov Chains.

Sentence prediction using Markov Chains module.
"""
import random
from collections import defaultdict


class MarkovChain:
    """Markov Chain N-Gram model learner."""
    def __init__(self):
        self.chains = defaultdict(lambda: defaultdict(int))

    def learn(self, text: 'list of tokens'):
        """
        Learn new text transitions.

        :param text: list of tokens.
        """
        for previous, current in zip(text[:-1], text[1:]):
            self.chains[previous][current] += 1

    def most_likely_word(self, word: 'previous word', threshold=0.25) -> str:
        """
        Get most likely word given previous word from Markov Chains.

        :param threshold: Markov inclusion threshold.
        :param word: previous word.
        """
        if word not in self.chains:
            word = random.choice(list(self.chains.keys()))
        words_counts = [val for key, val in self.chains[word].items()]
        mx_count = max(words_counts)
        most_frequent = list(filter((lambda w: self.chains[word][w] >= mx_count * threshold), self.chains[word].keys()))
        return random.choice(most_frequent)

    def generate_sentence(self, starting_word='___', length=10):
        """
        Generate text from Markov Chains with given starting word and with given length.
        :param starting_word: starting state.
        :param length: result requested length.
        """
        result = []
        current_word = starting_word
        for x in range(length):
            next_word = self.most_likely_word(current_word)
            result.append(next_word)
            current_word = next_word
        return " ".join(result).capitalize() + "."

    def generate_text(self, sentences_count=12):
        """
        Generate text using random length sentences.

        :param sentences_count: number of sentences to be generated
        """
        result = []
        for x in range(sentences_count):
            result.append(self.generate_sentence(length=random.randrange(3, 15)))
        return " ".join(result)

    def learn_text_from_file(self, path):
        """
        Learn Markov Chains from file with given path.

        :param path: source filename.
        """
        for line in open(path):
            words = line.split(" ")
            cleaned = [w.replace(".", "").replace("\n", "").replace(" ", "") for w in words if w and w != ' ']
            self.learn(cleaned)

    def converse(self):
        """
        Enter interactive conversation with Markov Chain model.
        """
        while True:
            in_ = input()
            if in_ == 'Bye':
                break
            else:
                print(self.generate_sentence(starting_word=in_.split(" ")[-1], length=random.randrange(2, 20)))


if __name__ == '__main__':
    print("Markov Chain N-Gram model. 2019 by Karol Oleszek")
    mc = MarkovChain()
    text_in = 'Semir dahak semir dahakian semir xd semir xd'.split(" ")
    mc.learn_text_from_file('out.txt')
    print(mc.generate_text(5))
    mc.converse()
