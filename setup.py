from setuptools import setup

setup(
    name="ojw",
    version="0.0.2",
    install_requires=[
        "online-judge-tools",
        "expander @ git+https://github.com/bayashi-cl/expander",
        "online-judge-verify-helper @ git+https://github.com/bayashi-cl/verification-helper@modify",
    ],
    entry_points={"console_scripts": ["ojw = ojw.main:main"]},
)
