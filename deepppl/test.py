import sys
from antlr4 import *
from parser.stanLexer import stanLexer
from parser.stanParser import stanParser

def main(argv):
    input = FileStream(argv[1])
    lexer = stanLexer(input)
    stream = CommonTokenStream(lexer)
    parser = stanParser(stream)
    tree = parser.program()
    print(tree.toStringTree(recog=parser))

if __name__ == '__main__':
    main(sys.argv)