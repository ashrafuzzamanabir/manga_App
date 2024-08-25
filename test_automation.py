import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

# Pytest fixture to set up and tear down the WebDriver instance
@pytest.fixture(scope="module")
def driver():
    # Initialize the Chrome driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()

# Test Scenario 1: Login Functionality
def test_login(driver):
    driver.get("https://myalice-automation-test.netlify.app/")
    time.sleep(2)
    
    # Wait for the login button to be clickable
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#login-btn"))
    )
    time.sleep(2)
    # Verify the login button text
    assert login_button.text == "Login"
    
    # Enter valid login credentials
    driver.find_element(By.CSS_SELECTOR, "#username").send_keys("testuser")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("password")
    time.sleep(2)
    # Click the "Login" button
    login_button.click()
    
    # Verify that the user is redirected to the manga search page
    manga_search = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "text-4xl"))
    )
    assert manga_search.text == "Manga You Should Read"
    time.sleep(2)
# Test Scenario 2: Manga Search and Display
def test_manga_search(driver):
    # Ensure the user is on the manga search page
    manga_search = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "text-4xl"))
    )
    assert manga_search.text == "Manga You Should Read"
    time.sleep(2)
    search_terms = ["Naruto", "One Piece", "Seven Deadly Sins", "No manga found"]
    
    for term in search_terms:
        # Search for the manga
        search_box = driver.find_element(By.CSS_SELECTOR, "#manga-search")
        search_box.clear()
        search_box.send_keys(term)
        driver.find_element(By.CSS_SELECTOR, ".bg-green-500").click()
        time.sleep(2)
        # Verify that the appropriate manga card or message is displayed
        if term == "No manga found":
            no_manga_message = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".text-red-500"))
            )
            assert no_manga_message.text == "No manga found"
            time.sleep(2)
        else:
            manga_name = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, "#manga-name"))
            )
            assert manga_name.text == term
            time.sleep(2)

# Test Scenario 3: Manga Details Modal
def test_manga_details_modal(driver):
    # Ensure the user is on the manga search page
    manga_search = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "text-4xl"))
    )
    assert manga_search.text == "Manga You Should Read"
    time.sleep(2)
    # Search for "Bleach"
    search_box = driver.find_element(By.CSS_SELECTOR, "#manga-search")
    search_box.clear()
    search_box.send_keys("Bleach")
    driver.find_element(By.CSS_SELECTOR, ".bg-green-500").click()
    time.sleep(2)
    # Click the "Details" link on a manga card
    try:
        details_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".text-blue-500"))
        )
        assert details_button.text == "Details"
        details_button.click()
        time.sleep(2)
        # Verify that the modal appears and displays the correct manga information
        image_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//img[contains(@class,'w-full')]"))
        )
        image_src = image_element.get_attribute('src')
        assert image_src == "https://res.cloudinary.com/emerging-it/image/upload/v1724240585/mangaImage/atlc7efewppsgeyr6mgu.jpg"
        time.sleep(2)
        manga_name = driver.find_element(By.CSS_SELECTOR, ".text-xl")
        assert manga_name.text == "Bleach"
        time.sleep(2)
        manga_summary = driver.find_element(By.CSS_SELECTOR, "p.text-gray-600")
        summary_text = manga_summary.get_attribute("textContent")
        print(summary_text)
        # assert summary_text == "Expected summary here"
        time.sleep(2)
    except NoSuchElementException:
        print("Details link not found")
    
    # Click the "Close" button on the modal
    close_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".bg-blue-500"))
    )
    close_button.click()
    time.sleep(2)
    # Verify that the modal is closed and no longer visible
    manga_search2 = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "text-4xl"))
    )
    assert manga_search2.text == "Manga You Should Read"
    time.sleep(2)
