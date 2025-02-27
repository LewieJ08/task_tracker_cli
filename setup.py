from setuptools import setup, find_packages

setup(
    name="task_tracker_cli",
    version="1.0.0",
    packages=find_packages(),  # Automatically finds package directories
    install_requires=[],  # No external dependencies needed
    entry_points={  
        "console_scripts": [
            "task-tracker=task_tracker_cli.main:main"  # Links CLI command to main()
        ]
    },
    author="Lewie Jackson",
    author_email="LewieJ08@gmail.com",
    description="A simple task tracker CLI app used to store and manage tasks.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LewieJ08/task_tracker_cli",  # Add your GitHub repo link once it's created
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)