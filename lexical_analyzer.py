##########################################################################
#
# TIAGO JOSÉ DA ROSA - 20200637
#
# LEXICAL ANALYZER
#
# Tool used to convert RegEx to DFA: https://jack-q.github.io/reg2dfa/
#
# Transition tables are based on the DFA from the tool, using regex as 
# input (but adapted, due to tool limitations).
#
##########################################################################

import sys

# the transition_table_1 is used to catch identifiers, numbers and all other terminal symbols, but not reserved words.
transition_table_1 = [
#    a       b       c       d       e       f       g       h       i       j       k       l       m       n       o       p       q       r       s       t       u       v       w       x       y       z       A       B       C       D       E       F       G       H       I       J       K       L       M       N       O       P       Q       R       S       T       U       V       W       X       Y       Z       _       0       1       2       3       4       5       6       7       8       9       (       )       {       }       ;       =       ,       <       >       +       -       *
    [2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  False,  4    ,  4    ,  4    ,  4    ,  4    ,  4    ,  4    ,  4    ,  4    ,  4    ,  5    ,  6    ,  7    ,  8    ,  9    ,  1    ,  10   ,  11   ,  12   ,  13   ,  14   ,  15   ], #0
    [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  3    ,  False,  False,  False,  False,  False,  False], #1
    [2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  2    ,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False], #2
    [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False], #3
    [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  4    ,  4    ,  4    ,  4    ,  4    ,  4    ,  4    ,  4    ,  4    ,  4    ,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False], #4
    [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False], #5
    [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False], #6
    [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False], #7
    [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False], #8
    [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False], #9
    [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False], #10
    [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False], #11
    [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False], #12
    [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  4    ,  4    ,  4    ,  4    ,  4    ,  4    ,  4    ,  4    ,  4    ,  4    ,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False], #13
    [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  4    ,  4    ,  4    ,  4    ,  4    ,  4    ,  4    ,  4    ,  4    ,  4    ,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False], #14
    [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False]  #15

]

# acceptance states for transition_table_1 
acceptance_states1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]


# the transition_table_2 is used to catch reserved words after they were identified as identifiers.
transition_table_2 = [
#    d       e       p       r       f       l       s       i       n       t       u 
    [1    ,  2    ,  4    ,  5    ,  False,  False,  False,  3    ,  False,  False,  False], #0
    [False,  6    ,  False,  False,  False,  False,  False,  False,  False,  False,  False], #1
    [False,  False,  False,  False,  False,  7    ,  False,  False,  False,  False,  False], #2
    [False,  False,  False,  False,  25    ,  False,  False,  False,  9    ,  False,  False], #3
    [False,  False,  False,  10   ,  False,  False,  False,  False,  False,  False,  False], #4
    [False,  11   ,  False,  False,  False,  False,  False,  False,  False,  False,  False], #5
    [False,  False,  False,  False,  23   ,  False,  False,  False,  False,  False,  False], #6
    [False,  False,  False,  False,  False,  False,  13   ,  False,  False,  False,  False], #7
    [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False], #8
    [False,  False,  False,  False,  False,  False,  False,  False,  False,  24   ,  False], #9
    [False,  False,  False,  False,  False,  False,  False,  15   ,  False,  False,  False], #10
    [False,  False,  False,  False,  False,  False,  False,  False,  False,  16   ,  False], #11
    [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False], #12
    [False,  17   ,  False,  False,  False,  False,  False,  False,  False,  False,  False], #13
    [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False], #14
    [False,  False,  False,  False,  False,  False,  False,  False,  18   ,  False,  False], #15
    [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  19   ], #16
    [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False], #17
    [False,  False,  False,  False,  False,  False,  False,  False,  False,  20   ,  False], #18
    [False,  False,  False,  21   ,  False,  False,  False,  False,  False,  False,  False], #19
    [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False], #20
    [False,  False,  False,  False,  False,  False,  False,  False,  22   ,  False,  False], #21
    [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False], #22
    [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False], #23
    [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False], #24
    [False,  False,  False,  False,  False,  False,  False,  False,  False,  False,  False]  #25
]

# acceptance states for transition_table_2
acceptance_states2 = [17,20,22,23,24,25]

# symbols dictionary for transition_table_1
symbols_dict1 = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25,
    "A": 26,
    "B": 27,
    "C": 28,
    "D": 29,
    "E": 30,
    "F": 31,
    "G": 32,
    "H": 33,
    "I": 34,
    "J": 35,
    "K": 36,
    "L": 37,
    "M": 38,
    "N": 39,
    "O": 40,
    "P": 41,
    "Q": 42,
    "R": 43,
    "S": 44,
    "T": 45,
    "U": 46,
    "V": 47,
    "W": 48,
    "X": 49,
    "Y": 50,
    "Z": 51,
    "_": 52,
    "0": 53,
    "1": 54,
    "2": 55,
    "3": 56,
    "4": 57,
    "5": 58,
    "6": 59,
    "7": 60,
    "8": 61,
    "9": 62,
    "(": 63,
    ")": 64,
    "{": 65,
    "}": 66,
    ";": 67,
    "=": 68,
    ",": 69,
    "<": 70,
    ">": 71,
    "+": 72,
    "-": 73,
    "*": 74
}

# symbols dictionary for transition_table_2
symbols_dict2 = {
    "d": 0,
    "e": 1,
    "p": 2,
    "r": 3,
    "f": 4,
    "l": 5,
    "s": 6,
    "i": 7,
    "n": 8,
    "t": 9,
    "u": 10
}

