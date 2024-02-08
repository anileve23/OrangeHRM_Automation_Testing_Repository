from selenium import webdriver
from login_page import LoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pyautogui

def test_add_new_employee():
    # Clicking the PIM link
    pim_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="PIM"]')))
    pim_link.click()
    time.sleep(2)

    # Clicking the 'Add Employee' button
    add_employee_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Add Employee"]')))
    add_employee_button.click()
    time.sleep(2)

    # Filling employee information
    first_name_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'firstName')))
    first_name_field.send_keys("Jonas")
    time.sleep(2)

    middle_name_field = driver.find_element(By.NAME, 'middleName')
    middle_name_field.send_keys("Petras")
    time.sleep(2)

    last_name_field = driver.find_element(By.NAME, 'lastName')
    last_name_field.send_keys("Agurkėlis")
    time.sleep(2)

    employee_id_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div[2]/div[1]/div[2]/div/div/div[2]/input')))
    employee_id_field.send_keys(Keys.CONTROL + "a")  # Select all text in the field
    employee_id_field.send_keys(Keys.DELETE)         # Delete the selected text
    employee_id_field.send_keys("0123")              # Enter the new value
    time.sleep(2)

    create_login_details = driver.find_element(By.CLASS_NAME, 'oxd-switch-input')
    create_login_details.click()
    time.sleep(2)

    # Filling login details
    username_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.oxd-input[autocomplete="off"]')))
    username_field.send_keys("Jonass")
    time.sleep(2)

    password_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input.oxd-input[type="password"][autocomplete="off"]')))
    password_field.send_keys("agurkėlis123")
    time.sleep(2)

    # Confirming password
    confirm_password_input = driver.execute_script('''
    return document.querySelector("#app > div.oxd-layout > div.oxd-layout-container > div.oxd-layout-context > div > div > form > div.orangehrm-employee-container > div.orangehrm-employee-form > div.oxd-form-row.user-password-row > div > div:nth-child(2) > div > div:nth-child(2) > input");
    ''')
    confirm_password_input.send_keys("agurkėlis123")
    time.sleep(2)

    # Adding photo
    add_photo_button = driver.find_element(By.CLASS_NAME, 'employee-image-action')
    add_photo_button.click()
    time.sleep(2)
    file_path = r"C:\Users\Evuliuks\Desktop\3prakuzd\employee.jpg"
    pyautogui.write(file_path)
    pyautogui.press('enter')
    time.sleep(2)

    # Saving employee form
    save_form = driver.find_element(By.CSS_SELECTOR, 'form')
    save_form.submit()
    time.sleep(5)

    # Clicking on Job navigation button
    job_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Job"]')))
    job_link.click()
    time.sleep(2)

    # Clicking on Calendar icon
    calendar_icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'i.oxd-icon.bi-calendar.oxd-date-input-icon')))
    calendar_icon.click()
    time.sleep(2)

    #Clicking on date of 2023-12-05
    date_2023_12_05 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="oxd-date-input-calendar"]//div[text()="5"]')))
    date_2023_12_05.click()
    time.sleep(2)

    #Clicking on dropdown of job title
    dropdown_arrow = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.oxd-select-text--after > i.oxd-icon.bi-caret-down-fill')))
    dropdown_arrow.click()
    time.sleep(2)

    #Clicking on option Chief Financial Officer
    cfo_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@role="option" and .//span[text()="Chief Financial Officer"]]')))
    cfo_option.click()
    time.sleep(2)

    # Clicking on dropdown of job category
    job_category_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[4]/div/div[2]/div/div/div[1]')))
    job_category_dropdown.click()
    time.sleep(1)

    #Clicking on option Craft Workers
    craft_workers_option = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//div[@role="option"]/span[text()="Sales Workers"]')))
    craft_workers_option.click()
    time.sleep(1)

    # Clicking on dropdown for Location
    dropdown_icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[6]/div/div[2]/div/div/div[2]/i')))
    dropdown_icon.click()
    time.sleep(1)

    #Clicing on option New York Sales Office
    ny_sales_office_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@role="option"]/span[text()="New York Sales Office"]')))
    ny_sales_office_option.click()
    time.sleep(1)

    #Clicking on dropdown of Employment status
    dropdown_icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[7]/div/div[2]/div/div/div[2]/i')))
    dropdown_icon.click()
    time.sleep(1)

    #Clicking on option full time permanent
    full_time_permanent_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@role="option"]/span[text()="Full-Time Permanent"]')))
    full_time_permanent_option.click()
    time.sleep(1)

    # Clicking on save button
    saving_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/button')))
    saving_button.click()
    time.sleep(3) 

    # Clicing on Report to button
    buttonn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[9]/a')))
    buttonn.click()
    time.sleep(2)

    #Clicking the button to add Supervisor
    buttonn2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/div/button')))
    buttonn2.click()
    time.sleep(2)

    #Finding the field of supervisor and writing in the name Odis
    supervisor_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Type for hints...']")))
    supervisor_input.send_keys("Odis")
    time.sleep(2)

    #Clicking on dropdown option Odis Adalwin
    dropdown = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.oxd-autocomplete-dropdown[data-v-3ebc98ba][data-v-390abb6d]')))
    suggestion = WebDriverWait(dropdown, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Odis  Adalwin']")))
    suggestion.click()
    time.sleep(2)

    #Clicking on dropdown of reporting method
    dropdown2 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/div/div/div[2]/i")))
    dropdown2.click()
    time.sleep(2)

    #Clicking on dropdown option direct
    direct_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Direct']")))
    direct_option.click()
    time.sleep(2)

    # Saving the employee record
    savee_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div[1]/form/div[2]/button[2]')))
    savee_button.click()
    time.sleep(5)

    # Clicking on Employee list
    employee_list = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/a')))
    employee_list.click()
    time.sleep(2) 

    # Clicking the dropdown of employment status
    dropdown_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[3]/div/div[2]/div/div/div[2]/i')))
    dropdown_element.click()
    time.sleep(2)

    # Clicking the fulltime permanent
    specific_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@role="option" and .//span[text()="Full-Time Permanent"]]')))
    specific_option.click()
    time.sleep(2)

    # Locating and filling the supervisors name field
    specified_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[5]/div/div[2]/div/div/input')))
    specified_field.send_keys("Odis")
    time.sleep(2)

    # Clicking the dropdown option Odis Adalwin
    dropdown3_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Odis  Adalwin']")))
    dropdown3_option.click()
    time.sleep(2)

    #Clicking on search button
    search_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]')))
    search_button.click()

    # Scroll to the bottom of the page
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    # Find the element by ID
    employee_id = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[text()="0123"]'))
    )
    time.sleep(3)

    print("Employee found successfully!")

