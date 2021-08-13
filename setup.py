from setuptools import setup, find_packages

long_description = open('README.md').read()

setup(
    name="pyziper",
    version="0.3",
    long_description=long_description,
    long_description_content_type='text/markdown',
    description=(
        "pyziper a simple cli tools to help you to handle archive file ,like zipping"
        " and unzipping "
    ),
    url='https://github.com/AlphaBeta1906/pyziper',
    download_url=(
        'https://github.com/AlphaBeta1906/pyziper/archive/refs/tags/v0.3.tar.gz'
    ),
    author="fariz",
    author_email="farizi1906@gmail.com",
    keywords='tools ,cli,zip,7z,tar,archive',
    install_requires=["Click", "py7zr", "colorama"],
    py_modules=["main"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Environment :: Console',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],
    entry_points="""
        [console_scripts]
        pyziper= main:pyziper
    """,
)
