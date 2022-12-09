import math


# H(X)
def get_entropy(probabilities: list):
    return -sum(map(lambda p: p * math.log(p, 2), probabilities))