def test_edit_new_employee():
    # Clicking on the button to edit employee details
    edit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[3]/div/div[9]/div/button[2]/i')))
    edit_button.click()
    time.sleep(2)

    # Finding and typing in the field for middle name with "Agurkiukas"
    middle_name_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div[2]/div/div/div[2]/input')))
    middle_name_field.clear()
    middle_name_field.send_keys("Agurkiukas")
    time.sleep(2)

    # Typing in the employee ID field with "01233"
    employee_id_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[1]/div[2]/div/div[2]/input')))
    employee_id_field.clear()
    employee_id_field.send_keys("01233")
    time.sleep(2)

    # Typing in the field for SSN with "54545444"
    ssn_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[1]/div/div[2]/input')))
    ssn_field.clear()
    ssn_field.send_keys("54545444")
    time.sleep(2)

    # Clicking on the calendar icon and setting the date to "2023-12-30"
    calendar_icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[2]/div[2]/div/div[2]/div/div/i')))
    calendar_icon.click()
    time.sleep(1)
    date_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="oxd-date-input-calendar"]//div[text()="30"]')))
    date_field.click()
    time.sleep(2)

    # Typing in the field for driver's license with "45849465"
    driver_license_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[1]/div/div[2]/input')))
    driver_license_field.clear()
    driver_license_field.send_keys("45849465")
    time.sleep(2)

    # Typing in the field for SSN with "541651"
    ssn_2_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div[3]/div[2]/div/div[2]/input')))
    ssn_2_field.clear()
    ssn_2_field.send_keys("541651")
    time.sleep(2)

    # Clicking on the dropdown for Nationality and choosing "American"
    nationality_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[1]/div/div[2]/div/div/div[2]/i')))
    nationality_dropdown.click()
    time.sleep(1)
    nationality_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="American"]')))
    nationality_option.click()
    time.sleep(2)

    # Clicking on the dropdown for Marital Status and choosing "Single"
    marital_status_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[1]/div[2]/div/div[2]/div/div/div[2]/i')))
    marital_status_dropdown.click()
    time.sleep(1)
    marital_status_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Single"]')))
    marital_status_option.click()
    time.sleep(2)

    dob_input_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[1]/div/div[2]/div/div/input')))
    dob_input_field.clear()  # Clear any existing value
    dob_input_field.send_keys("1989-02-15")

    # Clicking on the "Female" gender option
    gender_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[3]/div[2]/div[2]/div/div[2]/div[1]/div[2]/div/label/span')))
    gender_option.click()
    time.sleep(2)

    # Typing in the field for SSN with "America marine"
    description_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[1]/div/div[2]/input')))
    description_field.clear()
    description_field.send_keys("America marine")
    time.sleep(2)

    # Clicking on the "Yes" option for the smoker
    smoker_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[4]/div/div[2]/div/div[2]/div/label/span')))
    smoker_option.click()
    time.sleep(2)

    # Clicking on the save button
    save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[5]/button')))
    save_button.click()
    time.sleep(2)

    # Clicking on the dropdown for Blood Type and choosing "Blood B+"
    blood_type_dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[1]/div/div/div/div[2]/div/div/div[2]/i')))
    blood_type_dropdown.click()
    time.sleep(1)
    blood_type_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="B+"]')))
    blood_type_option.click()
    time.sleep(2)

    # Clicking on the second save button
    second_save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/form/div[2]/button')))
    second_save_button.click()
    time.sleep(2)

    # Clicking on the Attachments button
    attachment_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div/button')))
    attachment_button.click()
    time.sleep(2)

    # Clicking on the button to activate the file input
    file_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/form/div[1]/div/div/div/div[2]/div/div[1]')))
    file_button.click()
    time.sleep(2)

    # Attaching the file by sending keys to the file input element
    file_path = r"C:\Users\Evuliuks\Desktop\Testavimas\3prakuzd\sample.pdf"
    pyautogui.write(file_path)
    pyautogui.press('enter')
    time.sleep(2)
    
    # Clicking on the third save button
    third_save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/form/div[3]/button[2]')))
    third_save_button.click()
    time.sleep(2)

    # Clicking on the Attachments button again
    attachment_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[1]/div/button')))
    attachment_button.click()
    time.sleep(2)

    # Clicking on the button to activate the file input again
    file_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/form/div[1]/div/div/div/div[2]/div/div[1]')))
    file_button.click()
    time.sleep(2)

    # Attaching the file by sending keys to the file input element
    file_path = r"C:\Users\Evuliuks\Desktop\Testavimas\3prakuzd\test.txt"
    pyautogui.write(file_path)
    pyautogui.press('enter')
    time.sleep(2)
    
    # Clicking on the third save button again
    third_save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/form/div[3]/button[2]')))
    third_save_button.click()
    time.sleep(2)

    # Clicking on the specific button
    specific_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[3]/div/div[2]/div[1]/div/div[8]/div/button[1]')))
    specific_button.click()
    time.sleep(2)

    # Locating the text area and sending keys
    text_area = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/form/div[3]/div/div/div/div[2]/textarea')))
    text_area.send_keys("Checking the edit button")

    # Clicking on the third save button again
    third1_save_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div/form/div[4]/button[2]')))
    third1_save_button.click()
    time.sleep(2)

    # Clicking on the download button
    download1_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[3]/div/div[2]/div/div/div[8]/div/button[3]")))
    download1_button.click()
    time.sleep(4)

    # Clicking on the delete button
    delete_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/div/div[2]/div[3]/div[3]/div/div[2]/div/div/div[8]/div/button[2]")))
    delete_button.click()

    # Clicking on the delete button
    delete_yes_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"app\"]/div[3]/div/div/div/div[3]/button[2]")))
    delete_yes_button.click()
    time.sleep(4)

    print("Employee edited successfully!")

