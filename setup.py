from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "IHM",
    version = "1",
    description = "Votre programme",
    executables = [Executable("IHM.py")],
)