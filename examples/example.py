from pakman import PackageInstaller

# List of packages you want to install
requiredPackages = ['requests']

# Initialize the installer
installer = PackageInstaller(requiredPackages)

# Run the installer in verbose mode (shows output)
print("Running installer in verbose mode...")
installer.runInstaller(verbose=True)

# Run the installer in silent mode (hides output)
print("\nRunning installer in silent mode...")
installer.runInstaller(verbose=False)

# Once installed, you can import the packages as usual
import requests

print("\nAll required packages have been installed and are ready to use!")
