#!/bin/bash
set -e
echo "胡希恕经方辨证系统 - 安装"
if ! command -v python3 &> /dev/null; then
    echo "Error: Python3 not found"
    exit 1
fi
echo "Python: $(python3 --version)"
pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
echo "Done. Run ./start.sh"
