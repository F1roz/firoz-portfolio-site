#Story


# selenium_scraper.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramScraperSelenium:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()  # Replace with the path to your chromedriver executable
        self.login(username, password)

    def login(self, username, password):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)  # Wait for the page to load

        # Fill in login details
        username_input = self.driver.find_element("name", "username")
        password_input = self.driver.find_element("name", "password")
        username_input.send_keys(username)
        password_input.send_keys(password)

        # Submit login form
        password_input.send_keys(Keys.RETURN)
        time.sleep(5)  # Wait for login to complete

    def scrape_stories(self, target_username):
        # Implement scraping logic using Selenium
        # (This example assumes Instagram's HTML structure, which may change)
        self.driver.get(f"https://www.instagram.com/{target_username}")
        time.sleep(2)  # Wait for the page to load

        # Extract and process story elements
        story_elements = self.driver.find_elements_by_css_selector(".RR-M-.h5uC0")
        for story in story_elements:
            # Process or store the story data as needed
            print(f"Scraped Story from {target_username}: {story.get_attribute('src')}")

    def close(self):
        self.driver.quit()

# Example usage
if __name__ == "__main__":
    scraper_selenium = InstagramScraperSelenium("your_username", "your_password")
    scraper_selenium.scrape_stories("target_account_username")
    scraper_selenium.close()

#Engagement


# selenium_engagement_script.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramEngagementSelenium:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()  # Replace with the path to your chromedriver executable
        self.login(username, password)

    def login(self, username, password):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)  # Wait for the page to load

        # Fill in login details
        username_input = self.driver.find_element("name", "username")
        password_input = self.driver.find_element("name", "password")
        username_input.send_keys(username)
        password_input.send_keys(password)

        # Submit login form
        password_input.send_keys(Keys.RETURN)
        time.sleep(5)  # Wait for login to complete

    def engage_with_posts(self, target_username, num_likes=5, comment_text="Great post!"):
        # Implement engagement logic using Selenium
        self.driver.get(f"https://www.instagram.com/{target_username}")
        time.sleep(2)  # Wait for the page to load

        # Like posts
        like_buttons = self.driver.find_elements_by_css_selector(".fr66n .wpO6b")
        for button in like_buttons[:num_likes]:
            button.click()

        # Comment on posts
        comment_input = self.driver.find_element_by_css_selector(".Ypffh")
        comment_input.click()
        comment_input.send_keys(comment_text)
        comment_input.send_keys(Keys.RETURN)

    def close(self):
        self.driver.quit()

# Example usage
if __name__ == "__main__":
    engagement_selenium = InstagramEngagementSelenium("your_username", "your_password")
    engagement_selenium.engage_with_posts("target_account_username")
    engagement_selenium.close()

#Remember to adjust the paths and details based on your specific environment and requirements

#API

# social_media_scraper/selenium_scraper.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class InstagramScraperSelenium:
    def __init__(self, username, password):
        self.driver = webdriver.Chrome()  # Replace with the path to your chromedriver executable
        self.login(username, password)

    def login(self, username, password):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)  # Wait for the page to load

        # Fill in login details
        username_input = self.driver.find_element("name", "username")
        password_input = self.driver.find_element("name", "password")
        username_input.send_keys(username)
        password_input.send_keys(password)

        # Submit login form
        password_input.send_keys(Keys.RETURN)
        time.sleep(5)  # Wait for login to complete

    def scrape_stories(self, target_username):
        # Implement scraping logic using Selenium
        # (This example assumes Instagram's HTML structure, which may change)
        self.driver.get(f"https://www.instagram.com/{target_username}")
        time.sleep(2)  # Wait for the page to load

        # Extract and process story elements
        story_elements = self.driver.find_elements_by_css_selector(".RR-M-.h5uC0")
        scraped_stories = [story.get_attribute('src') for story in story_elements]

        return scraped_stories

    def close(self):
        self.driver.quit()


# social_media_scraper/api.py
from .selenium_scraper import InstagramScraperSelenium

class SocialMediaAPI:
    def __init__(self, username, password):
        self.scraper = InstagramScraperSelenium(username, password)

    def scrape_instagram_stories(self, target_username):
        """
        Initiates the scraping of Instagram Stories for a given target username.

        Parameters:
        - target_username (str): Username of the account to scrape stories from

        Returns:
        - list: List of scraped story URLs
        """
        return self.scraper.scrape_stories(target_username)

    def close_scraper(self):
        self.scraper.close()

# Example usage
if __name__ == "__main__":
    api = SocialMediaAPI("your_username", "your_password")
    scraped_stories = api.scrape_instagram_stories("target_account_username")
    
    # Process or print the scraped stories
    print("Scraped Stories:", scraped_stories)

    # Close the scraper when done
    api.close_scraper()




