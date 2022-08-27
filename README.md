# Arachnida
Web scraper and metadata display tool developed in the cybersecurity bootcamp at 42Madrid.

<img src='https://media.giphy.com/media/3oz8xC4rcE2A7onfoc/giphy.gif' width=500 heigth=500/>

Metadata is information that is used to describe other data, it is essentially data about data and is used in images 
and documents and can reveal sensitive information about those who have created or manipulated it.

The purpose of this project is to create two tools that will allow you to automatically extract information from 
the web and then analyze it to learn about sensitive data.

The **Spider** program will allow you to extract all the images, pdf and docx files from a website, recursively, by providing a url as a parameter.

The second **Scorpion** program will receive image files as parameters and will be able to analyze them for [EXIF](https://en.wikipedia.org/wiki/Exif) data and other metadata, displaying them on screen. 
It will support at least the same extensions that spider handles. It shall display basic attributes such as date of creation as well as other EXIF data.

To run the python script you must install the requirements indicated in the file 'requirements.txt'
```
pip install -r requirements.txt
```

# Spider
<img src='https://media.giphy.com/media/n8cIlujV4OoClykKMt/giphy.gif' width=400 heigth=400/>

### Options
```
# Recursive mode
python3 spider.py -r <URL>

# Recursive mode + level depth
python3 spider.py -r <URL> -l <Nº>

# Recursive mode +  directory download path
python3 spider.py -r <URL> -p <PATH>

# Recursive mode + Silent output
python3 spider.py -r <URL> -S

# File mode 
python3 spider.py -f <URL-RESOURCE>

# Print help message
python3 spider.py -h
```
When running the tool the **/data** folder and the **/logs** folder are generated in the repository directory, 
/data contains the files downloaded from the target website and /logs contains the log of actions. 

# Scorpion
<img src='https://media.giphy.com/media/5n3ZO8jVcAQow/giphy.gif' width=400 heigth=400/>

### Options
```
# Resources mode
python3 scorpion.py FILE1 FILE2 FILE3 ...

# Directory mode
python3 scorpion.py -d <DIRECTORY-PATH>
```

# Run Docker Test
- Install '[Docker Desktop](https://www.docker.com/products/docker-desktop/)' and run the app.
- Install 'make' and use the Makefile for buid a container and get a bash:
```
make && make exec
```
```
# Build image and container
->> make
# Get a bash from container
->> make exec
# Build a new container
->> make dock
# Build image
->> make image
# Remove image and container
->> make fclean
```
In the user's /home directory inside the container, two directories are generated and synchronized 
with the directories of both tools by means of volumes.

**Enjoy!**

---
Finished project.

![lgomes-o's 42 arachnida Score](https://badge42.vercel.app/api/v2/cl4osmqtg006109jvtxcd7k3u/project/2726915)