def test_add_new_candidate():

    # Clicking on the recruitment button
    recruitment_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[5]/a')))
    recruitment_button.click()
    time.sleep(2)

    # Clicking on the add button
    add_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button')))
    add_button.click()
    time.sleep(2)

    # Sending keys to input fields
    first_name_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div[1]/div[2]/input')))
    first_name_input.send_keys("Artūras")
    time.sleep(2)

    last_name_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div[2]/div[2]/input')))
    last_name_input.send_keys("Tomas")
    time.sleep(2)

    middle_name_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/div[3]/div[2]/input')))
    middle_name_input.send_keys("Nežiniukas")
    time.sleep(2)

    # Clicking on the dropdown
    dropdown = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/div/div/div[2]/i')))
    dropdown.click()
    time.sleep(2)

    junior_option = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Junior Account Assistant"]')))
    junior_option.click()
    time.sleep(2)

    # Sending keys to email and phone input fields
    email_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/input')))
    email_input.send_keys("neziniukas@gmail.com")
    time.sleep(2)

    phone_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div/div[2]/input')))
    phone_input.send_keys("86555515")
    time.sleep(2)

    # Clicking on the button to activate the file input again
    file_buttonn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[4]/div/div/div/div/div[2]/div/div[1]')))
    file_buttonn.click()
    time.sleep(2)

    # Attaching the file by sending keys to the file input element
    file_path = r"C:\Users\Evuliuks\Desktop\Testavimas\3prakuzd\sample.pdf"
    pyautogui.write(file_path)
    pyautogui.press('enter')
    time.sleep(2)

    # Clicking on save button
    saving_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[8]/button[2]')))
    saving_button.click()
    time.sleep(2)

    # Clicking the Shortlist button
    shortlist_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div[1]/form/div[2]/div[2]/button[2]')))
    shortlist_button.click()
    time.sleep(2)

    # Locating the textarea and sending keys
    textarea_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div/div/div[2]/textarea')))
    textarea_element.send_keys("This is first candidate")
    time.sleep(2)

    # Clicking on save button
    saveee_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]')))
    saveee_button.click()
    time.sleep(2)

    # Clicking the button for interview
    buttton_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div[1]/form/div[2]/div[2]/button[2]')))
    buttton_element.click()
    time.sleep(2)

    # Sending keys to the input field
    inpuut_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input')))
    inpuut_field.send_keys("Account Assistant Interview")
    time.sleep(2)

    #Finding the field of interviewer and writing in the name Odis
    interviewer_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div/div[2]/div/div/input')))
    interviewer_input.send_keys("Odis")
    time.sleep(2)

    #Clicking on dropdown option Odis Adalwin
    dropdowwn = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.oxd-autocomplete-dropdown[data-v-3ebc98ba][data-v-390abb6d]')))
    suggestion = WebDriverWait(dropdowwn, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Odis  Adalwin']")))
    suggestion.click()
    time.sleep(2)

    # Clicking on the calendar icon and setting the date to "2023-12-30"
    calendarrr_icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[3]/div/div[2]/div/div/i')))
    calendarrr_icon.click()
    time.sleep(1)
    dateee_field = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//div[@class="oxd-date-input-calendar"]//div[text()="29"]')))
    dateee_field.click()
    time.sleep(2)

   # Clicking on the watch icon
    watch_icon = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[4]/div/div[2]/div/div[1]/i')))
    watch_icon.click()

    # Locating the textarea element and sending keys
    textareaa_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[5]/div/div[2]/textarea')))
    textareaa_element.send_keys("This is a promising candidate")

    # Clicking on the save button
    savve_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app"]/div[1]/div[2]/div[2]/div/div/form/div[3]/button[2]')))
    savve_button.click()

    print("Candidate added successfully!")

def test_add_new_message():

    # Click on the first button
    afirst_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[12]/a')))
    afirst_button.click()
    time.sleep(2)

    # Typing a message in a text area
    teextaarea = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//textarea[@class="oxd-buzz-post-input"]')))
    teextaarea.send_keys("How is your Monday?")
    time.sleep(2)
    
    # Clicking on the element to upload a photo
    photooo_upload = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'oxd-glass-button') and contains(text(), 'Share Photos')]")))
    photooo_upload.click()

    #add photo
    add_photo_button = driver.find_element(By.XPATH, "//i[contains(@class, 'oxd-icon') and contains(@class, 'bi-images') and contains(@class, 'orangehrm-photo-upload-icon')]")
    add_photo_button.click()
    time.sleep(2)
    file_path = r"C:\Users\Evuliuks\Desktop\Testavimas\3prakuzd\atsisiusti.jpg"
    pyautogui.write(file_path)
    pyautogui.press('enter')
    time.sleep(2)
    
    #clicking share button
    share_button = driver.find_element(By.CSS_SELECTOR, 'div.oxd-overlay.oxd-overlay--flex.oxd-overlay--flex-centered > div > div > div > form > div.oxd-form-actions.orangehrm-buzz-post-modal-actions > button')
    # Click the button
    share_button.click()
    time.sleep(2)

    # Find like button and click it using XPath
    like_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "heart")))
    # Click on the 'heart' element
    like_button.click() 
    time.sleep(2)

    # Find the comment and click it using XPath
    comment_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "oxd-icon.bi-chat-text-fill")))
    comment_button.click()
    time.sleep(2)

    # Find the comment input field and send keys
    comment_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.oxd-input.oxd-input--focus[placeholder='Write your comment...']")))
    comment_input.click()
    comment_input.send_keys("Okay, hbu?")
    comment_input.send_keys(Keys.ENTER)
    time.sleep(2)

    # Like the comment
    like_comment = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(@class, 'oxd-text') and contains(@class, 'oxd-text--p') and contains(@class, 'orangehrm-post-comment-action') and text()='Like']")))
    like_comment.click()
    time.sleep(2)

    # Find and click the Edit button
    edit_comment = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(@class, 'oxd-text') and contains(@class, 'oxd-text--p') and contains(@class, 'orangehrm-post-comment-action') and text()='Edit']")))
    time.sleep(2)
    driver.execute_script("arguments[0].scrollIntoView(true);", edit_comment)
    time.sleep(2)
    driver.execute_script("arguments[0].click();", edit_comment)
    time.sleep(2)

    # Wait for the input field to appear
    edit_comment_input = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.oxd-input.oxd-input--focus")))
    edit_comment_input.clear()
    edit_comment_input.send_keys("(How about you?)")
    edit_comment_input.send_keys(Keys.ENTER)
    time.sleep(3)   

    #delete comment button
    delete_comment = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//p[contains(@class, 'oxd-text') and contains(@class, 'oxd-text--p') and contains(@class, 'orangehrm-post-comment-action') and text()='Delete']")))
    delete_comment.click()
    time.sleep(2)

    #delete comment comfirmation button
    delete_comment_yes = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.oxd-button.oxd-button--medium.oxd-button--label-danger.orangehrm-button-margin")))
    delete_comment_yes.click()
    time.sleep(2)

    # Scroll to the top of the page
    driver.execute_script("window.scrollTo(0, 0);")

    # Wait for the three-dots button to be clickable and click it using JavaScript
    three_dots_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "i.oxd-icon.bi-three-dots")))
    time.sleep(2)

    # Perform the click action using JavaScript
    driver.execute_script("arguments[0].click();", three_dots_button)
    time.sleep(3)

    edit_post_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//p[text()='Edit Post']")))

    # Perform the click action using JavaScript
    driver.execute_script("arguments[0].click();", edit_post_button)
    time.sleep(2)

