# -*- coding: utf-8 -*-
# from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.chrome.webdriver import WebDriver
import time, unittest


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class All_Smoke(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        # self.wd.implicitly_wait(60)
        self.wd.maximize_window()

    def test_All_Smoke(self):
        wd = self.wd
        wd.get("https://ext-uat/_layouts/supp/")
        time.sleep(2)
        wd.find_element_by_link_text("Вход").click()
        time.sleep(2)

        self.login(wd, username="bakhtiyar_Zubairov@epam.com", password="123qazQAZ")

        wd.find_element_by_link_text("Объявления о закупках через Реестр").click()
        wd.get("https://ext-uat/_layouts/supp/")
        wd.find_element_by_link_text("Кабинет поставщика").click()
        time.sleep(3)
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[1]/enrc-container/fieldset/enrc-input-text[1]/span/textarea").click()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[1]/enrc-container/fieldset/enrc-input-text[1]/span/textarea").clear()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[1]/enrc-container/fieldset/enrc-input-text[1]/span/textarea").send_keys(
            "ТОО Big Daddy Kane")
        self.country(wd, "Германия")
        """wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[1]/enrc-container/fieldset/enrc-select[2]/span/enrc-dropdown-list/span/span[1]/span[1]").click()
        wd.find_element_by_xpath("//li[@id='115a3951-ac58-415e-a0cf-bea335ec5d72']//div[.='Казахстан']").click()"""
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[1]/enrc-container/fieldset/enrc-input-text[2]/span/input").click()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[1]/enrc-container/fieldset/enrc-input-text[2]/span/input").clear()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[1]/enrc-container/fieldset/enrc-input-text[2]/span/input").send_keys(
            "981041003956")
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[1]/enrc-container/fieldset/enrc-input-text[3]/span/input").click()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[1]/enrc-container/fieldset/enrc-input-text[3]/span/input").clear()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[1]/enrc-container/fieldset/enrc-input-text[3]/span/input").send_keys()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[1]/enrc-container/fieldset/enrc-input-text[4]/span/input").click()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[1]/enrc-container/fieldset/enrc-input-text[4]/span/input").clear()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[1]/enrc-container/fieldset/enrc-input-text[4]/span/input").send_keys()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[1]/enrc-container/fieldset/enrc-input-text[5]/span/input").click()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[1]/enrc-container/fieldset/enrc-input-text[5]/span/input").clear()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[1]/enrc-container/fieldset/enrc-input-text[5]/span/input").send_keys()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[1]/enrc-container/fieldset/enrc-input-text[4]/span/input").click()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[1]/enrc-container/fieldset/enrc-input-text[4]/span/input").clear()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[1]/enrc-container/fieldset/enrc-input-text[4]/span/input").send_keys(
            "123456789123")
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[1]/enrc-container/fieldset/enrc-input-text[5]/span/input").click()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[1]/enrc-container/fieldset/enrc-input-text[5]/span/input").clear()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[1]/enrc-container/fieldset/enrc-input-text[5]/span/input").send_keys(
            "123")
        time.sleep(1)
        wd.find_element_by_xpath("//enrc-container[@class='fluent-table']/enrc-input-text/span/textarea").click()
        wd.find_element_by_xpath("//enrc-container[@class='fluent-table']/enrc-input-text/span/textarea").clear()
        wd.find_element_by_xpath("//enrc-container[@class='fluent-table']/enrc-input-text/span/textarea").send_keys(
            "Иванов Иван")
        time.sleep(1)
        dropdown = wd.find_element_by_xpath("(//enrc-input-position//span[@unselectable='on'])[2]")
        if (str(dropdown.get_attribute('class')).__contains__('k-state-disabled')):
            wd.find_element_by_css_selector("label.k-checkbox-label").click()
        else:
            dropdown.click()
        time.sleep(2)
        dropdown.click()
        time.sleep(1)
        wd.find_element_by_xpath("(//li[contains(text(), 'Директор')])[1]").click()
        time.sleep(2)
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[2]/enrc-container[1]/enrc-input-text[1]/span/textarea").click()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[2]/enrc-container[1]/enrc-input-text[1]/span/textarea").clear()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[2]/enrc-container[1]/enrc-input-text[1]/span/textarea").send_keys(
            "г. Астана")
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[2]/enrc-container[1]/enrc-input-text[2]/span/textarea").click()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[2]/enrc-container[1]/enrc-input-text[2]/span/textarea").clear()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[2]/enrc-container[1]/enrc-input-text[2]/span/textarea").send_keys(
            "г. Лондон")
        wd.find_element_by_xpath("//label[@for='ADDRESS_FACT_MATCH_WITH_POST1']").click()
        if not wd.find_element_by_id("ADDRESS_FACT_MATCH_WITH_POST1").is_selected():
            wd.find_element_by_id("ADDRESS_FACT_MATCH_WITH_POST1").click()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[2]/enrc-container[1]/enrc-input-text[4]/span/input").click()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[2]/enrc-container[1]/enrc-input-text[4]/span/input").clear()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[2]/enrc-container[1]/enrc-input-text[4]/span/input").send_keys(
            "www.erg.com")
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[2]/enrc-container[1]/enrc-input-text[5]/span/input").click()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[2]/enrc-container[1]/enrc-input-text[5]/span/input").clear()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[2]/enrc-container[1]/enrc-input-text[5]/span/input").send_keys(
            "859-456")
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[2]/enrc-container[1]/enrc-input-text[6]/span/input").click()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[2]/enrc-container[1]/enrc-input-text[6]/span/input").clear()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[2]/enrc-container[1]/enrc-input-text[6]/span/input").send_keys(
            "963-458")
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[2]/enrc-container[1]/enrc-input-text[7]/span/input").click()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[2]/enrc-container[1]/enrc-input-text[7]/span/input").clear()
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[2]/enrc-container[1]/enrc-input-text[7]/span/input").send_keys(
            "АО Жайремский ГОК")

        wd.find_element_by_xpath("//div[@class='action-btn-panel']//button[.='Сохранить']").click()
        time.sleep(4)
        wd.find_element_by_css_selector("span.k-icon.k-i-close").click()
        # wd.find_element_by_css_selector("span.k-icon.k-i-close").click()
        time.sleep(2)
        wd.find_element_by_link_text("Выход").click()
        time.sleep(5)

    def login(self, wd, username, password):
        username_element = wd.find_element_by_id("ctl00_PlaceHolderMain_signInControl_UserName")
        password_element = wd.find_element_by_id("ctl00_PlaceHolderMain_signInControl_Password")
        username_element.send_keys(username)
        password_element.send_keys(password)
        wd.find_element_by_id("ctl00_PlaceHolderMain_signInControl_Login").click()

    def country(self, wd, country):
        # Выбор страны регистрации
        wd.find_element_by_xpath(
            "//div[@class='supplier-common-info']/div[1]/enrc-container/fieldset/enrc-select[2]/span/enrc-dropdown-list/span/span[1]/span[1]").click()
        time.sleep(1)
        wd.find_element_by_xpath(
            "//li[@role = 'option']//*[contains(text(), '" + country + "')]").click()
        time.sleep(1)

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
