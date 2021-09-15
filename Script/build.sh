#build package and push it to pypi
clear
cd ..
echo "piencrypt: -----> Starting Pie Test..";
echo -en '\n';
cd Test
python pie_test.py;
echo -en '\n';
echo "piencrypt: -----> Test completed"
echo -en '\n';
cd ..
echo "piencrypt: -----> Starting package build...";
echo -en '\n';
python setup.py sdist bdist_wheel;
echo -en '\n';
echo "piencrypt: -----> Build successfull"
echo -en '\n';
twine upload dist/*;
echo -en '\n';
echo '---------------------------------------------'
echo "piencrypt: -----> Upload Successfull";
echo -en '\n';
# cat build.sh