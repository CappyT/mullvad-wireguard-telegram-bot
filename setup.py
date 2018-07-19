import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mullvadbot",
    version="0.0.1",
    author="CappyT",
    author_email="cappyt@eden.network",
    description="A bot to control your mullvad account and multiplex it on a server.",
    ##long_description=long_description,
    long_description="LELLINO",
    ##long_description_content_type="text/markdown",
    url="https://github.com/CappyT/mullvadbot",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License 3",
        "Operating System :: OS Independent",
    ),
)