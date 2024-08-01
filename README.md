# About

This was a college project for the discipline of Introduction to Compilers, where the goal was to create a lexical analyzer. The program receives an input file with code written on a given gramatic, and identifies all tokens from this file, except when there is an error, which means that there was a token that is not part of the accepted gramatic. All the token recognition was made based on finite automata using transition tables.

The accepted tokens are:

- identifiers, caracterized by the following RegEx: `([a-z]|[A-Z])([a-z]|[A-Z]|[0-9]|_)*`
- numbers (integers), caracterized by the following RegEx: `(+|-)?([0-9])*`
- reserved words: `def else if int print return`
- symbols: `( ) { } ; = , > < + - *`

## How to execute the Lexical Analyzer

- Clone or download the repository
- Open the terminal on the cloned/downloaded repository
- Execute the following command: `python3 lexical_analyzer.py lexical_test_1.lsi`

## Output

- If no error occurred, it outputs tuples containing token type and token value, in this order. Tuples are outputed in the same order that the tokens appear on the input file.
- If an error occurred, it outputs an error message, informing line and column where the error was found.

Success output example:

```
('int', 'int')
('identifier', 'first')
('semicolon', ';')
('int', 'int')
('identifier', 'second')
('semicolon', ';')
```

Error output example (unsuported symbol):

```
LEXICAL ERROR! line:14, column:11 (UNSUPORTED SYMBOL: ')
Note: lines and columns start from zero.
```

Error output example (unsuported pattern):

```
LEXICAL ERROR! line:14, column:58 (UNSUPORTED PATTERN: _)
Note: lines and columns start from zero.
```