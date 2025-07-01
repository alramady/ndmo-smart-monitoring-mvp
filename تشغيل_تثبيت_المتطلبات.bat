@echo off
title تثبيت المتطلبات
echo جاري تثبيت المتطلبات من requirements.txt ...
python -m pip install --upgrade pip
pip install -r requirements.txt

echo.
echo تم التثبيت بنجاح!
pause