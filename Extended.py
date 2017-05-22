# -*- coding: utf-8 -*-
# from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.chrome.webdriver import WebDriver
import time, unittest
from selenium.webdriver.common.keys import Keys


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class Extended(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        # self.wd.implicitly_wait(60)
        self.wd.maximize_window()

    def test_Extended(self):
        wd = self.wd
        wd.get("https://ext-uat/_layouts/supp/")
        time.sleep(3)
        wd.find_element_by_link_text("Вход").click()
        wd.find_element_by_id("ctl00_PlaceHolderMain_signInControl_UserName").click()
        wd.find_element_by_id("ctl00_PlaceHolderMain_signInControl_UserName").clear()
        wd.find_element_by_id("ctl00_PlaceHolderMain_signInControl_UserName").send_keys("werw@gmail.com")
        wd.find_element_by_id("ctl00_PlaceHolderMain_signInControl_Password").click()
        wd.find_element_by_id("ctl00_PlaceHolderMain_signInControl_Password").clear()
        wd.find_element_by_id("ctl00_PlaceHolderMain_signInControl_Password").send_keys("123qazQAZ")
        wd.find_element_by_id("ctl00_PlaceHolderMain_signInControl_Login").click()
        wd.find_element_by_link_text("Объявления о закупках через Реестр").click()
        time.sleep(3)
        wd.get("https://ext-uat/_layouts/supp/")
        time.sleep(2)
        wd.find_element_by_link_text("Кабинет поставщика").click()
        time.sleep(2)
        wd.find_element_by_link_text("Регистрационные данные").click()
        time.sleep(2)
        wd.find_element_by_xpath("//div[@class='docs-drop-zone']//button[.='Добавить документы']").click()
        # Выбрать документы
        wd.find_element_by_css_selector("button.k-button.select-file-button").click()
        time.sleep(2)
        # wd.elem.send_keys("Open").click(ENTER)

        # wd.switch_to_window(self, "Open")


        # set the file name in clipboard
        wd.switch_to_active_element().send_keys(self.ENTER)
        #wd.switch_to.alert("open").sendKeys("D:\123.rar").accept()
        wd.switch_to.window("Open")
        wd.find_element_by_xpath("//input[@id='id_1']").send_keys("D:\\123.rar")
        wd.find_element_by_xpath('//input[@value="Open"]').click()
        wd.switch_to.default_content()
        # StringSelection ss = new StringSelection("D:\\123.rar")
        # Нажали на свободное место чтобы раскрыть список
        wd.find_element_by_css_selector("div.item-header").click()
        # Клик по выпадающему списку
        wd.find_element_by_css_selector("span.k-input").click()
        # Выбор типа документа
        wd.find_element_by_css_selector("li.k-item.k-state-hover").click()
        # Напечатать Наименование
        wd.find_element_by_xpath("//div[@class='file-item']/form/enrc-input-text/span/input").click()
        wd.find_element_by_xpath("//div[@class='file-item']/form/enrc-input-text/span/input").clear()
        wd.find_element_by_xpath("//div[@class='file-item']/form/enrc-input-text/span/input").send_keys("Тестинг")
        # Нажать кнопку Добавить
        wd.find_element_by_css_selector("button.k-button.upload").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
