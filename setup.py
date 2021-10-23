from setuptools import setup

setup(
    name="ojw",
    version="0.0.2",
    install_requires=["online-judge-tools"],
    entry_points={"console_scripts": ["ojw = ojw.main:main", "ojp = ojw.main:passer"]},
)
