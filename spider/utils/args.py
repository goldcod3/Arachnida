import argparse

# Flags spider configurations
def config_args():
    parse = argparse.ArgumentParser(
        description="""*** Arachnida - Spider ***
        Web Image Scraper - Download all images from a target website."""
    )
    parse.add_argument("-r","--recursive", default=None, help="[-r URL] Recursive mode.")
    parse.add_argument("-l","--level", default=None, help="[-r URL -l Nº] Recursive mode + level of scanning.")
    parse.add_argument("-p","--path", default=None, help="[-r URL -p /absolute-path] Dyrectory for download images.")
    parse.add_argument("-S","--silent", default=False, action="store_true", help="Silent option.")
    parse.add_argument("-i","--image", default=None, help="[-i URL-RESOURCE] Download resource image to default path.")
    return parse.parse_args()