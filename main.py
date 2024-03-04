import argparse
from src.controller import Controller


def main():
    parser = argparse.ArgumentParser(description='Convert JSON to XML')
    parser.add_argument('filename', help='JSON file to convert')
    parser.add_argument(
        '--root_el_name', help='Name for the root element', default='root')
    args = parser.parse_args()

    Controller.start(args.filename, args.root_el_name)


if __name__ == '__main__':
    main()
