from setuptools import setup
import os
from glob import glob
package_name = 'rover'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),

        (os.path.join('share', package_name), glob('lunch/*.py')),
        (os.path.join('share', package_name), glob('urdf/*')),
        (os.path.join('share', package_name), glob('meshes/*')),
        (os.path.join('share', package_name), glob('.world/*')),


    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='thirapol',
    maintainer_email='tauthiraphon5678@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'spawn_demo = rover.spawn_demo:main'
        ],

    },
)
