#!/usr/bin/env python3

import string
import numpy as np
import typing

def toNum(text):
    alpha = string.ascii_lowercase
    num = np.array([],dtype=np.int64)
    for i in text:
        #print(i)
        if i not in string.whitespace:
            #print(i)
            num = np.append(num,[alpha.index(i)])
    return num

def toText(num):
    alpha = string.ascii_lowercase
    text = ""
    for i in num:
        text = text + alpha[i]
    return text


class Code(object):

    code = None

    def __init__ (self, plain_text):
        self.code = toNum(plain_text)

    def add(self, value: int):
        self.code += value*np.ones(len(self.code),dtype=np.int64)
        self.code = self.code % 26

    def add_code(self, value):
        print(type(value))
        for i in range(min(len(value.code),len(self.code))):
            self.code[i] += value.code[i]
            self.code = self.code % 26

    def append(self, value):
        self.code = np.append(self.code, value.code)

    def print(self):
        print(toText(self.code))
        