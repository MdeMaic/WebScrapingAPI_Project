from argparse import ArgumentParser
from SRC.createdfsregion import createRegion

def parser():
    # Create ArgumentParser object
    parser = ArgumentParser(description="HDI calculations")
    # Add argument
    #No int arguments
    # Boolean Argument
    parser.add_argument("-top", action='store_true',default=False)
    # Group of arguments, mutually exclusive
    parser.add_argument("-region", action='store_const', const=createRegion)
    # Retrieve Arguments
    args = parser.parse_args()
    # Accessing different variables in args
    top = args.top
    region = args.region
    
    return top,region