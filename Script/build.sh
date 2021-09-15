#build package and push it to pypi
clear
cd ..
echo "Starting Pie Test..";
cd Test
python pie_test.py;
echo "Test completed"
cd ..
echo "Starting package build...";
python setup.py sdist bdist_wheel;
twine upload dist/*;
echo "Upload Successfull";
# cat build.sh