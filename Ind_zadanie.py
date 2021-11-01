#!/usr/bin/env python 3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    A = (1, 2, 1, 1, 3, 2, 0, 0, 1, 2, 0, 1, 2, 1, 2, 1, 5, 4, 0, 0, 0, 1, 2, 3, 1, 2)
    B = (1, 0, 0, 0, 0, 5, 2, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 3, 1, 1, 2, 1, 2, 1, 2)
    sum_1 = sum(A)
    sum_2 = sum(B)
    print(sum_1 + sum_2)


