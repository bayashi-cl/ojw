from setuptools import setup

setup(
    name="ojw",
    version="0.0.1",
    install_requires=["online-judge-tools"],
    entry_points={"console_scripts": ["ojw = ojw.main:main"]},
)
