from lark import Lark, Tree, Transformer, v_args

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


grammar = r"""
        !expr: expr (and|or) expr | factor
        !factor: "(" expr ")" | identifier | not factor
        !and: "and"
        !or: "or"
        !not: "not"|"~"
        !identifier: "a"|"b"|"c"|"d"
        %import common.ESCAPED_STRING
        %import common.SIGNED_NUMBER
        %import common.WS
        %ignore WS
        """

def build_array_from_tree(root):
    # depth first search: inorder traversal
    s = [root]
    res = []
    while s:
        curr = s.pop()
        #go only left first
        if (root.__class__.__name__ == "Token"):
            # node is a leaf
            res.append(str(curr))
        for child in root.children:
            s.append(child)
    return res

def compute(expr):
    bool_parser = Lark(grammar, start='expr', parser="lalr")
    try:
        tree = bool_parser.parse(expr)
        print(bool_parser)
        print(tree)
        #print(build_array_from_tree(tree))
    except Exception:
        print("Invalid expression!")
        return 
    


if __name__ == "__main__":
    expr = input("Please enter a boolean expression with a,b,c: ")
    compute(expr)
