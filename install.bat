
@echo off
echo 🚀 بدء تثبيت منصة الرصد الذكي...

REM إنشاء بيئة افتراضية
python -m venv venv

REM تفعيل البيئة
call venv\Scripts\activate

REM تحديث pip وتثبيت المتطلبات
python -m pip install --upgrade pip
pip install -r requirements.txt

REM تشغيل المنصة
echo ✅ تم التثبيت بنجاح.
streamlit run main.py

pause
