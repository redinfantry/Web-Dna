import hashlib
import json
import os
import re
import subprocess
import sys
import time
import urllib.request
import webbrowser

def get_user_agent():
    return os.environ.get('HTTP_USER_AGENT', '')

def get_screen_resolution():
    return subprocess.check_output('xrandr | grep "\*" | cut -d" " -f4', shell=True).decode().strip()

def get_timezone():
    return time.strftime('%z')

def get_ip_address():
    return urllib.request.urlopen('https://api.ipify.org').read().decode()

def get_language():
    return os.environ.get('HTTP_ACCEPT_LANGUAGE', '')

def get_installed_fonts():
    return subprocess.check_output('fc-list', shell=True).decode()

def get_webgl_fingerprint():
    # Open a headless Chrome instance
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options)

    # Navigate to a website that generates a WebGL fingerprint
    driver.get('https://valve.github.io/fingerprintjs2/')
    time.sleep(5)

    # Extract the WebGL fingerprint from the website's output
    output_element = driver.find_element_by_id('output')
    output_text = output_element.text
    fingerprint_match = re.search(r'WebGL fingerprint: (.+)', output_text)
    if fingerprint_match:
        return fingerprint_match.group(1)
    else:
        return None

def generate_hash():
    # Get all the information
    user_agent = get_user_agent()
    screen_resolution = get_screen_resolution()
    timezone = get_timezone()
    ip_address = get_ip_address()
    language = get_language()
    installed_fonts = get_installed_fonts()
    webgl_fingerprint = get_webgl_fingerprint()

    # Combine the information into a dictionary
    info_dict = {
        'user_agent': user_agent,
        'screen_resolution': screen_resolution,
        'timezone': timezone,
        'ip_address': ip_address,
        'language': language,
        'installed_fonts': installed_fonts,
        'webgl_fingerprint': webgl_fingerprint,
    }

    # Convert the dictionary to a JSON string
    info_json = json.dumps(info_dict, sort_keys=True)

    # Generate a SHA-256 hash of the JSON string
    hash_obj = hashlib.sha256(info_json.encode())
    return hash_obj.hexdigest()

if __name__ == '__main__':
    hash_value = generate_hash()
    print(hash_value)
