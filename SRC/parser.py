from argparse import ArgumentParser
#from SRC.createdfsregion import filterRegion

def parser():
    # Create ArgumentParser object
    parser = ArgumentParser(description="HDI calculations")
    # Add argument
    #No int arguments
    # Boolean Argument
    parser.add_argument("-top", action='store_true',default=False)
    parser.add_argument("-region", action='store_true', default=False)
    parser.add_argument("-filt", action='store_true', default=False)
    parser.add_argument("-repo", action='store_true', default=False)
    # Group of arguments, mutually exclusive
    #parser.add_argument("numbers", type=float, nargs=2, help="Two values between 0.49 and 0.93")
    # Retrieve Arguments
    args = parser.parse_args()
    # Accessing different variables in args
    top = args.top
    region = args.region
    filt = args.filt
    repo = args.repo

    return top,region,filt,repo