from setuptools import setup, find_packages

setup(
    name="analyze-capsulecrm",
    version="0.1.0",
    description="Meltano project file bundle of Matatika datasets for Capsule",
    packages=find_packages(),
    package_data={
        "bundle": [
            "analyze/datasets/tap-capsulecrm/*.yaml",
            "orchestrate/tap-capsulecrm/elt.sh"
        ]
    },
)
