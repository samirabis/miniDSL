# parser.py
class Parser:
    def __init__(self, lexer):
        self.lexer = lexer
        self.current_token = self.lexer.get_next_token()

    def error(self, message):
        raise Exception(message)

    def eat(self, token_type):
        # Consume the current token if it matches the expected type
        if self.current_token['type'] == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()  # Raise an exception for unexpected token types


    def factor(self):
        token = self.current_token
        self.eat('INTEGER')

        if token['value'] == 0 and self.current_token['type'] == 'DIVIDE':
            self.error("Division by zero")

        return token['value']

    def term(self):
        result = self.factor()

        while self.current_token['type'] in ('MULTIPLY', 'DIVIDE'):
            token = self.current_token
            if token['type'] == 'MULTIPLY':
                self.eat('MULTIPLY')
                result *= self.factor()
            elif token['type'] == 'DIVIDE':
                self.eat('DIVIDE')
                divisor = self.factor()
                if divisor == 0:
                    self.error("Division by zero")
                result /= divisor

        return result

    def expr(self):
        result = self.term()

        while self.current_token['type'] in ('PLUS', 'MINUS'):
            token = self.current_token
            if token['type'] == 'PLUS':
                self.eat('PLUS')
                result += self.term()
            elif token['type'] == 'MINUS':
                self.eat('MINUS')
                result -= self.term()

        return result
