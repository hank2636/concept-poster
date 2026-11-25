---
name: concept-poster
description: 把文字、流程、影片重點或參考圖做成概念海報、資訊圖或雙面名片。海報支援 16:9 橫式、1:1 方形與 A4 直式，交付可編輯 HTML 和 PNG。
---

# Concept Poster

## 讀素材

先確認觀眾、用途和要傳達的主張。收到影片連結時，先讀完整影片或字幕，再整理內容。讀不到時請使用者提供影片檔或逐字稿。使用參考圖時，沿用使用者指定的構圖方向，另做主視覺並換掉第三方的姓名、聯絡資訊和 QR Code。

## 選版型並排版

- 16:9 橫式預設用 [橫式海報](templates/ppt-16x9.html)。
- 1:1 方形用 [方形海報](templates/ig-square-1x1.html)。
- A4 直式用 [A4 海報](templates/a4-portrait.html)。
- 做雙面名片時讀 [名片指南](references/business-card.md)。暖米款可從 [雙面名片模板](templates/business-card-warm.html) 開始。

把模板複製成新 HTML，再替換示例內容。依素材選重點條列、步驟流程、概念圖或左右對照。遇到圖形能直接表達主張時，依 [編輯式海報排版](references/editorial-design.md) 調整欄寬、字級、留白和閱讀順序。用原尺寸與手機縮圖各檢查一次。

## 匯出與交付

保留 HTML，使用 [PNG 匯出工具](scripts/export_png.py) 或同等的 Chromium 截圖方式匯出。海報預設長邊 3840 px，保持版面比例。名片依參考比例或指定尺寸匯出。檢查字型、裁切和圖示，正式名片另用手機掃描 QR Code。

平台支援附件時直接附上 PNG。只轉送文字的橋接可交付實際下載驗證過的圖片連結。若 Claude 環境提供 Artifact 工具，也可發布 HTML 預覽。後續修改同一份 HTML，再匯出新版。