####
    
    teextaarea = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "oxd-buzz-post-input")))
    teextaarea.send_keys(" I think this is funny:")
    time.sleep(2)
####

    #clicking share button
    share_button = driver.find_element(By.CSS_SELECTOR, 'div.oxd-overlay.oxd-overlay--flex.oxd-overlay--flex-centered > div > div > div > form > div.oxd-form-actions.orangehrm-buzz-post-modal-actions > button')
    # Click the button
    share_button.click()
    time.sleep(2)

    # Wait for the three-dots button to be clickable and click it using JavaScript
    three_dots_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "i.oxd-icon.bi-three-dots")))
    time.sleep(2)

    # Perform the click action using JavaScript
    driver.execute_script("arguments[0].click();", three_dots_button)
    time.sleep(2)

    delete_post_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//i[contains(@class, 'bi-trash')]")))
    time.sleep(2)

    # Perform the click action using JavaScript
    driver.execute_script("arguments[0].click();", delete_post_button)
    time.sleep(2)

    #delete post comfirmation button
    delete_post_yes = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.oxd-button.oxd-button--medium.oxd-button--label-danger.orangehrm-button-margin")))
    delete_post_yes.click()
    time.sleep(2)

    #time to observe
    time.sleep(5)

    print("Message added and deleted successfully!")
    
