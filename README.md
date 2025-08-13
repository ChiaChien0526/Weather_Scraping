# NYC Weather Web Scraper 🌤️

這個專案使用 Selenium 和 BeautifulSoup 爬取 Wunderground 網站上紐約市從 2014 年至 2024 年的每月平均氣溫，並儲存為 CSV 檔。

## 🧰 使用工具

- Python
- Selenium
- BeautifulSoup (`bs4`)
- pandas
- ChromeDriver（使用 `webdriver_manager` 自動管理）

## 🚀 功能說明

- 開啟 Wunderground 的紐約市天氣歷史頁面
- 自動點擊進入歷史查詢並切換年份與月份
- 擷取各月平均氣溫資料
- 儲存為 `nyc_weather.csv`

## 📦 安裝需求

請先安裝以下套件：

```bash
pip install selenium pandas beautifulsoup4 lxml webdriver_manager
