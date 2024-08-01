##########################################################################
#
# LEXICAL ANALYZER
#
# Tool used to convert RegEx to DFA: https://jack-q.github.io/reg2dfa/
#
# Transition tables are based on the DFA from the tool, using regex as 
# input (but they were adapted, due to tool limitations on regex use).
#
##########################################################################

import sys

from automatas.general_automata import \
    transition_table as general_transition_table, \
    acceptance_states as general_acceptance_states, \
    symbols_dict as general_symbols_dict
from automatas.keywords_automata import \
    transition_table as keywords_transition_table, \
    acceptance_states as keywords_acceptance_states, \
    symbols_dict as keywords_symbols_dict 


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
                actual_state = general_transition_table[actual_state][general_symbols_dict[actual_symbol]]

            # KeyError means that the symbol that is actually being processed is not in symbols_dict 
            except KeyError:

                # but if previous state was acceptance state and actual symbol is in ignored_symbols variable,
                # no error is raised, and the processing continues from state 0 after appending the token
                # formed until now on the tokens_list
                if (
                    (actual_symbol in ignored_symbols)
                    and (previous_state in general_acceptance_states)
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
                    and (previous_state not in general_acceptance_states)
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
                if previous_state in general_acceptance_states: 
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
        if actual_state in general_acceptance_states:
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
                    actual_state = keywords_transition_table[actual_state][keywords_symbols_dict[actual_symbol]]
                except KeyError:
                    token_type = 'identifier'
                
                if actual_state in keywords_acceptance_states:
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


if __name__ == '__main__':

    # cacthes first argument and passes it to main function, that tries to use it as input file name
    args = sys.argv
    if len(args) < 2:
        print('Inform a file name (with extension, if it has) as first command line argument!')
    elif len(args) == 2:
        input_file_name = sys.argv[1]
        main(input_file_name)
    elif len(args) > 2:
        print('This program takes exactly one argument, which is a file name (with extension, if it has).')


