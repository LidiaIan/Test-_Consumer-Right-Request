import time


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

"Initializam o variabila in driver care interactioneaza cu browserul"
opt_out = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
opt_out.get('https://optoutccpa-devenv.bigdbm.com/')
opt_out.maximize_window()

submit = opt_out.find_element(by=By.CLASS_NAME, value="btn-primary")
opt_out.execute_script("arguments[0].scrollIntoView();", submit)
time.sleep(2)
# submit.click()

agreement_box = opt_out.find_element(by=By.ID, value="inlineFormCheck")
time.sleep(2)
agreement_box.click()

submit.click()

delete_box = opt_out.find_element(by=By.ID, value="formCheckDelete")
opt_out.execute_script("arguments[0].scrollIntoView();", delete_box)
time.sleep(2)
delete_box.click()
opt_out.find_element(by=By.ID, value="formCheckCategories").click()
opt_out.find_element(by=By.ID, value="formCheckSpecial").click()

submit = opt_out.find_element(by=By.CLASS_NAME, value="btn-primary")
opt_out.execute_script("arguments[0].scrollIntoView();", submit)
time.sleep(2)
# submit.click()


first_name = opt_out.find_element(value="horizontal-firstname-input")
first_name.send_keys("lidia")

last_name = opt_out.find_element(value="horizontal-lastname-input")
last_name.send_keys("TEST")

address1 = opt_out.find_element(value="horizontal-address1-input")
address1.send_keys("2239 Pine Ridge Rd")

address2 = opt_out.find_element(value="horizontal-address2-input")
address2.send_keys("flat 69")

city = opt_out.find_element(value="horizontal-city-input")
city.send_keys("Orlando")

# state = opt_out.find_element(value="")
# state.send_keys("abfgfg")

zip_code = opt_out.find_element(value="horizontal-zip-input")
zip_code.send_keys("12345")

email = opt_out.find_element(value="horizontal-email-input")
email.send_keys("lidia@bigdbm.com")

opt_out.find_element(value="horizontal-phone-input").send_keys("8055830260")

agent_email = opt_out.find_elements(by=By.CLASS_NAME, value="form-control")[8]
agent_email.send_keys("lidia.ianus@dapter.com")

agent_verif = opt_out.find_elements(by=By.CLASS_NAME, value="form-control")[9]
agent_verif.send_keys("secret")

time.sleep(4)

submit = opt_out.find_element(by=By.CLASS_NAME, value="btn-primary")
# submit.click()

# #ERROR: ModuleNotFoundError: No module named 'element'
# home_elements = opt_out.find_element(by=By.CLASS_NAME, value="nav-link text-dark")
# # for elements in home_elements:
# #     print(f"{element.text}: {element.tag_name}")
#
# home_elements[0].click

# attachment = opt_out.find_element(value="additionalFiles")
# attachment.click()

time.sleep(2)

# Metoda de identificare linku-ri din pagine

# links = opt_out.find_elements(by=By.TAG_NAME, value="a")
# for link in links:
#    print(f"{link.tag_name}: {link.text}")



# privacy = opt_out.find_element(by=By.LINK_TEXT, value="Privacy")
# privacy.click()
# time.sleep(5)
#
# optofsale = opt_out.find_element(by=By.LINK_TEXT, value="Opt Out of Sale")
# optofsale.click()
# time.sleep(5)

# privacy_policy = opt_out.find_element(by=By.LINK_TEXT, value="Privacy Policy")
# opt_out.execute_script("arguments[0].scrollIntoView();", privacy_policy)
# time.sleep(1)
# privacy_policy.click()
# time.sleep(5)


print("Test complete")
