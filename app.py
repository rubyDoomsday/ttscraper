import argparse
from app import ttscraper

if __name__=='__main__':
    argParser = argparse.ArgumentParser(
            prog = 'ttscraper',
            description = 'a thousand trails destination processor',
            epilog = 'thanks for playing')

    argParser.add_argument("-w", "--write", help="write to csv")
    argParser.add_argument("-p", "--park", help="park ID")

    args = argParser.parse_args()

    ttscraper.run(args)
