import subprocess
import pytest

# define a helper function to check if a package is installed
def is_package_installed(package_name):
    try:
        subprocess.check_output(["dpkg", "-s", package_name], stderr=subprocess.STDOUT, text=True)
        return True
    except subprocess.CalledProcessError:
        return False

# test if the required packages have been installed
def test_required_packages_installed():
    required_packages = [
        "ca-certificates",
        "software-properties-common",
        "rsync",
        "unzip",
        "apt-utils",
        "gpg-agent",
        "wget",
        "curl",
        "xsel",
        "python3",
        "xdg-utils",
        "zsh",
        "peco",
        "apt-transport-https",
    ]

    for package in required_packages:
        assert is_package_installed(package), f"{package} is not installed"
