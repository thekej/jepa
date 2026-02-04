from setuptools import setup, find_packages

VERSION = "0.0.1"

if __name__ == "__main__":
  setup(
      name="jepa",
      version=VERSION,
      description="JEPA research code.",
      packages=find_packages(),
  )

