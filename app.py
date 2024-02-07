import streamlit as st

st.set_page_config(page_title="Delorean Main Page")

st.header('Delorean Links')

link00 = "https://drive.google.com/drive/folders/1Lek27C3Nw2QASHphTO0Lef-M60vZkQXc"
text00 = "Link"
st.markdown(f'<div style="font-size: 20px;">Shared Google Drive <a target="_blank" href="{link00}">{text00}</a></div>', unsafe_allow_html=True)

link0 = "https://dl-screener.streamlit.app"
text0 = "Link"
st.markdown(f'<div style="font-size: 20px;">DL Screener Streamlit <a target="_blank" href="{link0}">{text0}</a></div>', unsafe_allow_html=True)

link1 = "https://momentum-monitor.streamlit.app/Momentum_Monitor"
text1 = "Link"
st.markdown(f'<div style="font-size: 20px;">Global Momentum Streamlit <a target="_blank" href="{link1}">{text1}</a></div>', unsafe_allow_html=True)

link2 = "https://etf-model.streamlit.app"
text2 = "Link"
st.markdown(f'<div style="font-size: 20px;">ETF Model Streamlit <a target="_blank" href="{link2}">{text2}</a></div>', unsafe_allow_html=True)

link3 = "https://drive.google.com/file/d/1nkVG3_tkDJt6WVeOhXllTkKHpygYjSf9/view?hl=en_GB"
text3 = "Link"
st.markdown(f'<div style="font-size: 20px;">ETF Charts <a target="_blank" href="{link3}">{text3}</a></div>', unsafe_allow_html=True)

link4 = "https://us-stock-model.streamlit.app"
text4 = "Link"
st.markdown(f'<div style="font-size: 20px;">US Stock Model Streamlit <a target="_blank" href="{link4}">{text4}</a></div>', unsafe_allow_html=True)

link5 = "https://drive.google.com/file/d/17ik5Xj2OBbIkau5sJtOsu9mlUFq4bFFD/view"
text5 = "Link"
st.markdown(f'<div style="font-size: 20px;">US Stock Charts <a target="_blank" href="{link5}">{text5}</a></div>', unsafe_allow_html=True)

link6 = "https://india-stock-model.streamlit.app"
text6 = "Link"
st.markdown(f'<div style="font-size: 20px;">India Model Streamlit <a target="_blank" href="{link6}">{text6}</a></div>', unsafe_allow_html=True)

link7 = "https://drive.google.com/file/d/1V60lDnSXZrDjUV9yE-si-8nRRADsWwkc/view"
text7 = "Link"
st.markdown(f'<div style="font-size: 20px;">India Charts <a target="_blank" href="{link7}">{text7}</a></div>', unsafe_allow_html=True)
