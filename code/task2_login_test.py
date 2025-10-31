
import time
import traceback
import platform
from datetime import datetime
import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, WebDriverException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# URLs
LOGIN_URL = "https://practicetestautomation.com/practice-test-login/"

# Credentials
VALID_USER = "student"
VALID_PASS = "Password123"
INVALID_USER = "wrong"
INVALID_PASS = "wrong"

RESULTS_FILE = "task2_results.txt"
SCREENSHOT_DIR = "screenshots"

# Read headless toggle from environment (default=1 -> headless enabled)
HEADLESS = os.environ.get("HEADLESS", "1") != "0"


def _log_to_file(msg: str):
    # internal helper to avoid recursion while driver not available
    print(msg)
    with open(RESULTS_FILE, "a", encoding="utf-8") as f:
        f.write(msg + "\n")


def init_driver():
    """Initialize Chrome WebDriver using webdriver-manager with diagnostics.

    Raises WebDriverException on failure with logs written to `RESULTS_FILE`.
    """
    options = webdriver.ChromeOptions()
    if HEADLESS:
        # newer headless mode flag; if unsupported, Chrome will ignore
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("window-size=1280,800")

    try:
        _log_to_file("Initializing Chrome WebDriver...")
        driver_path = ChromeDriverManager().install()
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service, options=options)

        # attempt to log browser capabilities
        try:
            caps = driver.capabilities
            browser = caps.get("browserName")
            browser_version = caps.get("browserVersion") or caps.get("version")
            _log_to_file(f"Selenium: {webdriver.__version__} | Browser: {browser} {browser_version} | Driver: {driver_path}")
        except Exception:
            _log_to_file("Could not read driver/browser capabilities")

        return driver
    except Exception as e:
        tb = traceback.format_exc()
        _log_to_file("Failed to initialize WebDriver:")
        _log_to_file(str(e))
        _log_to_file(tb)
        _log_to_file(f"Platform: {platform.system()} {platform.release()} | Python: {platform.python_version()}")
        raise WebDriverException(f"Could not start Chrome WebDriver: {e}")


def log(msg):
    _log_to_file(msg)


def run_test(username, password, expected_success=True):
    driver = None
    result = "FAIL"
    screenshot_path = os.path.join(SCREENSHOT_DIR, f"{username}_{expected_success}.png")
    os.makedirs(SCREENSHOT_DIR, exist_ok=True)

    log(f"\n--- Test started at {datetime.now()} ---")
    log(f"Testing credentials: {username}/{password}")

    try:
        driver = init_driver()
        driver.get(LOGIN_URL)

        wait = WebDriverWait(driver, 10)
        # Wait for the username field to be present
        wait.until(EC.presence_of_element_located((By.ID, "username")))

        driver.find_element(By.ID, "username").clear()
        driver.find_element(By.ID, "username").send_keys(username)
        driver.find_element(By.ID, "password").clear()
        driver.find_element(By.ID, "password").send_keys(password)

        # click submit
        driver.find_element(By.ID, "submit").click()

        # Wait for either navigation away from the login URL or appearance of an error/success text
        wait.until(lambda d: d.current_url != LOGIN_URL or
                   "logged in" in d.page_source.lower() or
                   "success" in d.page_source.lower() or
                   "invalid" in d.page_source.lower() or
                   "error" in d.page_source.lower())

        page_src = driver.page_source.lower()

        if expected_success:
            # heuristic checks for success
            if driver.current_url != LOGIN_URL or "logged in" in page_src or "success" in page_src:
                result = "PASS"
            else:
                result = "FAIL"
        else:
            # heuristic checks for failure (stays on login page or shows error text)
            if driver.current_url == LOGIN_URL and ("invalid" in page_src or "error" in page_src):
                result = "PASS"
            else:
                result = "FAIL"

    except Exception as e:
        log(f"Exception during test: {e}")
        log(traceback.format_exc())
        result = "FAIL"
    finally:
        try:
            if driver:
                driver.save_screenshot(screenshot_path)
        except Exception:
            log("Failed to save screenshot")
        try:
            if driver:
                driver.quit()
        except Exception:
            log("Failed to quit driver cleanly")

        log(f"Result: {result}")
        log(f"Screenshot saved: {screenshot_path}")
        log("--- End of Test ---\n")


def main():
    if os.path.exists(RESULTS_FILE):
        os.remove(RESULTS_FILE)

    log("=== AI in Software Engineering - Task 2: Automated Testing ===")
    run_test(VALID_USER, VALID_PASS, expected_success=True)
    run_test(INVALID_USER, INVALID_PASS, expected_success=False)
    log(" Testing completed successfully.")


if __name__ == "__main__":
    main()
