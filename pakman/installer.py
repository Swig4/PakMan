import subprocess
import sys
import importlib.util

class PackageInstaller:
    def __init__(self, packages: list):
        """
        param packages: List of package names to install.
        """
        self.packages = packages

    @staticmethod
    def isInstalled(package: str) -> bool:
        """
        Checks if a package is installed.
        """
        return importlib.util.find_spec(package) is not None
    
    def install(self, package: str, verbose: bool = False):
        """
        Installs/Upgrades the package if it's not installed.
        """
        if not self.isInstalled(package):
            args = [sys.executable, "-m", "pip", "install", "--upgrade", package]
            if verbose:
                print(f"Installing/Upgrading {package}...")
                subprocess.run(args, check=True)
            else:
                subprocess.run(args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def runInstaller(self, verbose: bool = False):
        """
        Iterates through the list of packages and installs them if they're not installed.
        """
        for package in self.packages:
            if not self.isInstalled(package):
                self.install(package, verbose)
