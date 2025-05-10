from src.interface.ui import banner
from src.pinkerton.main import perform_checks

from argparse import ArgumentParser

if __name__ == "__main__":
    
    banner()

    parser = ArgumentParser()
    parser.add_argument("-u", "--url", help="Specify the target URL", required=True)
    parser.add_argument("-H", "--HEADER", help="Specify a custom header to be used", nargs=2, default=[], action='append')
    args = parser.parse_args()

    perform_checks(args)
