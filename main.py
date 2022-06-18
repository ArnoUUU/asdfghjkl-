from selenium import webdriver as wd
import chromedriver_binary
wd = wd.Chrome()
wd.implicitly_wait(5)
wd.get("https://usfirst.submittable.com/gallery/48359bf4-58a8-4ef2-9fba-f2bce3af4ff0/23881035")
BUTTON=wd.find_element_by_xpath("//*@id=\"container\"]/div[2]/div/div/div/div[1]/div[1]/div[1]/button")
while True:
  BUTTON.click()
  print("clicked")
