#!/usr/bin/env python3
import os
import subprocess
import sys


def main():
    # Install dependencies
    subprocess.run([sys.executable, "-m", "pip", "install",
                   "-r", "requirements.txt"], check=True)

    # Collect static files
    subprocess.run([sys.executable, "manage.py",
                   "collectstatic", "--noinput"], check=True)

    print("Build completed successfully!")


if __name__ == "__main__":
    main()
