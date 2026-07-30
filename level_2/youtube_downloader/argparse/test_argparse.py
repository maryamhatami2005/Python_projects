import argparse


def main():
    pass

if __name__ == "__main__" :
    parser = argparse.ArgumentParser(
        description = "YouTube Downloader"
    )


    parser.add_argument( "-u", "--url",  help= "YouTube video URL", default=None)
    parser.add_argument("-q", "--quality", help= "Quality of the video", default= 720)
    parser.add_argument("-o", "--output", help="The address of the file to be saved", default=None)

    parser.add_argument("-d", "--delay", help= "Delay between downloads", type=int, default=0)
    parser.add_argument("-ul", "--url_list", help="list of URLs", nargs= "+")

    args= parser.parse_args()

    print(args)
    print(args.url)