from pakman import PackageInstaller

# List of packages you want to install
required_packages = ['requests']

# Initialize the installer
installer = PackageInstaller(required_packages)

# Run the installer to check and install missing packages
installer.runInstaller()

# Once installed, you can import the packages as usual
import requests

print("All required packages have been installed and ready to use!")
