#build package and push it to pypi
clear
cd ..
echo "piencrypt: -----> Starting Pie Test..";
cd Test
python pie_test.py;
echo "piencrypt: -----> Test completed"
cd ..
echo "piencrypt: -----> Starting package build...";
python setup.py sdist bdist_wheel;
twine upload dist/*;
echo "piencrypt: -----> Upload Successfull";
# cat build.sh