@echo off
chcp 65001 > nul
echo Installing...
python --version
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
echo Done. Run start.bat
pause
