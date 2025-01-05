import time
import hashlib
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from datetime import datetime
from webdriver_manager.chrome import ChromeDriverManager

# Function to load cookies from a Netscape cookie file
def load_cookies(file_path):
    cookies = []
    with open(file_path, 'r') as file:
        for line in file:
            if line.startswith('#') or not line.strip():
                continue  # Skip comments and empty lines
            parts = line.strip().split('\t')
            if len(parts) == 7:
                cookies.append({
                    "domain": parts[0],
                    "httpOnly": parts[3] == "TRUE",
                    "path": parts[2],
                    "secure": parts[3] == "TRUE",
                    "expiry": int(parts[4]) if parts[4].isdigit() else None,
                    "name": parts[5],
                    "value": parts[6],
                })
    return cookies

# Function to calculate hash of a string
def calculate_hash(content):
    return hashlib.md5(content.encode("utf-8")).hexdigest()

# Path to your cookie file
cookie_file_path = "cookies.txt"

# Load cookies from the file
cookies = load_cookies(cookie_file_path)

options = webdriver.ChromeOptions()

# Path to Chrome binary (if needed)
chrome_binary_path = "/usr/bin/google-chrome"
options.binary_location = chrome_binary_path

# Create service for ChromeDriver
service = Service(ChromeDriverManager().install())

# Create the browser instance
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the target page
url = "example.com"
driver.get(url)

# Add cookies to the browser
for cookie in cookies:
    try:
        driver.add_cookie(cookie)
    except Exception as e:
        print(f"Failed to add cookie: {cookie}, Error: {e}")

# Refresh the page to use the cookies
driver.refresh()

# Initialize previous hash
previous_hash = None

# Start monitoring loop
try:
    while True:
        # Wait for a specific dynamic element to load (adjust the selector)
        try:
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".dynamic-class"))
            )
        except Exception as e:
            print(f"Error waiting for the element: {e}")

        # Get the current page source
        current_page_source = driver.page_source

        # Calculate the current hash
        current_hash = calculate_hash(current_page_source)

        # Check if the page has changed
        if current_hash != previous_hash:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"rendered_page_{timestamp}.html"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(current_page_source)
            print(f"Page changed! Rendered page saved as: {filename}")

            # Update the previous hash
            previous_hash = current_hash
        else:
            print("No changes detected.")

        # Wait before checking again (e.g., 30 seconds)
        time.sleep(63)

except KeyboardInterrupt:
    print("Monitoring stopped by user.")

# Close the browser
driver.quit()
