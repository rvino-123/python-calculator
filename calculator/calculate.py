"""This file performs the calcluation and returns a value"""
from parser import Parser
from tokenizer import tokenize

calculateFunctions = {}


class Calculator():
    def __init__(self, cmdString):
        self.cmdString = cmdString
        self.tokenize = tokenize
