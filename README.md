TIAGO JOSÉ DA ROSA - 20200637

### How to execute the Lexical Analyzer

- Put all files in the same directory (test files and lexical analyzer)
- After opening the terminal on this directory, execute the following command:
- `python3 lexical_analyzer.py lexical_test1.lsi`

### Output

- If no error occurred, it outputs tuples containing token type and token value, in this order. The tuples are outputed in the same order that the tokens appear on the input file.
- If an error occurred, it outputs an error message.

Success output example:

```
('int', 'int')
('identifier', 'first')
('semicolon', ';')
('int', 'int')
('identifier', 'second')
('semicolon', ';')
```

Error output example:

```
LEXICAL ERROR! line:14, column:11 (UNSUPORTED SYMBOL: ')
Note: lines and columns start from zero.
```