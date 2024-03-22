# lexer.py
class Lexer:
    def __init__(self, text):
        self.text = text
        self.position = 0
        self.current_char = self.text[self.position]

    def error(self):
        raise Exception("Invalid character")

    def advance(self):
        # Move to the next character in the input text
        self.position += 1
        if self.position < len(self.text):
            self.current_char = self.text[self.position]
        else:
            self.current_char = None

    def get_integer(self):
        # Extract an integer from the input text
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        while self.current_char is not None:
            if self.current_char.isspace():
                # Skip whitespace characters
                self.advance()
                continue
            if self.current_char.isdigit():
                # Recognize and return INTEGER tokens
                return {'type': 'INTEGER', 'value': self.get_integer()}
            if self.current_char == '+':
                # Recognize and return PLUS tokens
                self.advance()
                return {'type': 'PLUS', 'value': '+'}
            if self.current_char == '-':
                # Recognize and return MINUS tokens
                self.advance()
                return {'type': 'MINUS', 'value': '-'}
            if self.current_char == '*':
                # Recognize and return MULTIPLY tokens
                self.advance()
                return {'type': 'MULTIPLY', 'value': '*'}
            if self.current_char == '/':
                # Recognize and return DIVIDE tokens
                self.advance()
                return {'type': 'DIVIDE', 'value': '/'}
            self.error()  # Raise an exception for invalid characters
        return {'type': 'EOF', 'value': None}
