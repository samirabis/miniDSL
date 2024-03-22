# dsl_interpreter.py
from lexer import Lexer
from my_parser import Parser  # Use relative import
from interpreter import Interpreter

def main():
    while True:
        try:
            text = input('DSL> ')  # Prompt user for DSL input
        except EOFError:
            break
        if not text:
            continue

        # Initialize lexer, parser, and interpreter
        lexer = Lexer(text)
        parser = Parser(lexer)
        interpreter = Interpreter(parser)

        # Interpret the DSL expression and display the result
        result = interpreter.interpret()

        print(result)

if __name__ == "__main__":
    main()
