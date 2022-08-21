import argparse

# Flags spider configurations
def config_args():
    parse = argparse.ArgumentParser(
        description="""*** Arachnida - Spider ***
        Web Image Scraper - Download all images from a target website."""
    )
    # Recursive download resources
    parse.add_argument("-r","--recursive", default=None, help="[-r URL] Recursive mode.")
    # Level of depth scanning
    parse.add_argument("-l","--level", default=None, help="[-r URL -l Nº] Recursive mode + level of scanning.")
    # Path of download resources
    parse.add_argument("-p","--path", default=None, help="[-r URL -p /absolute-path] Dyrectory for download images.")
    # Silent mode
    parse.add_argument("-S","--silent", default=False, action="store_true", help="Silent option.")
    # Download resource from url
    parse.add_argument("-i","--image", default=None, help="[-i URL-RESOURCE] Download resource image to default path.")
    return parse.parse_args()