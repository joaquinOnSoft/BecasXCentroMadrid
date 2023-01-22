import getopt
import sys

from schoolarshipxcenter.consolidation.MadridGrantByCenterConsolidator import MadridGrantByCenterConsolidator


def print_help():
    print('Mix a csv with the centers and the grants by center in a single file')
    print('\nExecution:')
    print('\tMadridCenterGrantDetail.py -c <centers_file> -g <grant_file> -o output')
    print('where:')
    print('\t-h --help: Print this help')
    print('\t-c --center: (Mandatory) Centers file (csv with a list of Centers (Schools, High schools...')
    print('\t-g --grant: (Mandatory) Grants file (csv with a list of Grants by Center')
    print('\t-o --output: (Mandatory) output file (csv file which will contains extended information for each center')


def main(argv):
    center_file = None
    grant_file = None
    output_file = None

    try:
        opts, args = getopt.getopt(argv, "hc:g:o:", ["help", "center=", "grant=", "output="])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_help()
            sys.exit()
        elif opt in ("-c", "--center"):
            center_file = arg
        elif opt in ("-g", "--grant"):
            grant_file = arg
        elif opt in ("-o", "--output"):
            output_file = arg

    if center_file is not None and grant_file is not None and output_file is not None:
        MadridGrantByCenterConsolidator.process(center_file, ";", grant_file, ";", output_file)
    else:
        print_help()


if __name__ == "__main__":
    main(sys.argv[1:])
