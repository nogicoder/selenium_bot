wd = wd.Chrome("C:/Users/Chris/Workspace/bot/chromedriver")
wd.implicitly_wait(10)

wd.get("https://www.fahasa.com/ve-voi-van-vo-tap-1.html")

add_to_cart_button = wd.find_element_by_xpath('//*[@id="product_addtocart_form"]/div/div[1]/div[1]/div[2]/button[2]')

time.sleep(3)
add_to_cart_button.click()

check_box_select_all_items = wd.find_element_by_xpath('//*[@id="checkbox-all-products"]')

random_wait_time = random.randrange(1,2)
print("random_wait_time")
time.sleep(random_wait_time)
check_box_select_all_items.click()
time.sleep(3)

coupon_button = wd.find_element_by_xpath('//*[@id="block-totals-mobile"]/div/div/div[1]/div[1]/div[2]/span[1]')
coupon_button.click()
time.sleep(3)

apply_coupon_button = wd.find_element_by_xpath('//*[@id="popup-loading-event-cart-content-tabs"]/div/div[1]/div[2]/div[2]/div[2]/div[2]/button')
apply_coupon_button.click()

coupon_panel_title = wd.find_element_by_xpath('//*[@id="popup-loading-event-cart"]/div[1]/div[1]/div/div[1]/span[2]').text
if coupon_panel_title:
    close_button = wd.find_element_by_xpath('//*[@id="popup-loading-event-cart"]/div[1]/div[1]/div/div[2]/div/img')
    close_button.click()
    time.sleep(3)

time.sleep(3)
payment_button = wd.find_element_by_xpath('//*[@id="content"]/div[4]/div/div[2]/div/div/button')
payment_button.click()

name_field = wd.find_element_by_xpath('//*[@id="fhs_shipping_fullname"]')
name_field.send_keys('Nguyen Van Hung')

email_field = wd.find_element_by_xpath('//*[@id="fhs_shipping_email"]')
email_field.send_keys('atelias@gmail.com')

phone_field = wd.find_element_by_xpath('//*[@id="fhs_shipping_telephone"]')
phone_field.send_keys('09019283647')

from selenium.webdriver.support.select import Select
province_field = wd.find_element_by_xpath('//*[@id="select2-fhs_shipping_city_select-container"]')
province_field.click()
hanoi_province_field = wd.find_element_by_xpath('//*[@id="select2-fhs_shipping_city_select-result-cvxl-487"]')
hanoi_province_field.click()

from selenium.webdriver.support.select import Select
district_field = wd.find_element_by_xpath('//*[@id="select2-fhs_shipping_district_select-container"]')
district_field.click()
caugiay_district_field = wd.find_element_by_xpath('//*[@id="select2-fhs_shipping_district_select-result-4n23-52"]')
caugiay_district_field.click()

from selenium.webdriver.support.select import Select
ward_field = wd.find_element_by_xpath('//*[@id="select2-fhs_shipping_wards_select-container"]')
ward_field.click()
trunghoa_ward_field = wd.find_element_by_xpath('//*[@id="select2-fhs_shipping_wards_select-result-ofi2-689"]')
trunghoa_ward_field.click()

address_field = wd.find_element_by_xpath('//*[@id="fhs_shipping_street"]')
address_field.send_keys('39 Pham Ngu Lao')
time.sleep(3)

confirm_payment_button = wd.find_element_by_xpath('//*[@id="wrapper"]/div[2]/div[1]/div/div[2]/div/div/div[13]/div[2]/div[3]/div/div/div[2]/div[2]/div/button')
confirm_payment_button.click()
