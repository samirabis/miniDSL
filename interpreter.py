# interpreter.py
from my_parser import Parser  # Use relative import


class Interpreter:
    def __init__(self, parser):
        self.parser = parser

    def interpret(self):
        # Start the interpretation process by calling the parser's expr() method
        return self.parser.expr()
