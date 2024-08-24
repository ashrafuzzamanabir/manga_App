from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Test Scenario 1: Login Functionality
def test_login():
    driver.get("https://myalice-automation-test.netlify.app/")
    time.sleep(2)
    
    
    element = driver.find_element(By.CSS_SELECTOR, "#login-btn")
    print(element)
    assert element.text == "Login"
    time.sleep(2)
    
    # Enter valid login credentials
    driver.find_element(By.CSS_SELECTOR, "#username").send_keys("testuser")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("password")
    time.sleep(2)
    
    # Click the "Login" button
    driver.find_element(By.CSS_SELECTOR, "#login-btn").click()
    time.sleep(2)
    
    # Verify that the user is redirected to the manga search page
    Manga_search = driver.find_element(By.CSS_SELECTOR, "#manga-search")
    print(Manga_search)
    assert Manga_search.text == "Search" 
    time.sleep(2)

# Test Scenario 2: Manga Search and Display
def test_manga_search():
    # Ensure the user is on the manga search page
    assert "Manga Search" in driver.title
    
    # Search for "Naruto"
    search_box = driver.find_element(By.CSS_SELECTOR, "#manga-search")
    search_box.clear()
    search_box.send_keys("Naruto")
    driver.find_element(By.CSS_SELECTOR, ".bg-green-500 text-white py-2 px-4 rounded mr-2").click()
    time.sleep(2)
    # Verify that manga cards with the name "Naruto" are displayed
    assert "Naruto" in driver.page_source
    
    # Search for "One Piece"
    search_box.clear()
    search_box.send_keys("One Piece")
    driver.find_element(By.ID, "searchButton").click()
    time.sleep(2)
    
    
    # Search for "Seven Deadly Sins"
    search_box.clear()
    search_box.send_keys("Seven Deadly Sins")
    driver.find_element(By.ID, "searchButton").click()
    time.sleep(2)
    # Verify that manga cards with the name "Seven Deadly Sins" are displayed
    assert "Seven Deadly Sins" in driver.page_source
    
    # Search for a term that returns no results
    search_box.clear()
    search_box.send_keys("No manga found")
    driver.find_element(By.ID, "searchButton").click()
    time.sleep(2)
    # Verify that a "No manga found" message is displayed
    assert "No manga found" in driver.page_source

# Test Scenario 3: Manga Details Modal
def test_manga_details_modal():
    # Ensure the user is on the manga search page
    assert "Manga Search" in driver.title
    
    # Click the "Details" link on a manga card
    driver.find_element(By.LINK_TEXT, "Details").click()
    time.sleep(2)
    
    # Verify that the modal appears and displays the correct manga information
    assert "Manga Details" in driver.page_source
    assert "Image" in driver.page_source
    assert "Name" in driver.page_source
    assert "Summary" in driver.page_source
    
    # Click the "Close" button on the modal
    driver.find_element(By.ID, "closeButton").click()
    time.sleep(2)
    
    # Verify that the modal is closed and no longer visible
    assert "Manga Details" not in driver.page_source

# Run the tests
test_login()
test_manga_search()
test_manga_details_modal()

# Close the browser
driver.quit()
