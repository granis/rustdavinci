import subprocess

subprocess.run("pyuic6 mainui.ui -o mainui.py")

with open("mainui.py", mode="a") as file:
    s = "\nimport rustdavinci.ui.resources.icons_rc  # noqa: F401, E402\n"
    file.write(s)
