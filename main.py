from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
import time

options = Options()
#prevents page from shutting down
options.add_experimental_option("detach", True)
#prevent pop up adds from appearing when the script is running
options.add_extension('uBlock.crx')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

#helper functions
def find_element(driver, locator, timeout=10):
    try:
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
    except TimeoutException:
        print(f"Error: Element with locator {locator} not found within {timeout} seconds.")

def click_element(driver, locator, timeout=10):
    element = find_element(driver, locator, timeout)
    if element:
        try:
            element.click()
        except Exception as e:
            print(f"Error: {e}")

def send_keys(driver, locator, text, timeout=10):
    element = find_element(driver, locator, timeout)
    if element:
        try:
            element.send_keys(text)
        except Exception as e:
            print(f"Error: {e}")

#1 Go to the website
driver.get("https://www.automationexercise.com")
driver.maximize_window()

#2 signing into the website(on homepage click signup/login button)
click_element(driver, (By.XPATH, "//a[@href='/login']"))

#fill in the details
send_keys(driver, (By.XPATH, "//input[@name='email']"), 'qat@mailinator.com')
send_keys(driver, (By.XPATH, "//input[@name='password']"), '123456')

# #press login button
click_element(driver, (By.XPATH, '//button[contains(text(),"Login")]'))

#3 Fetch all items and sort them as per their price [Low to High] and print it on Console [Label & Price]
featured_items_section = find_element(driver, (By.CLASS_NAME, "features_items"))

# Check if the featured items section is found on the webpage
if featured_items_section:
    # getting items within the featured items section
    apparel_items = featured_items_section.find_elements(By.CLASS_NAME, "col-sm-4")
    
    # Initialize an empty dictionary to store item labels and prices
    items_dict = {}

    # Iterate through each apparel item found
    for item in apparel_items:
        # Find the label element within the current item and get its text
        label_element = item.find_element(By.XPATH, ".//div[@class='productinfo text-center']/p")
        label = label_element.text.strip()

        # Find the price element within the current item and get its text
        price_element = item.find_element(By.XPATH, ".//div[@class='productinfo text-center']/h2")
        # Remove "Rs." from the price text and strip any surrounding whitespace
        price_text = price_element.text.replace("Rs.", "").strip()
        # Convert the price text to a float
        price = float(price_text)

        # Add the label and price to the dictionary
        items_dict[label] = price

    # Sort the items dictionary by price (values) in ascending order
    sorted_items = sorted(items_dict.items(), key=lambda x: x[1])

    # Iterate through the sorted items and print the label and price
    for item, price in sorted_items:
        # Print the label and price formatted to two decimal places
        print(f"{item}: Rs.{price:.2f}")

#4 navigating to Women> dress>women>tops and adding items to cart
#scroll to the area if out of view
women_items = find_element(driver, (By.XPATH, "//a[@href='#Women']"))
ActionChains(driver).move_to_element(women_items).perform()

#click on the women dropdown & press dress
click_element(driver, (By.XPATH, ".//span[@class='badge pull-right']")) 
time.sleep(2)
click_element(driver, (By.XPATH, "//a[@href='/category_products/1']"))

#click on the women dropdown & press tops
click_element(driver, (By.XPATH, ".//span[@class='badge pull-right']")) 
time.sleep(2)
click_element(driver, (By.XPATH, "//a[@href='/category_products/2']"))

# Select the Fancy Green Top and add to cart.
fancy_green_top = find_element(driver, (By.XPATH, ".//div[@class='productinfo text-center']/p[text()='Fancy Green Top']"))
if fancy_green_top:
    fancy_green_top_container = fancy_green_top.find_element(By.XPATH, "./..")  # Get the parent container
    add_to_cart_button = fancy_green_top_container.find_element(By.CSS_SELECTOR, "a.add-to-cart")  # Use CSS selector
    time.sleep(3)
    add_to_cart_button.click()

# Select Summer White Top and add to cart as well.
summer_white_top = find_element(driver, (By.XPATH, ".//div[@class='productinfo text-center']/p[text()='Summer White Top']"))
if summer_white_top:
    summer_white_top_container = summer_white_top.find_element(By.XPATH, "./..")  # Get the parent container
    add_to_cart_button = summer_white_top_container.find_element(By.CSS_SELECTOR, "a.add-to-cart")  # Use CSS selector
    add_to_cart_button.click()

#5 view items in cart

click_element(driver, (By.XPATH, "//a[@href='/view_cart']"))
time.sleep(3)
#proceed to checkout
click_element(driver, (By.XPATH, "//a[@class='btn btn-default check_out']"))
time.sleep(2)
#add comment "order placed"
send_keys(driver, (By.XPATH, "//textarea[@class='form-control']"), "Order placed.")
time.sleep(2)
#click on place order button
click_element(driver, (By.XPATH, "//a[@class='btn btn-default check_out']"))
time.sleep(2)
#enter card details
send_keys(driver, (By.XPATH, "//input[@name='name_on_card']"), "Test Card")
send_keys(driver, (By.XPATH, "//input[@name='card_number']"), "4100 0000 0000")
send_keys(driver, (By.XPATH, "//input[@name='cvc']"), "123")
send_keys(driver, (By.XPATH, "//input[@name='expiry_month']"), "01")
send_keys(driver, (By.XPATH, "//input[@name='expiry_year']"), "1900")

time.sleep(2)
#press pay and confirm button to finish payment process
click_element(driver, (By.XPATH, "//button[contains(text(), 'Pay and Confirm Order')]"))

#6 confirm the order is placed
success_message = find_element(driver, (By.XPATH, "//p[contains(text(), 'Congratulations! Your order has been confirmed!')]"))
if success_message:
    print("Order has been placed successfully.")
