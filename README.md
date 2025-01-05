# HTML Page Recorder with Cookies

This project provides a Python script that uses **Selenium** to load a web page with cookies from a file and continuously monitors for changes. If the page changes, the updated HTML is saved with a timestamped filename.

## Features

- Load cookies from a Netscape HTTP cookie file.
- Monitor a web page for changes without reloading it.
- Save the HTML source of the page whenever it changes.
- Customizable to work with dynamic web pages and specific selectors.
- Uses **Selenium** WebDriver to interact with the page.

## Requirements

- Python 3.6 or higher
- Selenium
- WebDriver Manager for Chrome
- Chrome browser (ensure it's installed)
- A valid Netscape HTTP cookie file

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/yourusername/html-page-recorder.git
   cd html-page-recorder
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
2. Install the required packages:

   ```
   pip install -r requirements.txt
   ```
4. Ensure that Google Chrome is installed and the path to the Chrome binary is correct in the script.
5. Place your cookies.txt file (Netscape HTTP Cookie File format) in the project directory.

## Usage

1. Edit the script main.py to point to your cookies.txt file and update the url variable with the target page.

2. Run the script:

    ```
    python main.py
    ```

3. The script will start monitoring the page. If a change is detected, the updated HTML page will be saved with a timestamped filename, e.g., rendered_page_20250105_120505.html.

4. The script will continue running indefinitely until manually stopped (e.g., via CTRL + C).

## Troubleshooting
### "Error waiting for the element"

If you encounter the error "Error waiting for the element" when trying to wait for a dynamic element to load, it might be due to the page taking longer to load or the element being unavailable at the time.

To resolve this:
increase the Wait Timeout: In the script, locate the WebDriverWait section where the page waits for the dynamic element. Increase the timeout value to allow the page more time to load.
For example, change the timeout from 20 seconds to 60 seconds:

    WebDriverWait(driver, 60).until(
       EC.presence_of_element_located((By.CSS_SELECTOR, ".dynamic-class"))
    )
    
## License

This project is licensed under the MIT License - see the LICENSE file for details.
## Contributing

Feel free to fork the repository and submit issues or pull requests. Contributions are welcome!
