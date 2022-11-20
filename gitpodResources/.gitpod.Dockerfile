FROM gitpod/workspace-full

USER gitpod

RUN pip install pandas numpy matplotlib beautifulsoup4 pyautogui
