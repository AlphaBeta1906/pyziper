from setuptools import setup, find_packages

setup(
    name="pyzip",
    version="0.2",
    description=(
        "pyzip a simple cli tools to help you to handle archive file ,like zipping and"
        " unzipping "
    ),
    keywords='tools ,cli,zip,7z,tar,archive',
    install_requires=["Click", "py7zr"],
    py_modules=["main"],
    entry_points="""
        [console_scripts]
        pyzip= main:pyzip
    """,
)
