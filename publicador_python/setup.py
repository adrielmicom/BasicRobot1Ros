from setuptools import find_packages, setup

package_name = 'publicador_python'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='adri',
    maintainer_email='adrielmicom@protonmail.com',
    description=' publicador de comandos en python3 ',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'publicador_cmd = publicador_python.publicador_cmd:main',
            'subscriber_odom = publicador_python.subscriber_odom:main',
        ],
    },
)
