from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import random
import time
import logging
from logging.handlers import RotatingFileHandler


def log_settings():
    #  Logger definitions
    log_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(funcName)s - line: %(lineno)d - %(message)s')
    logFile = "app.log"
    my_handler = RotatingFileHandler(logFile, mode="a", maxBytes=2*1024*1024, backupCount=2, encoding=None, delay=False)
    my_handler.setFormatter(log_formatter)
    my_handler.setLevel(logging.DEBUG)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    console_handler.setLevel(logging.INFO)
    app_log = logging.getLogger("course_clicker")
    app_log.setLevel(logging.INFO)
    if len(app_log.handlers) < 2:
        app_log.addHandler(my_handler)
        app_log.addHandler(console_handler)
    return app_log


if __name__ == "__main__":
    # change values below
    timer = 5  # timer in hours
    course = "link_to_course_by_href"
    app_log = log_settings()
    url_auth = "link_to_login_page"
    app_log.info("Course clicker app is started")
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(url_auth)
    x_next = "xpath_to_next_button"
    x_final = 'xpath_to_final_button'
    fin_flag = True
    time1 = timer*3600
    t0 = int(time.time())
    try:  # authorization
        app_log.info("Start authorization.")
        name = driver.find_element_by_name("email")
        name.send_keys("your_login")
        pasw = driver.find_element_by_name("password")
        pasw.send_keys("your_password")
        pasw.submit()
    except Exception as ex:
        app_log.error(f"Authorization fails: {ex}")
        driver.close()
    else:
        app_log.info("Authorization successful")
        app_log.info(driver.current_url)
        time.sleep(1)
        try:  # find and choose a course
            app_log.info("Finding the predefined course...")
            driver.find_element_by_xpath('//a[@href="'+course+'"]').click()
        except Exception as ex1:
            app_log.error(f"Course not found: {ex1}")
            driver.close()
        else:
            app_log.info("Course is found and selected.")
            time.sleep(1)
            while fin_flag:  # loop until end
                app_log.info("Looping through the course...")
                ran = random.randint(180, 210)
                d_time = int(time.time()) - t0
                if d_time >= time1:
                    app_log.info("Timer is runs out!")
                    app_log.info("Please continue this course later. See you soon!")
                    fin_flag = False
                    continue
                try:  # find the complete test button
                    app_log.info(driver.current_url)
                    app_log.info(f"Timeout is: {ran}")
                    app_log.info(f"Searching finish button..")
                    fin = driver.find_element_by_xpath(x_final)
                    time.sleep(ran)
                    fin.click()
                    app_log.info(f"Finish button was found and clicked")
                    app_log.info("Wait until time runs out and finish the course")
                except NoSuchElementException:
                    app_log.info(f"Finish button NOT found..")
                    try:  # find the next button
                        app_log.info(f"Searching Next button..")
                        next1 = driver.find_element_by_xpath(x_next)
                        app_log.info(f"Next button was found")
                        time.sleep(ran)
                        next1.click()
                        app_log.info(f"Next button was clicked after timeout")
                    except Exception as ex3:
                        app_log.error(f"Next button NOT found: {ex3}")
                        driver.close()
                except Exception as ex2:
                    app_log.error(f" Some big troubles with the finish button: {ex2}")
                else:
                    app_log.info("Finish looping.")
                    fin_flag = False
    time.sleep(10)
    app_log.info("Stop the app")
    driver.close()
