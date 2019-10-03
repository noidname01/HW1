import sys
from graph_gen import *
from p1 import p1_has_cycle

def main():
    p1_list = list()
    if len(sys.argv) <= 1:
        p1_list = get_p1('r07')
    else:
        p1_list = get_p1(sys.argv[1])
        
    with open(sys.argv[1] + '_p1.txt', 'w') as f1:
        for sets in p1_list:
            if p1_has_cycle(sets):
                f1.write('Yes')
            else:
                f1.write('No')
            f1.write('\n')

if __name__ == '__main__':
    main()
