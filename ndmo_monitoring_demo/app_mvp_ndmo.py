
import streamlit as st
import pandas as pd
from PIL import Image
from pathlib import Path

st.set_page_config(page_title="منصة الرصد الذكي", layout="centered")
st.markdown("<h2 style='text-align: center;'>📊 تقرير جهة تجريبية - منصة الرصد الذكي</h2>", unsafe_allow_html=True)

base_path = Path("ndmo_monitoring_demo") / "example_entity" / "scan_2025-07-01"
df = pd.read_excel(base_path / "results.xlsx")
image_path = base_path / "screenshot.png"
ppt_path = base_path / "تقرير_الجهة.pptx"
txt_path = base_path / "policy.txt"

st.subheader("🖼️ صورة صفحة سياسة الخصوصية")
try:
    image = Image.open(image_path)
    st.image(image, use_container_width=True)
except Exception:
    st.warning("⚠️ تعذر عرض الصورة.")

st.subheader("✅ نتائج تحليل البنود")
st.dataframe(df, use_container_width=True)

passed = df["النتيجة"].tolist().count("✅")
status = "ممتثل" if passed == 8 else "امتثال جزئي" if passed >= 4 else "غير ممتثل"
percentage = round(passed / 8 * 100, 1)

st.metric("نسبة التغطية", f"{percentage}%")
st.markdown(f"**الحالة:** `{status}`")

st.subheader("📄 نص السياسة (مقتطف)")
with open(txt_path, "r", encoding="utf-8") as f:
    st.code(f.read()[:500], language="markdown")

st.subheader("📥 تحميل التقرير الكامل")
with open(ppt_path, "rb") as f:
    st.download_button(
        label="📎 تحميل تقرير PowerPoint",
        data=f,
        file_name="تقرير_الجهة.pptx",
        mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
    )
