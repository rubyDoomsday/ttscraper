import argparse
from app import ttscraper

if __name__=='__main__':
    argParser =argparse.ArgumentParser()
    argParser.add_argument("-w", "--write", help="write to csv")
    argParser.add_argument("-p", "--park", help="park ID")

    args = argParser.parse_args()

    ttscraper.run(args)
