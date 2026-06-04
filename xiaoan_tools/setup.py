from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="xiaoan-tools",
    version="0.1.0",
    author="xiaoan",
    description="小安工具箱 - 小红书封面生成、办公效率工具集",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/slm527/xiaoan-tools",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=["Pillow>=9.0"],
    entry_points={
        "console_scripts": [
            "xiaohongshu-cover=xiaoan_tools.cover:main",
        ],
    },
)
