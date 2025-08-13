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
```

## ▶️ 執行方式
```bash
python weather_scraper.py
```
執行後會產出 nyc_weather.csv，內含 2014~2024 年紐約市每月平均氣溫。

## 📁 輸出格式

| Year | Month | AvgTemperature |
|------|-------|----------------|
| 2014 | 1     | 32°F           |
| ...  | ...   | ...            |

---

## 🌐 資料來源

所有天氣資料皆爬取自：

> [Wunderground - New York City Historical Weather](https://www.wunderground.com/weather/us/ny/new-york-city)

此網站提供詳細的歷史天氣數據，包括每日與每月的溫度、降雨量、濕度等資訊。

---

## 📝 注意事項

- 請確認你的電腦已安裝 Google Chrome 瀏覽器
- 程式會模擬點擊與載入，執行時間可能數分鐘
- 若網頁結構改變，CSS selector 需更新
