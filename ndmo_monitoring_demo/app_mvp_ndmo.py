
import streamlit as st
import pandas as pd
from PIL import Image
from pathlib import Path

# إعداد الصفحة
st.set_page_config(page_title="منصة الرصد الذكي - نموذج تجريبي", layout="centered")
st.markdown("<h2 style='text-align: center;'>📊 تقرير جهة تجريبية - منصة الرصد الذكي</h2>", unsafe_allow_html=True)

# تحميل البيانات
base_path = Path("منصة_الرصد_الذكي_المصغرة") / "example_entity" / "scan_2025-07-01"
df = pd.read_excel(base_path / "results.xlsx")
image_path = base_path / "screenshot.png"
ppt_path = base_path / "تقرير_الجهة.pptx"
txt_path = base_path / "policy.txt"

# عرض صورة الصفحة
st.subheader("🖼️ صورة صفحة سياسة الخصوصية")
if image_path.exists():
    st.image(str(image_path), use_column_width=True)
else:
    st.warning("⚠️ لم يتم العثور على صورة الصفحة.")

# عرض جدول التحليل
st.subheader("✅ نتائج تحليل البنود")
st.dataframe(df, use_container_width=True)

# عرض النسبة النهائية والحالة
passed = df["النتيجة"].tolist().count("✅")
status = "ممتثل" if passed == 8 else "امتثال جزئي" if passed >= 4 else "غير ممتثل"
percentage = round(passed / 8 * 100, 1)

st.metric("نسبة التغطية", f"{percentage}%")
st.markdown(f"**الحالة:** `{status}`")

# عرض نص السياسة
st.subheader("📄 نص السياسة (مقتطف)")
with open(txt_path, "r", encoding="utf-8") as f:
    policy_preview = f.read()[:500]
st.code(policy_preview, language="markdown")

# رابط تحميل التقرير
st.subheader("📥 تحميل التقرير الكامل")
with open(ppt_path, "rb") as f:
    st.download_button(
        label="📎 تحميل تقرير PowerPoint",
        data=f,
        file_name="تقرير_الجهة.pptx",
        mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
    )
