from setuptools import setup, find_packages

setup(
    name="smartbin",
    version="1.0.0",
    author="Thandeka",
    description="SmartBin Campus Sustainability Rewards System",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "fastapi>=0.104.0",
        "uvicorn>=0.24.0",
        "pytest>=7.4.0",
        "httpx>=0.25.0",
    ],
)
