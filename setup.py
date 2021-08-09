from setuptools import setup, find_packages

setup(
    name="pyzip",
    version="0.1",
    description="a simple cli tools for automation git repository creation",
    keywords='automation,tools ,cli,git,github,development',
    install_requires=["Click", "py7zr"],
    py_modules=["main"],
    entry_points="""
        [console_scripts]
        pyzip= main:pyzip
    """,
)
