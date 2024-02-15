import subprocess

subprocess.run('pyside6-rcc icons.qrc -o icons_rc.py')
with open('icons_rc.py') as file:
    s = file.read()
    s = s.replace('PySide6', 'PyQt6')

with open('icons_rc.py', mode='w') as file:
    file.write(s)
