import subprocess

subprocess.run('pyuic6 settingsui.ui -o settingsui.py')

with open('settingsui.py', mode='a') as file:
    s = '\nimport rustdavinci.ui.resources.icons_rc  # noqa: F401, E402\n'
    file.write(s)
