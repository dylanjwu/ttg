"""
valid operators: and/^/&, or/|, ~/not, ->/=>
identifiers: anything without a space in it
parentheses: e.g. (a and b) or ~(a or (a and ~b)) -> c

API outline:
- take in input expression from user via CLI or http API call from front end
- [create boolean expression CFG]
- use Lark parser library to parse the expression using the CFG
- parse out the identifiers from the accepted input string
- run the 'generate_TT' script on the number of identifiers
- enumerate through each T/F configuration:
    - replace each identifier with a 1 or 0
    - call eval on the string, store its T/F (0/1) result
- once each combination has been evaluated, and its result stored, 
    return all of the necessary information (incl. the expression input)
"""