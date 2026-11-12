\# 學生作業資料



學號：C113152352



姓名：吳柏勳



GitHub 網址：

https://github.com/c113152352-cmd/TEXT1



作業名稱：TEXT1｜高雄市停車場查詢系統



作業說明：

功能

依處所名稱或地址搜尋停車場。

依行政區域及最低小型車輛篩選資料。

顯示符合資格的處所號碼、車位總數與行政區號碼。

以長條圖比較各行政區的小型車位總數。

查看清單清單，並下載目前篩選結果為 CSV。

資料來源

資料集名稱： 停車場資訊

提供機關：高雄市政府交通局

用途：提供高雄市轄內各行政區停車場資訊。

官方資料集頁面：高雄市府資料開放平台－停車場資訊

官方頁標註下載格式：CSV、JSON。

系統使用欄位：行政區、臨時停車處、可提供小型停車位、地址（原始檔另含Seq）。

本專案附帶parking\_lots.csv，是用戶提供的下載檔案複製而來；此文件有121筆資料。資料會隨資料來源更新，請以官方平台及附帶文件的實際內容為準。

啟動方式

請先安裝 Python 3.9 或更新版本。於本資料夾開啟終端機後執行：



python -m pip install -r requirements.txt

python -m streamlit run app.py

Streamlit啟動後會在瀏覽器開啟本機頁面。停止程序可在終端機按Ctrl+C。



專案檔案

app.py：程式入口，啟動Streamlit畫面。

text1/data\_loader.py：讀取CSV、檢查欄位並整理車頭。

text1/parking\_service.py：處理、關鍵字行政區、最低車輛篩選及行政區統計。

text1/ui.py：顯示查詢條件、指標、圖表、清單與下載功能。

text1/\_\_init\_\_.py：讓Python將text1識別為模組套件。

parking\_lots.csv：資料集 CSV 原始資料副本（UTF-8 與 BOM）。

requirements.txt：需要Python套件。

README.md：專題說明及操作方式。

資料處理和查詢邏輯已從畫面拆開，方便之後分別修改或功能增加；目前仍維持精簡的Python套件結構，沒有額外的資料庫或服務。

