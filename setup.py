from setuptools import setup
with open("README.md", "r") as f:
    long_description = f.read()

setup(
  name = 'img_filters',
  packages = ['img_filters'],
  version = '0.0.5', 
  license='MIT', 
  description = 'A package for image manipulation',
  long_description=long_description,
  long_description_content_type="text/markdown",
  author = 'AyushSehrawat',
  author_email = 'scientificnationwords@gmail.com',
  url = 'https://github.com/AyushSehrawat/img_filters',
  download_url = 'https://github.com/AyushSehrawat/img_filters/archive/0.0.5.tar.gz',
  keywords = ["image manipulation",'image-manipulation','opencv','pillow'],
  install_requires=['Pillow','opencv-python','numpy','kiwisolver','matplotlib'],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
  ],
)