from pakman import PackageInstaller

# List of packages you want to install
requiredPackages = ['requests']

# Initialize the installer with a list of packages
installer = PackageInstaller(requiredPackages)

# Run the installer for the list of packages in verbose mode (shows output)
print("Running installer for multiple packages in verbose mode...")
installer.runInstaller(verbose=True)

# Run the installer for the list of packages in silent mode (hides output)
print("\nRunning installer for multiple packages in silent mode...")
installer.runInstaller(verbose=False)

# Install a single package using the install method
print("\nInstalling a single package in verbose mode...")
installer.install('numpy', verbose=True)

# Once installed, you can import the packages as usual
import requests
import numpy

# You can also use the isInstalled method to check if a package is installed. It returns a boolean value.
print(PackageInstaller.isInstalled('requests'))
print(PackageInstaller.isInstalled('numpy'))

print("\nAll required packages have been installed and are ready to use!")