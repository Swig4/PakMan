# tests/example.py
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pakman.installer import PackageInstaller

class TestPackageInstaller(unittest.TestCase):
    def test_installer(self):
        installer = PackageInstaller(["requests"])
        self.assertIsInstance(installer, PackageInstaller)

if __name__ == "__main__":
    unittest.main()
