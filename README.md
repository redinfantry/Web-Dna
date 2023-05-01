
# Web Dna

A web fingerprinting application is a software tool that helps identify and track visitors to web servers. This tool can gather information about the user's browser, operating system, IP address, screen resolution, and other attributes. The collected data can then be used to build a unique profile for each visitor, enabling website owners to monitor their traffic, target their marketing campaigns more effectively, and enhance the overall user experience.

The application works by analyzing the user's HTTP request and response headers, as well as other client-side data that is transmitted during the interaction with the website. The software then compares this data to a database of known fingerprints, which are unique identifiers based on the user's hardware and software configurations.

In addition to providing valuable insights into website traffic, web fingerprinting can also be used for security purposes. By monitoring incoming traffic and detecting anomalies or suspicious patterns, this tool can help identify potential threats and protect against malicious attacks.

Overall, a web fingerprinting application can be a powerful tool for website owners, marketers, and security professionals alike, helping to optimize web performance, enhance user experiences, and safeguard against potential threats.

Also it can help law enforcement agencies to create a unique profile of the visitors and maybe potentially used to identify and track the criminals with the help of information provided by the Web-Dna

## Necessary Dependencies

This program uses various Python modules to extract the requested information. It uses os.environ to get the user agent and language, subprocess to execute a shell command to get the screen resolution and installed fonts, time to get the timezone, urllib.request to get the IP address, and Selenium's webdriver to generate a WebGL fingerprint.

Once all the information is collected, the program combines it into a dictionary and converts it to a JSON string. Then it generates a SHA-256 hash of the JSON string using the hashlib module. Finally, it prints the hash value to the console.

Note that this program requires a few additional dependencies, such as hashlib, json, os, re, subprocess, time, urllib, and selenium. You may need to install these dependencies using pip before running the program.

```bash
  pip install [Package-name]
```


## Installation

Fork or download this repo and unzip the zip package and after that run the script

```bash
  python3 fingerprinting.py [request-from-client]
```
    
