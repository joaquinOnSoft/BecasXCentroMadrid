import getopt
import sys

from schoolarshipxcenter.consolidation.MadridCenterConsolidator import MadridCenterConsolidator


def print_help():
    print('Preparation of data to analyze the distribution of scholarships by Center in the Community of Madrid')
    print('\nExecution:')
    print('\tMadridCenterDetailGroup.py -i <input_file> -o <output_file>')
    print('where:')
    print('\t-h: Print this help')
    print('\t-i --input: (Mandatory) input file (csv with a list of Centers (Schools, High schools...')
    print('\t-o --output: (Mandatory) output file (csv file which will contains extended information for each center')


def main(argv):
    input_file = None
    output_file = None

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["help", "input=", "output="])
    except getopt.GetoptError:
        print_help()
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print_help()
            sys.exit()
        elif opt in ("-i", "--input"):
            input_file = arg
        elif opt in ("-o", "--output"):
            output_file = arg

    if input_file is not None and output_file is not None:
        MadridCenterConsolidator.process(input_file, output_file, ";")
    else:
        print_help()


if __name__ == "__main__":
    main(sys.argv[1:])
