import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="multilingual_rouge_scoring",
    author="Google LLC",
    author_email="no-reply@google.com",
    description="Pure python implementation of ROUGE-1.5.5.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License"
    ],
    packages=["rouge_score"],
    package_dir = {"rouge_score":""},
    install_requires=[
        "absl-py",
        "nltk",
        "numpy",
        "six>=1.14.0",
    ],
    python_requires='>=3.6',
)