def main(input_file_name):
    
    line = 0
    column = 0
    actual_state = 0
    previous_state = 0
    actual_token = ''
    tokens_list = []
    ignored_symbols = [' ', '\t', '\n', '\r']
    newliners = ['\n','\r']

    with open(input_file_name) as f:

        # gets file content
        file_content = f.read()
        file_lenght = len(file_content)
        i = 0

        # iterates throught every file's character
        while i < file_lenght:
            actual_symbol = file_content[i]
    
            # tries to advance to next state
            try:
                previous_state = actual_state
                actual_state = transition_table_1[actual_state][symbols_dict1[actual_symbol]]

            # KeyError means that the symbol that is actually being processed is not in symbols_dict 
            except KeyError:

                # but if previous state was acceptance state and actual symbol is in ignored_symbols variable,
                # no error is raised, and the processing continues from state 0 after appending the token
                # formed until now on the tokens_list
                if (
                    (actual_symbol in ignored_symbols)
                    and (previous_state in acceptance_states1)
                ): 
                    processed_token = process_token(actual_token, previous_state)
                    tokens_list.append(processed_token)
                    actual_token = ''
                    actual_state = 0
                    column += 1

                    if actual_symbol in newliners:
                        line += 1
                        column = 0

                    i += 1
                    continue

                # and if previous state was NOT acceptance state and actual symbol is in ignored_symbols variable,
                # it just goes to the next iteration (an example is when two ignored_symbols come one after the other)
                elif (
                    (actual_symbol in ignored_symbols)
                    and (previous_state not in acceptance_states1)
                ):
                    column += 1
                    
                    if actual_symbol in newliners:
                        line += 1
                        column = 0

                    i += 1
                    continue

                # if symbol is not in symbols_dict and is not in ignored_symbols, shows error and exits
                elif (actual_symbol not in ignored_symbols):
                    print(f'LEXICAL ERROR! line:{line}, column:{column} (UNSUPORTED SYMBOL: {actual_symbol})')
                    print('Note: lines and columns start from zero.')
                    exit()

            # if actual state is a valid state, add symbol to token formation
            if actual_state != False:
                actual_token += actual_symbol
                
            # if actual state is invalid
            if actual_state == False:
                
                # but previous state was valid, appends token to tokens_list and restarts from state 0
                # without going to next iteration
                # [an example is when a '(' symbol arrives after a 't' and the actual token is 'int']
                if previous_state in acceptance_states1: 
                    processed_token = process_token(actual_token, previous_state)
                    tokens_list.append(processed_token)
                    actual_token = ''
                    actual_state = 0
                    column += 1

                    if actual_symbol in newliners:
                        line += 1
                        column == 0

                    continue

                # and previous state was invalid, shows error and exits
                actual_token += actual_symbol
                print(f'LEXICAL ERROR! line:{line}, column:{column} (UNSUPORTED PATTERN: {actual_token})')
                print('Note: lines and columns start from zero.')
                exit()
            
            column += 1
            i += 1
            
        # if the while loop ended at acceptance state, adds the last token to tokens_list
        if actual_state in acceptance_states1:
            processed_token = process_token(actual_token, actual_state)
            tokens_list.append(processed_token)
        
        # shows output (each list item at a line)
        for i in tokens_list:
            print(i)
            
# receives tokens as strings and returns them as tuples containing token_type and token_value.
# If token received is an identifier, it checks if this identifier is not a reserved word. If 
# it is, returns the token with the correct type.
def process_token(actual_token, previous_state):
    token_type = ''

    match previous_state:
        case 1: 
            token_type = 'atribution'
        
        case 2:
            # identifier
            actual_state = 0
            for i in range(len(actual_token)):
                actual_symbol = actual_token[i]

                try:
                    actual_state = transition_table_2[actual_state][symbols_dict2[actual_symbol]]
                except KeyError:
                    token_type = 'identifier'
                
                if actual_state in acceptance_states2:
                    processed_token = process_token(actual_token, actual_state)
                    return processed_token
                
                else:
                    token_type = 'identifier'
        
        case 3:
            token_type = 'assertion'
        
        case 4:
            token_type = 'number'
        
        case 5:
            token_type = 'open_parenthesis'
        
        case 6:
            token_type = 'close_parenthesis'
        
        case 7:
            token_type = 'open_curly_brackets'
        
        case 8:
            token_type = 'close_curly_brackets'
        
        case 9:
            token_type = 'semicolon'
        
        case 10:
            token_type = 'comma'
        
        case 11:
            token_type = 'lesser_than'
        
        case 12:
            token_type = 'greater_than'
        
        case 13:
            token_type = 'plus'
        
        case 14:
            token_type = 'minus'
        
        case 15:
            token_type = 'multiplier' 
        
        case 17:
            token_type = 'else'
        
        case 20:
            token_type = 'print'
        
        case 22:
            token_type = 'return'
        
        case 23:
            token_type = 'def'
        
        case 24:
            token_type = 'int'
        
        case 25:
            token_type = 'if'

    return (token_type, actual_token)


# cacthes first argument and passes it to main function, that tries to use it as input file name
if __name__ == '__main__':
    args = sys.argv
    if len(args) == 1:
        print('Inform a file name (with extension, if it has) as first command line argument!')
    else:
        input_file_name = sys.argv[1]
        main(input_file_name)


