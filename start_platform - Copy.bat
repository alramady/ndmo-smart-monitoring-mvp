@echo off
REM إنشاء بيئة افتراضية
python -m venv venv

REM تفعيل البيئة
call venv\Scripts\activate

REM تحديث pip وتثبيت المتطلبات
python -m pip install --upgrade pip
pip install -r requirements.txt