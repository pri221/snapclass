import streamlit as st

def subject_card(name, code, section, stats=None, footer_callback=None):
    html = f"""<div style="background:white; border-left: 8px solid #EB459E; padding:25px; border-radius: 20px; border: 1px solid #e2e8f0; margin-bottom:20px; box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);">
<h3 style="margin:0 0 10px 0; color: #1e293b; font-size: 1.5rem; font-weight: 600;">{name}</h3>
<p style="color:#64748b; margin:0 0 15px 0; font-size: 0.95rem;">Code : <span style="background:#E0E3FF; color:#5865F2; padding:3px 8px; border-radius:6px; font-weight: 500;">{code}</span> &nbsp;|&nbsp; Section : {section}</p>"""

    if stats:
        html += '<div style="display: flex; gap:10px; flex-wrap:wrap;">'
        for icon, label, value in stats:
            html += f'<div style="background: #fdf2f8; color: #701a75; padding:6px 14px; border-radius:12px; font-size:0.9rem; font-weight: 500; display: inline-flex; align-items: center; gap: 6px;">{icon} <b>{value}</b> {label}</div>'
        html += '</div>'

    html += '</div>'
    
    st.markdown(html, unsafe_allow_html=True)

    if footer_callback:
        footer_callback()