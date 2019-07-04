from cx_Freeze import setup, Executable
import os.path


PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')
# On appelle la fonction setup


setup(
    name = "IHM",
    version = "1",
    description = "Votre programme",
    executables = [Executable("IHM.py")],
)