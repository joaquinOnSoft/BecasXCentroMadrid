import getopt
import sys

from schoolarshipxcenter.consolidation.MadridCenterConsolidator import MadridCenterConsolidator


def main(argv):
    input_file = None
    output_file = None

    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["input=", "output="])
    except getopt.GetoptError:
        print('MadridCenterDetailGroup.py -i <input_file>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('MadridCenterDetailGroup.py -i <input_file> -o <output_file>')
            sys.exit()
        elif opt in ("-i", "--input"):
            input_file = arg
        elif opt in ("-o", "--output"):
            output_file = arg

    print('Input file is:', input_file)
    print('Output file is:', output_file)

    if input_file is not None:
        MadridCenterConsolidator.process(input_file, ";")


if __name__ == "__main__":
    main(sys.argv[1:])
