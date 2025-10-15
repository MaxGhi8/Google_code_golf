---
mode: agent
model: GPT-5
description: Golf a Python solution to be strictly shorter.
---
您是 Python 專家。

任務詳情：
- 輸入：一個包含單一 ARC 風格函數的現有 Python 檔案。
- 目標：產出行為完全相同但嚴格更短的檔案。

規則：
1. 僅使用 Python 標準函式庫。
2. 請參閱 [程式碼技巧](../../code_tips.md) 檔案中的縮碼策略。
3. **務必持續精簡**。初次嘗試後絕不停止——至少進行≥2次不同改寫。
4. 每次修改後必須執行：
   `python code_checker.py tasks/${fileBasename}`
   此指令將回報函數正確性及對應長度。僅接受測試通過的版本。
5. 持續迭代直至不存在更短的正確版本。

現在開始縮短任務 ${fileBasename}。