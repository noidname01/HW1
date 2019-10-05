import sys
from graph_gen import *
from p2 import p2_has_cycle

def main():
    p2_list = list()
    if len(sys.argv) <= 1:
        p2_list = get_p2('r07')
    else:
        p2_list = get_p2(sys.argv[1])
    
    with open(sys.argv[1] + '_p2.txt', 'w') as f2:
        for sets in p2_list:
            if p2_has_cycle(sets):
                f2.write('Yes')
            else:
                f2.write('No')
            f2.write('\n')

if __name__ == '__main__':
    main()
