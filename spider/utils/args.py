import argparse

# Flags spider configurations
def config_args():
    parse = argparse.ArgumentParser(
        description="""*** Arachnida - Spider ***
        Web Scraper - Download resources from a target website."""
    )
    # Recursive download resources
    parse.add_argument("-r","--recursive", default=None, help="[-r <URL>] Recursive mode.")
    # Level of depth scanning
    parse.add_argument("-l","--level", default=None, help="[-r <URL> -l <Nº>] Recursive mode + level of scanning.")
    # Path of download resources
    parse.add_argument("-p","--path", default=None, help="[-r <URL> -p <path>] Recursive mode + directory for download images.")
    # Download resource from url
    parse.add_argument("-f","--file", default=None, help="[-f <URL-RESOURCE>] Download resource image to default data path.")
    # Silent mode
    parse.add_argument("-S","--silent", default=False, action="store_true", help="Silent mode option.")
    return parse.parse_args()