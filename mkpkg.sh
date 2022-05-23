rm -rf dist/*
python3 setup.py sdist bdist_wheel
python3 -m twine check dist/*

# upload a test version
python3 -m twine upload --repository testpypi dist/*
# test in new environment
python3 -m virtualenv test
source test/bin/activate
# install from the test repository
python3 -m pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple --upgrade mindaffectBCI
python3 -m mindaffectBCI.online_bci
deactivate
rm -rf test

<<<<<<< HEAD
=======

>>>>>>> a548ede18b5df0b53d3ccd030994f9147272f202
python3  -m twine upload dist/*
