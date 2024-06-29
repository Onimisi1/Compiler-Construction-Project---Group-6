import ast
import astor
import re

class CustomSyntaxError(SyntaxError):
    def __init__(self, message, suggestion, lineno, col_offset):
        super().__init__(message)
        self.suggestion = suggestion
        self.lineno = lineno
        self.col_offset = col_offset

def check_syntax(source):
    source = source.lstrip()  # Strip leading whitespace and newlines
    try:
        ast.parse(source)
    except SyntaxError as e:
        suggestion = suggest_fix(e)
        raise CustomSyntaxError(f"{e.msg}", suggestion, e.lineno, e.offset)

def suggest_fix(error):
    if "unexpected EOF while parsing" in error.msg:
        return "Did you forget to close a parenthesis, bracket, or string?"
    elif "invalid syntax" in error.msg:
        if error.text and "def" in error.text and ":" not in error.text:
            return "It seems like there's a syntax error in your function definition. Ensure you have a colon at the end of the function header."
        elif error.text and "=" in error.text:
            return "Check if you're using the assignment operator correctly."
        elif error.text and ":" in error.text:
            return "Ensure all colons are used correctly, such as in if statements, loops, and function definitions."
        elif error.text and ("(" in error.text or ")" in error.text):
            return "Ensure all opening parentheses have matching closing ones."
        else:
            return "Possible issues include missing colons, unmatched parentheses, or incorrect indentation."
    elif "unexpected indent" in error.msg:
        return "Ensure your indentation is consistent."
    elif "unindent does not match any outer indentation level" in error.msg:
        return "Make sure you are using the correct level of indentation."
    elif "expected an indented block" in error.msg:
        return "Check if you're missing a code block under a statement."
    elif "expected ':'" in error.msg:
        if error.text and "class" in error.text:
            return "Add a colon at the end of the class declaration."
        elif error.text and "def" in error.text:
            return "Add a colon at the end of the function declaration."
        else:
            return "Check your syntax."
    elif "NameError" in error.msg:
        return "Ensure that all variables and functions are defined before use."
    elif "IndentationError" in error.msg:
        return "Check your indentation. Python relies on consistent indentation to define code blocks."
    elif "EOL while scanning string literal" in error.msg:
        return "Ensure all string literals are closed properly."
    elif "EOF while scanning triple-quoted string literal" in error.msg:
        return "Ensure all triple-quoted string literals are closed properly."
    elif "can't assign to" in error.msg:
        return "Ensure you are not trying to assign to a keyword or literal."
    elif "return outside function" in error.msg:
        return "Ensure all return statements are inside a function."
    elif "break outside loop" in error.msg:
        return "Ensure all break statements are inside a loop."
    elif "continue outside loop" in error.msg:
        return "Ensure all continue statements are inside a loop."
    elif "yield outside function" in error.msg:
        return "Ensure all yield statements are inside a function."
    elif "duplicate argument" in error.msg:
        return "Ensure all arguments have unique names."
    elif "non-default argument follows default argument" in error.msg:
        return "Reorder your arguments."
    elif "positional argument follows keyword argument" in error.msg:
        return "Reorder your arguments."
    elif "f-string: unterminated string" in error.msg:
        return "Ensure all f-strings are closed properly."
    elif "f-string: expressions nested too deeply" in error.msg:
        return "Simplify the expression."
    elif "f-string: single '}' is not allowed" in error.msg:
        return "Use a double '}}' to include a literal '}' in an f-string."
    elif "f-string: invalid conversion character" in error.msg:
        return "Use '!s', '!r', or '!a' for string, repr, or ascii conversion."
    elif "invalid character in identifier" in error.msg:
        return "Use only letters, digits, and underscores in identifiers."
    elif "unexpected character after line continuation character" in error.msg:
        return "Ensure the line continuation character is used correctly."
    elif "unterminated parenthetical" in error.msg:
        return "Ensure all parentheses, brackets, and braces are closed properly."
    elif "invalid decimal literal" in error.msg:
        return "Ensure all numeric literals are valid."
    else:
        return "Check your syntax."

def parse_code(source_code):
    try:
        check_syntax(source_code)
        return "Code parsed successfully!"
    except CustomSyntaxError as e:
        return f"SyntaxError on line {e.lineno}, column {e.col_offset}: {e.msg}\nSuggestion: {e.suggestion}"


class Refactorer(ast.NodeTransformer):
    def visit_FunctionDef(self, node):
        original_name = node.name
        node.name = self.to_snake_case(node.name)
        self.generic_visit(node)
        return node

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            node.func.id = self.to_snake_case(node.func.id)
        self.generic_visit(node)
        return node

    def to_snake_case(self, name):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

def refactor_code(source_code):
    parsed = ast.parse(source_code)
    refactored = Refactorer().visit(parsed)
    return astor.to_source(refactored)

def process_code(source_file, return_file=False):
    with open(source_file, 'r') as file:
        source_code = file.read()

    # Check Syntax
    result = parse_code(source_code)
    if "SyntaxError" in result:
        return result
    
    print(result)
    
    # Refactor Code
    refactored_code = refactor_code(source_code)

    if return_file:
        # Write the refactored code to a new file
        with open("compiled_" + source_file, 'w') as file:
            file.write(refactored_code)
    
        return "compiled code written to 'compiled_" + source_code + "'"

    return refactored_code

# source_code = """
# def exampleFunction():
#     print("Hello, world!")

# class BankAccount():
#     def __init__(self):
#         self.value = value

#     def sayHello():
#         print("Hello")

# """

# Provide the path to your python file here
source_code = "CSC454_sourcecode.py"

print(process_code(source_code, return_file=True))




