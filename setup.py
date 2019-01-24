import setuptools

with open("readme.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tf.objd",
    author="PaSe",
    description="My Tensorflow object detection pkg (striped down to core)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/PascalS86/my-tensorflow-object_detection-pkg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: tested on Windows 10",
        "Type :: AI :: Object Detection :: Tensorflow"
    ],
)