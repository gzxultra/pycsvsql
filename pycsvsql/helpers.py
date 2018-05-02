# coding: utf-8
from itertools import islice


def next_n_lines(file, n_lines):
    return [x.strip() for x in islice(file, n_lines)]
