import cx_Freeze
from cx_Freeze import *
setup(
    name = "bloxy",
    options = {'build_exe':{'packages': ['pygame']}},
    executables = [
        Executable(
            "main.pyw"
        )
    ]
)
