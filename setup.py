from setuptools import setup, find_packages

setup(
    name="taufeeq-cli-resume",
    version="1.0.0",
    description="Print Taufeeq's resume in the terminal.",
    author="Taufeeq Riyaz",
    author_email="contact.taufeeq@gmail.com",
    packages=find_packages(),
    install_requires=["rich"],
    entry_points={
        "console_scripts": [
            "taufeeq-resume=taufeeq_cli_resume.resume:display_resume",
        ],
    },
)
