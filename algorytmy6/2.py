import string
from collections import Counter

class Node:
    def __init__(self, word, prob, left=None, right=None):
        self.word = word
        self.prob = prob
        self.left = left
        self.right = right
        self.code = ''


def remove_non_letters(text):
    allowed_characters = string.ascii_letters+' '
    matching_characters = filter(lambda char: char in allowed_characters, text)
    return ''.join(matching_characters)


def get_words_probability(text):
    text = remove_non_letters(text)
    words = text.split(' ')
    words = list(map(str.lower, words))
    data = dict(Counter(words))

    unique_words = []
    probabilities = []
    for word, occurence in data.items():
        unique_words.append(word)
        probabilities.append(occurence / len(words))

    #for i in range(len(probabilities)):
        #print(unique_words[i])
        #print(probabilities[i])
    return unique_words, probabilities


def huffman_encode(text):
    def _fill_codes(node, words_fill, codes_fill, code=''):
        new_code = code + str(node.code)

        if node.left:
            _fill_codes(node.left, words_fill, codes_fill, new_code)

        if node.right:
            _fill_codes(node.right, words_fill, codes_fill, new_code)

        if not node.left and not node.right:
            codes_fill.append(new_code)
            words_fill.append(node.word)

    words, probabilities = get_words_probability(text)

    zipped = list(zip(words, probabilities))

    nodes = [Node(word, prob) for word, prob in zipped]

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.prob)

        left, right = nodes[0], nodes[1]
        left.code, right.code = 0, 1

        new_word = left.word + right.word
        new_prob = left.prob + right.prob
        new_node = Node(new_word, new_prob, left, right)

        nodes.remove(left)
        nodes.remove(right)
        nodes.append(new_node)

    huffman_tree, = nodes

    words_fill = []
    codes_fill = []
    _fill_codes(huffman_tree, words_fill, codes_fill)
    print(words_fill)
    print(codes_fill)

    _words = []
    for word in remove_non_letters(text).split(' '):
        if word:
            _words.append(word)
    print(_words)

    encoded_text = ''
    for word in _words:
        if word.lower() in words_fill:
            encoded_text += codes_fill[words_fill.index(word.lower())]


    return encoded_text


if __name__ == "__main__":
    sample_text = open('test.txt', 'r').read()

    huffman_code = huffman_encode(sample_text)

    print(huffman_code)
