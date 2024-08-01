# this transition table is used to catch reserved words after they were identified as identifiers
transition_table = [
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

# transition table's acceptance states
acceptance_states = [17,20,22,23,24,25]

# transition table's symbols dictionary
symbols_dict = {
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