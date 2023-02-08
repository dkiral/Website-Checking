import requests

def check_website(website):
    try:
        response = requests.get(website)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False

def export_valid_websites(file_name):
    with open(file_name, "r") as file:
        websites = file.readlines()
    valid_websites = []
    for website in websites:
        website = website.strip()
        if check_website(website):
            valid_websites.append(website)
    with open("valid_websites.txt", "w") as file:
        for website in valid_websites:
            file.write(website + "\n")

export_valid_websites("websites.txt")
