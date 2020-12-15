if __name__ == '__main__':
    # importing required modules
    import argparse

    # create a parser object
    parser = argparse.ArgumentParser(description='End-to-end low-code NLP framework')

    # add argument
    parser.add_argument(
        'config', nargs = 1, metavar = "path to config file",
        help = 'Specify path to configuration file'
    )

    # parse the arguments from standard input
    args = parser.parse_args()

    # check if add argument has any input data.
    # If it has, then print sum of the given numbers
    if len(args.add) != 0:
        print(sum(args.add))
else:
