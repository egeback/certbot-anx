from setuptools import setup


try:
    long_desc = open("README.md").read()
except:
    print("Skipping README.py_modules for long description as it was not found")
    long_desc = None

setup(
    name="certbot_anx",
    version="0.0.1",
    description="ANX DNS authentication plugin for Certbot",
    long_description=long_desc,
    license="BSD",
    author="Marky Egebäck",
    author_email="marky@egeback.se",
    url="https://github.com/egeback/pycertbot-anx",
    py_modules=["certbot_anx"],
    install_requires=[
        "certbot>=0.37.0",
        #"pyanxdns>=1.0",
        "zope.interface>=4.4.0"
    ],
    entry_points={
        "certbot.plugins": [
            "auth = certbot_anx:ANXAuthenticator",
        ],
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Plugins",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Topic :: Internet :: Name Service (DNS)",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
    ],
)