def test_reports():

    # Clicking the PIM link
    pim_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//span[text()="PIM"]')))
    pim_link.click()
    time.sleep(2)

    # Clicking the 'Reports' button
    reports_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Reports"]')))
    reports_button.click()
    time.sleep(2)

    # Clicking the 'Add' button
    add_report_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button")))
    add_report_button.click()
    time.sleep(2)

    # Filling the report name
    report_name = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div/div/div[2]/input")))
    report_name.click()
    report_name.send_keys("Test Report")
    time.sleep(2)

    #selecting and adding criteria
    list_criteria_1 = driver.find_element(By.XPATH, "//div[@class='oxd-select-text-input' and text()='-- Select --']")
    list_criteria_1.click()
    time.sleep(2)

    select_criteria_1 = driver.find_element(By.XPATH, "//span[text()='Employment Status']")
    select_criteria_1.click()
    time.sleep(2)

    add_criteria_button = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div[2]/div[2]/button")
    add_criteria_button.click()
    time.sleep(2)

    list_criteria_2 = driver.find_element(By.XPATH, "//div[@class='oxd-select-text-input' and text()='-- Select --']")
    list_criteria_2.click()
    time.sleep(2)

    select_criteria_2 = driver.find_element(By.XPATH, "//span[text()='Service Period']")
    select_criteria_2.click()
    time.sleep(2)

    add_criteria_button.click()
    time.sleep(2)

    #deleting criteria
    delete_criteria_1 = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[3]/button")
    delete_criteria_1.click()
    time.sleep(2)

    delete_criteria_2 = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[3]/button")
    delete_criteria_2.click()
    time.sleep(2)

    #selecting option Current and Past Employees
    selection_include = driver.find_element(By.XPATH, "//div[@class='oxd-select-text-input' and text()='Current Employees Only']")
    selection_include.click()
    time.sleep(2)

    select_include = driver.find_element(By.XPATH, "//span[text()='Current and Past Employees']")
    select_include.click()
    time.sleep(2)

    #selecting fiels or groups
    list_display_field_group = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/div/div/div[1]")
    list_display_field_group.click()
    time.sleep(2)

    select_display_field_group_1 = driver.find_element(By.XPATH, "//span[text()='Personal']")
    select_display_field_group_1.click()
    time.sleep(2)

    add_display_fields_button = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div[2]/div[2]/button")
    add_display_fields_button.click()
    time.sleep(2)

    list_display_field_group.click()
    time.sleep(2)

    select_display_field_group_2 = driver.find_element(By.XPATH, "//span[text()='Contact Details']")
    select_display_field_group_2.click()
    time.sleep(2)

    add_display_fields_button.click()
    time.sleep(2)

    list_display_field_group.click()
    time.sleep(2)

    select_display_field_group_3 = driver.find_element(By.XPATH, "//span[text()='Skills']")
    select_display_field_group_3.click()
    time.sleep(2)

    add_display_fields_button.click()
    time.sleep(2)

    list_display_field_group.click()
    time.sleep(2)

    select_display_field_group_4 = driver.find_element(By.XPATH, "//span[text()='Supervisors']")
    select_display_field_group_4.click()
    time.sleep(2)

    list_display_field = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[2]/div[1]/div[2]/div/div/div[1]")
    list_display_field.click()
    time.sleep(2)

    select_display_field = driver.find_element(By.XPATH, "//span[text()='First Name']")
    select_display_field.click()
    time.sleep(2)

    add_display_fields_button.click()
    time.sleep(2)

    #including headears
    include_header = driver.find_elements(By.CSS_SELECTOR, "span.oxd-switch-input.oxd-switch-input--active.--label-right")
    time.sleep(2)

    action = ActionChains(driver)
    action.key_down(Keys.CONTROL)

    for element in include_header:
            element.click()
    time.sleep(2)

    # Removing elements
    remove_address_loc = driver.find_element(By.XPATH, "//span[text()='Address ']")
    remove_button = remove_address_loc.find_element(By.CSS_SELECTOR, "i.oxd-icon.bi-x.--clear")
    remove_button.click()
    time.sleep(2)

    remove_home_tel_loc = driver.find_element(By.XPATH, "//span[text()='Home Telephone ']")
    remove_button = remove_home_tel_loc.find_element(By.CSS_SELECTOR, "i.oxd-icon.bi-x.--clear")
    remove_button.click()

    remove_work_tel_loc = driver.find_element(By.XPATH, "//span[text()='Work Telephone ']")
    remove_button = remove_work_tel_loc.find_element(By.CSS_SELECTOR, "i.oxd-icon.bi-x.--clear")
    remove_button.click()
    time.sleep(2)

    remove_employee_loc = driver.find_element(By.XPATH, "//span[text()='Employee Id ']")
    remove_button = remove_employee_loc.find_element(By.CSS_SELECTOR, "i.oxd-icon.bi-x.--clear")
    remove_button.click()
    time.sleep(2)

    remove_personal_group = driver.find_element(By.XPATH, "//*[@id=\"app\"]/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[3]/button")
    remove_personal_group.click()
    time.sleep(2)

    # Saving
    save_button = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[4]/button[2]")
    save_button.click()
    time.sleep(5)

    #time for observing
    time.sleep(100)

    print("Reports test was successfull!")

if __name__ == "__main__":
    # Initialize WebDriver, launch the browser, and perform test scenarios
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com")
    driver.maximize_window()

    # Initialize LoginPage object with the WebDriver instance
    login_page = LoginPage(driver)
    login_page.fill_login_form("Admin", "admin123")

    # Execute the test cases
    
    test_add_new_employee()
    test_edit_new_employee()
    test_add_new_candidate()
    test_add_new_message()
    test_reports()

    # Close the browser session
    driver.quit()