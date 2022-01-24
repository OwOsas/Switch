import cx_Freeze


executables = [cx_Freeze.Executable("Switch.py", base = "Win32GUI")]

cx_Freeze.setup(
    name = "Switch",
    options = {"build_exe": {"packages":["pygame", "random"]}},
    executables = executables
)
