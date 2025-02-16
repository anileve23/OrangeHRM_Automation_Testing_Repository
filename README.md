---

# 🖥️ HR Management System Test Automation

This script automates employee and candidate management tasks in an HR management system using **Selenium WebDriver**. The test script interacts with the login page of the system: [OrangeHRM Demo](https://opensource-demo.orangehrmlive.com/web/index.php/auth/login).

## 🔧 How to Run the Test

1. **Clone or Download** the repository:
   ```bash
   git clone https://github.com/anileve23/OrangeHRM_Automation_Testing_Repository.git
   ```

2. **Install Dependencies**:
   Install the necessary Python libraries (like Selenium) by running:
   ```bash
   pip install -r requirements.txt
   ```

3. **Edit File Path**:  
   Open `test_login.py` and navigate to **line 65**. Replace the current file path with your own local path to the image here:
   ![image](https://github.com/user-attachments/assets/1520984c-2ffe-41a9-ac72-9e2bcf49a1c1)

4. **Run the Test**:
   After editing the file path, you can run the test:
   ```bash
   python test_login.py
   ```

   The script will log in to the demo HR system and perform the necessary tasks, including uploading the image specified in the file path.

## ⚙️ Features

- Automated login to **OrangeHRM Demo**.
- Upload employee image (edit the file path before running).
- Easy-to-follow test automation using **Selenium WebDriver**.

## 📸 Screenshot
![image](https://github.com/user-attachments/assets/db2cec68-19f5-4659-be22-fb99e72815fc)

## 📋 Requirements

- **Python 3.x**
- **Selenium WebDriver**
- Web browser (Chrome/Firefox with the appropriate WebDriver installed)
