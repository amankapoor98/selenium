from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
import time
from selenium.webdriver.common.keys import Keys
from datetime import datetime as dt

driver_path = "C:\\Users\\v-amanlnu\\Downloads\\edgedriver_win64\\msedgedriver.exe"
service = EdgeService(executable_path=driver_path)

def get_driver_home():
    options=webdriver.EdgeOptions()
    options.add_argument("disable-Infobars")
    options.add_argument("start-maximized")
    options.add_argument("disable-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_argument("disable-link-features=AutomationControlled")
    driver=webdriver.Edge(service=service, options=options)
    driver.get("https://vnext.s360.msftcloudes.com/blades/security?blade=KPI:527fb616-07aa-8198-6419-50d04ef1c2f3~SLA:3~AssignedTo:AssignedToServices~Forums:All~waves:All~KPI%20Ranking:All~Tab:Summary~_loc:Security&peopleBasedNodes=sonala_team&global=@SONALA%2BSonal%20Agarwal%20(SONALA)")
    return driver

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import json

extracted_results = []

def process_url(driver, url, original_url):
    wait = WebDriverWait(driver, 10)
    # Navigate to the new URL
    print(f"Navigating to URL: {url}")
    driver.get(url)
    time.sleep(5)

    # Check for VPN Connection Required popup and approve if present
    try:
        approve_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Approve and Continue')]")))
        if approve_button.is_displayed():
            print("VPN Connection Required popup detected. Approving and continuing...")
            approve_button.click()
            time.sleep(5)  # Wait for the page to proceed after approval
    except Exception as e:
        print(f"VPN popup not found or timeout reached: {e}")
        # Popup not present, continue normally
        pass

    # New extraction logic as per user instructions
    print("Running new extraction logic on new URL")
    time.sleep(30)
    # Scroll to the bottom of the page to load all content
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait for any lazy-loaded content to load
    time.sleep(30)
    extracted_data = []
    try:
        grids = driver.find_elements(By.CSS_SELECTOR, 'div[role="grid"]')
        table_count = 0
        for grid in grids:
            rows = grid.find_elements(By.CSS_SELECTOR, 'div[role="row"]')
            row_index_set = set()
            for row in rows:
                row_index = row.get_attribute("row-index")
                if row_index is None:
                    continue
                if row_index == "0":
                    table_count += 1
                # Collect row indexes to check existence
                row_index_set.add(int(row_index))
                if table_count == 3:
                    row_data = {}
                    col_ids = ["VulnerabilityName", "RoleName", "SubscriptionName"]
                    for col_id in col_ids:
                        try:
                            # Extract value and ensure no empty string for SubscriptionName
                            value = row.find_element(By.CSS_SELECTOR, f'div[col-id="{col_id}"] div.cf-wrapper span.cf-content').text.strip()
                            if col_id == "SubscriptionName" and not value:
                                value = "UNKNOWN_SUBSCRIPTION"
                        except Exception:
                            value = "UNKNOWN_SUBSCRIPTION" if col_id == "SubscriptionName" else ""
                        row_data[col_id] = value
                        # Save each col-id value to separate file, avoid writing empty lines
                        # Skip writing SubscriptionName to file as per user request
                        if col_id != "SubscriptionName":
                            filename = f"{col_id}.txt"
                            if value and value != "UNKNOWN_SUBSCRIPTION":
                                with open(filename, "a", encoding="utf-8") as f:
                                    f.write(value + "\n")
                    # Remove SubscriptionName from row_data before appending to extracted_data
                    if "SubscriptionName" in row_data:
                        del row_data["SubscriptionName"]
                    extracted_data.append(row_data)
            # After processing rows, iterate row-index from 0 until no more rows exist
            current_index = 0
            while current_index in row_index_set:
                # Here you can add logic to extract data from each row by row-index if needed
                current_index += 1
            print(f"Processed {current_index} rows in table {table_count}")
        # Filter extracted_data if any SubscriptionName is "SYSTEM CENTER BUILDS IDC"
        subscription_filter = "SYSTEM CENTER BUILDS IDC"
        filtered_data = extracted_data
        if any(item.get("SubscriptionName") == subscription_filter for item in extracted_data):
            filtered_data = [item for item in extracted_data if item.get("SubscriptionName") == subscription_filter]

        # Append filtered data to global results and print
        extracted_results.extend(filtered_data)
        print(f"Extracted data for URL {url}:")
        for item in filtered_data:
            print(item)

        # Save extracted results to JSON file named by run date
        run_date = dt.now().strftime("%Y-%m-%d")
        json_filename = f"{run_date}.json"
        with open(json_filename, "w", encoding="utf-8") as f:
            json.dump(extracted_results, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error during extraction: {e}")
    

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape(driver):
    wait = WebDriverWait(driver, 30)  # Wait up to 30 seconds for elements
    time.sleep(5)  # Initial wait for page to load
    comp_id = 886
    increment = 23
    original_url = "https://vnext.s360.msftcloudes.com/blades/security?blade=KPI:527fb616-07aa-8198-6419-50d04ef1c2f3~SLA:3~AssignedTo:AssignedToServices~Forums:All~waves:All~KPI%20Ranking:All~Tab:Summary~_loc:Security&peopleBasedNodes=sonala_team&global=@SONALA%2BSonal%20Agarwal%20(SONALA)"
    max_retries = 3
    max_iterations = 10  # Limit the number of comp-id iterations to avoid infinite loop
    iteration_count = 0

    while iteration_count < max_iterations:
        retries = 0
        while retries < max_retries:
            try:
                # Wait for the element with the current comp-id to be present on the original URL page
                driver.get(original_url)
                element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f'div[comp-id="{comp_id}"]')))
                # Extract the URL from the anchor tag inside the span
                anchor = element.find_element(By.CSS_SELECTOR, "span a[target='_blank']")
                url = anchor.get_attribute("href")
                print(f"Found comp-id {comp_id} with URL: {url}")
                # Call the common function to process the URL
                process_url(driver, url, original_url)
                # Increment comp_id by 23 for next iteration
                comp_id += increment
                iteration_count += 1
                break  # Exit retry loop on success
            except Exception as e:
                print(f"Attempt {retries+1} failed for comp-id {comp_id}: {e}")
                retries += 1
                if retries == max_retries:
                    print(f"Max retries reached for comp-id {comp_id}. Stopping execution.")
                    # Removed screenshot saving as per user request
                    # Stop execution instead of continuing
                    return

def main():
    driver = get_driver_home()
    scrape(driver)
    # Remove print(driver.current_url) to avoid error if window is closed
    time.sleep(10)

if __name__ == "__main__":
    main()
