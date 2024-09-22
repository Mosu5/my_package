from setuptools import find_packages, setup
import glob
import os

package_name = 'my_package'

# Find all .launch.py files in the launch directory
launch_files = glob.glob(os.path.join('launch', '*.launch.py'))

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include the launch files in the data_files section
        (os.path.join('share', package_name, 'launch'), launch_files),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='moustapha',
    maintainer_email='m.azaimi@student.avans.nl',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'python_executable_name = pkg_name.python_executable_name:main'
        ],
    },
)