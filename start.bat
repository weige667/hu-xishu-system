@echo off
chcp 65001 > nul
echo Starting...
streamlit run ui\app.py --server.port 8501 --server.address 0.0.0.0
pause
