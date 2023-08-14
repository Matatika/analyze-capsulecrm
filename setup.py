from setuptools import setup, find_packages

setup(
    name="analyze-capsulecrm",
    version="1.0.0",
    description="Meltano project file bundle of Matatika datasets for Capsule",
    packages=find_packages(),
    package_data={
        "bundle": [
            "analyze/datasets/tap-capsulecrm/*.yml",
            "orchestrate/tap-capsulecrm/elt.sh"
        ]
    },
)
