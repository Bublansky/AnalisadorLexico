__author__ = 'Ludus'
from cx_Freeze import setup, Executable

setup(
    name="FileReader EXECUTABLE",
    version = "1.0.0",
    description = ".py to .exe",
    executables = [Executable("FileReader.py")])