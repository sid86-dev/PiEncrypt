#build package and push it to pypi
clear
echo "Starting package build...";
python setup.py sdist bdist_wheel;
twine upload dist/*;
echo "Upload Successfull";
# cat build.sh