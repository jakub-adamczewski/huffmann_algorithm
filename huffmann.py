class Node(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return self.left, self.right


def huffman_code_tree(node, bin_string: str = ''):
    if type(node) is str:
        return {node: bin_string}
    (l, r) = node.children()
    d = {}
    d.update(huffman_code_tree(l, bin_string + '1'))
    d.update(huffman_code_tree(r, bin_string + '0'))
    return d


def get_huffman_coding(string: str, log=False):
    counts = {}
    for c in string:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1

    counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

    nodes = counts

    while len(nodes) > 1:
        (key1, c1) = nodes[-1]
        (key2, c2) = nodes[-2]
        nodes = nodes[:-2]
        node = Node(key1, key2)
        nodes.append((node, c1 + c2))

        nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

    huffmanCode = huffman_code_tree(nodes[0][0])

    if log:
        print(' Char | Huffman code ')
        print('#####################')
        for (char, frequency) in counts:
            print(' %-4r | %12s' % (char, huffmanCode[char]))

    return huffmanCode
