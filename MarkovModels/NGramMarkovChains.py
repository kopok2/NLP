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

    def most_likely_word(self, word: 'previous word') -> str:
        """
        Get most likely word given previous word from Markov Chains.

        :param word: previous word.
        """
        if word not in self.chains:
            word = random.choice(list(self.chains.keys()))
        words_counts = [val for key, val in self.chains[word].items()]
        mx_count = max(words_counts)
        most_frequent = list(filter((lambda w: self.chains[word][w] == mx_count), self.chains[word].keys()))
        return random.choice(most_frequent)


if __name__ == '__main__':
    mc = MarkovChain()
    text_in = 'Semir dahak semir dahakian semir xd semir xd'.split(" ")
    mc.learn(text_in)
    print(mc.most_likely_word("semir"))
    print(mc.most_likely_word("Sedmir"))
