# 匯入套件
import time
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

# 啟動瀏覽器工具的選項
my_options = webdriver.ChromeOptions()
# my_options.add_argument("--headless")       #不開啟實體瀏覽器背景執行
my_options.add_argument("--start-maximized")  # 最大化視窗
my_options.add_argument("--incognito")  # 開啟無痕模式
my_options.add_argument("--disable-popup-blocking")  # 禁用彈出攔截
my_options.add_argument("--disable-notifications")  # 取消通知

# 使用 Chrome 的 WebDriver
driver = webdriver.Chrome(options=my_options)

# 開啟 Stackoverflowjobs 網站
driver.get("https://www.wunderground.com/weather/us/ny/new-york-city")

# 等待頁面載入
time.sleep(2)

wait = WebDriverWait(driver, 3)

# 取得檢視原始碼的內容 (page_source 取得的 html，是動態的、使用者操作過後的結果)
html = driver.page_source

# 指定 lxml 作為解析器
soup = bs(html, "lxml")

# 等待標籤欄位的 <a> 標籤出現
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "ul.subnav.subnav-left a"))
)

# 所有 <a> 標籤，尋找"HISTORY"欄的，並點擊
links = driver.find_elements(By.CSS_SELECTOR, "ul.subnav.subnav-left a")
for link in links:
    if "HISTORY" in link.text.strip().upper():
        link.click()
        break

# 等待頁面載入
time.sleep(2)

# 用 CSS selector 選取monthly欄並點擊
month = driver.find_elements(By.CSS_SELECTOR, "a.link")
month[2].click()

# 等待頁面載入
time.sleep(2)

# 儲存資料用的清單
weather_data = []

# 開始爬取 2014/01 ~ 2024/12
for year in range(2014, 2025):
    for month in range(1, 13):
        try:
            # 選擇年份
            year_select = Select(
                driver.find_element(By.CSS_SELECTOR, "select#yearSelection")
            )
            year_select.select_by_visible_text(str(year))

            # 選擇月份
            month_select = Select(
                driver.find_element(By.CSS_SELECTOR, "select#monthSelection")
            )
            month_select.select_by_value(str(month))

            # 點擊 "View"
            view_button = driver.find_element(By.CSS_SELECTOR, "input#dateSubmit")
            view_button.click()
            time.sleep(3)

            # 解析 HTML
            # soup = bs(driver.page_source, "lxml")

            # 找到summary區塊元素
            summary = driver.find_element(By.CSS_SELECTOR, "div.summary-title")
            # 滾動至該區塊
            driver.execute_script(
                "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
                summary,
            )
            # 稍微暫停，模擬人類操作
            time.sleep(2)

            # 取得平均氣溫
            avg_temp = driver.find_elements(
                By.CSS_SELECTOR,
                "div.summary-table tbody td[_ngcontent-app-root-c145428343]",
            )

            # 擷取平均氣溫（調整 td 位置以對應實際資料）
            # avg_temp_tag = soup.select_one("div.summary-table tbody td:nth-of-type(5)")
            # avg_temp = avg_temp_tag.text.strip() if avg_temp_tag else "N/A"

            # 儲存一筆資料
            weather_data.append(
                {"Year": year, "Month": month, "AvgTemperature": avg_temp[4].text}
            )

            print(f"✅ 已擷取：{year}-{month:02d} Avg Temp: {avg_temp[4].text}")
            time.sleep(1)

        except Exception as e:
            print(f"❌ 失敗於 {year}-{month:02d}：{e}")
            weather_data.append(
                {"Year": year, "Month": month, "AvgTemperature": "Error"}
            )
            continue

# 關閉瀏覽器
driver.quit()

# 儲存為 CSV 檔
df = pd.DataFrame(weather_data)
df.to_csv("nyc_weather.csv", index=False, encoding="utf-8-sig")

print("📁 所有資料已儲存為 nyc_weather.csv")