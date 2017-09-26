from setuptools import find_packages, setup

tests_requirements = [
    'pytest',
    'pytest-cov',
    'pytest-flake8',
    'pytest-isort',
]

setup(
    name="www-pellov",
    version="0.1.dev0",
    description="Website for PromoMaker",
    url="https://www.promomaker.fr",
    author="Kozea",
    packages=find_packages(),
    include_package_data=True,
    scripts=['pellov.py'],
    install_requires=[
        'Flask',
        'mandrill',
    ],
    tests_require=tests_requirements,
    extras_require={'test': tests_requirements}
)
