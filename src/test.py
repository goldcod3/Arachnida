from fuzzer import *

fuz = Fuzzer("https://www.kali.org/")
fuz.get_hrefs()
fuz.print_result()