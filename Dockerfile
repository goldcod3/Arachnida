FROM debian:latest

# Install Dependencies
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install sudo zip vim -y
RUN apt-get install python3 python3-pip -y
RUN pip install beautifulsoup4 requests lxml tqdm Pillow
RUN pip install exifread python-docx pypdf2

# User target configuration
RUN useradd -m dev
RUN usermod -s /bin/bash dev
RUN usermod -aG sudo dev
RUN echo "dev:42madrid" | chpasswd

# Volume directory
RUN mkdir -p /home/dev/spider
RUN mkdir -p /home/dev/scorpion

USER dev

ENTRYPOINT bash
