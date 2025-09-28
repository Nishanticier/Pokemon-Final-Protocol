#!/bin/bash
cd "$(dirname "$0")/GameFiles"
python3 scripts/main.py
read -p "Press Enter to exit" -r
