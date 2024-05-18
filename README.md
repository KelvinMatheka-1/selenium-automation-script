
# Selenium Automation Script for AutomationExercise

This README provides instructions for setting up and running the Selenium automation script for testing the AutomationExercise website. The script performs various actions including signing in, fetching items, sorting them, adding items to the cart, and placing an order on the "https://www.automationexercise.com" website.

### Overview

The script automates the following tasks:
1. Login to the website.
2. Sort and print the featured items by price (low to high).
3. Navigate through the Women's section and add specific items to the shopping cart.
4. View the shopping cart, proceed to checkout, and simulate making a payment.
5. Confirm the order placement.

### Requirements
- Python 3.x
- Selenium library
- ChromeDriver
- uBlock Extension (uBlock.crx)

### Setup Instructions

1. **Python Installation:**
   Ensure that Python 3.x is installed on your machine. You can download it from the official Python [website](https://www.python.org/downloads/).

2. **Selenium Installation:**
   Install the Selenium package using pip:
   ```
   pip install selenium
   ```

3. **ChromeDriver Setup:**
   The script uses `webdriver-manager` to handle the driver for Chrome. Install it using pip:
   ```
   pip install webdriver-manager
   ```

4. **uBlock Extension Setup:**
   - The `uBlock.crx` file is used to block ads during the automation process.
   - Download the `.crx` file for uBlock from a reliable source or extract it from an already installed extension in Chrome.
   - Place the `uBlock.crx` file in the same directory as your script.

### Script Walkthrough

- **Initialization:**
  The script begins by initializing a ChromeDriver session with options to detach and include the uBlock extension.

- **Login:**
  It navigates to the login page of "https://www.automationexercise.com", fills in the credentials, and logs in.

- **Fetch, Sort, and Print Items:**
  Retrieves items from the 'Featured Items' section, sorts them by price, and prints each item's name alongside its price.

- **Add Items to Cart:**
  Moves through different categories (Women>Dress>Women>Tops), selects specific items ('Fancy Green Top' and 'Summer White Top'), and adds them to the cart.

- **Checkout Process:**
  Views the cart, proceeds to checkout, and fills out the necessary details for payment simulation.

- **Order Confirmation:**
  Confirms that the order has been successfully placed by checking for the presence of a confirmation message.

### Running the Script

To run the script, use the following command in the terminal:
```
python3 main.py
```
Replace `<script_name>` with the actual name of your Python file.

### Note:
Ensure that the details in the script (like login credentials or product names) are accurate as per the current scenario on 
"https://www.automationexercise.com" for successful execution.

For any updates to the website's layout or element classes/identifiers, you may need to update the corresponding locators in the script.
