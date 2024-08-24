from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import NoSuchElementException

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
    Manga_search = driver.find_element(By.CLASS_NAME, "text-4xl")
    print(Manga_search)
    assert Manga_search.text == "Manga You Should Read" 
    time.sleep(2)

# Test Scenario 2: Manga Search and Display
def test_manga_search():
    # Ensure the user is on the manga search page
    Manga_search = driver.find_element(By.CLASS_NAME, "text-4xl")
    print(Manga_search)
    assert Manga_search.text == "Manga You Should Read" 
    time.sleep(2)
    
    # Search for "Naruto"
    search_box = driver.find_element(By.CSS_SELECTOR, "#manga-search")
    search_box.clear()
    search_box.send_keys("Naruto")
    driver.find_element(By.CSS_SELECTOR, ".bg-green-500").click()
    time.sleep(2)
    # Verify that manga cards with the name "Naruto" are displayed
    Manga_name = driver.find_element(By.CSS_SELECTOR, "#manga-name")
    print(Manga_name)
    assert Manga_name.text == "Naruto" 
    time.sleep(2)
    
    # Search for "One Piece"
    search_box.clear()
    search_box.send_keys("One Piece")
    driver.find_element(By.CSS_SELECTOR, ".bg-green-500").click()
    time.sleep(2)
    # Verify that manga cards with the name "One Piece" are displayed
    Manga_name = driver.find_element(By.CSS_SELECTOR, "#manga-name")
    print(Manga_name)
    assert Manga_name.text == "One Piece" 
    time.sleep(2)
    
    # Search for "Seven Deadly Sins"
    search_box.clear()
    search_box.send_keys("Seven Deadly Sins")
    driver.find_element(By.CSS_SELECTOR, ".bg-green-500").click()
    time.sleep(2)
    # Verify that manga cards with the name "Seven Deadly Sins" are displayed
    try:
        Manga_name = driver.find_element(By.CSS_SELECTOR, "#manga-name")
        assert Manga_name.text == "Seven Deadly Sins"
        print("Manga card 'Seven Deadly Sins' found")
    except NoSuchElementException:
        print("Manga card 'Seven Deadly Sins' not found")
    
    # Search for a term that returns no results
    search_box.clear()
    search_box.send_keys("No manga found")
    driver.find_element(By.CSS_SELECTOR, ".bg-green-500").click()
    time.sleep(2)
    # Verify that a "No manga found" message is displayed
    Manga_name = driver.find_element(By.CSS_SELECTOR, ".text-red-500")
    print(Manga_name)
    assert Manga_name.text == "No manga found" 
    time.sleep(2)

# Test Scenario 3: Manga Details Modal
def test_manga_details_modal():
    # Ensure the user is on the manga search page
    # Manga_search = driver.find_element(By.CLASS_NAME, "text-4xl")
    # print(Manga_search)
    # assert Manga_search.text == "Manga You Should Read" 
    # time.sleep(2)
    # search_box = driver.find_element(By.CSS_SELECTOR, "#manga-search")
    # search_box.clear()
    # search_box.send_keys("Dragon Ball Z")
    # driver.find_element(By.CSS_SELECTOR, ".bg-green-500").click()
    # time.sleep(2)
    
    # # Click the "Details" link on a manga card
    # try:
    #     button = driver.find_element(By.CSS_SELECTOR, ".text-blue-500")
    #     assert button.text == "Details"
    #     driver.find_element(By.CSS_SELECTOR, ".text-blue-500").click()
    #     print("Details link found")
    #     time.sleep(2)

    #     # Verify that the modal appears and displays the correct manga information
    #     image_element = driver.find_element(By.XPATH,"img")  # Replace with the appropriate locator
    #     # Get the src attribute of the image
    #     image_src = image_element.get_attribute('src')
    #     print(image_src)
    #      # Assert that the src value is correct
    #     assert image_src == "https://res.cloudinary.com/emerging-it/image/upload/v1724240585/mangaImage/atlc7efewppsgeyr6mgu.jpg"


    # except NoSuchElementException:
    #     print("Details link not found")
    
    Manga_search = driver.find_element(By.CLASS_NAME, "text-4xl")
    print(Manga_search)
    assert Manga_search.text == "Manga You Should Read"
    time.sleep(2)
        
    search_box = driver.find_element(By.CSS_SELECTOR, "#manga-search")
    search_box.clear()
    search_box.send_keys("Bleach")
    driver.find_element(By.CSS_SELECTOR, ".bg-green-500").click()
    time.sleep(2)
        
        # Click the "Details" link on a manga card
    try:
        
        button = driver.find_element(By.CSS_SELECTOR, ".text-blue-500")
        assert button.text == "Details"
        driver.find_element(By.CSS_SELECTOR, ".text-blue-500").click()
        print("Details link found")
        time.sleep(2)
            
        # Verify that the modal appears and displays the correct manga information
        image_element = driver.find_element(By.XPATH,"//img[contains(@class,'w-full')]")  # Replace with the appropriate locator
        image_src = image_element.get_attribute('src')
        print(image_src)
        assert image_src == "https://res.cloudinary.com/emerging-it/image/upload/v1724240585/mangaImage/atlc7efewppsgeyr6mgu.jpg"
        
        man_name = driver.find_element(By.CSS_SELECTOR, ".text-xl")
        assert man_name.text == "Bleach"

        man_summury = driver.find_element(By.CSS_SELECTOR, "p.text-gray-600")
        summury = man_summury.get_attribute("textContent")
        print(summury)
        # assert summury == "A teenager gains the abilities of a Soul Reaper and must protect the living and the dead from evil spirits."


    except NoSuchElementException:
        print("Details link not found")

    
    # Click the "Close" button on the modal
    driver.find_element(By.CSS_SELECTOR, ".bg-blue-500").click()
    time.sleep(2)
    
    # Verify that the modal is closed and no longer visible
    # assert "Manga Details" not in driver.page_source

# Run the tests
test_login()
test_manga_search()
test_manga_details_modal()

# Close the browser
driver.quit()
