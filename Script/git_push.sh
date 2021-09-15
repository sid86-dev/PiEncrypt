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
echo "piencrypt: -----> Tracking files..";
echo -en '\n';
git add .;
echo -en '\n';
git commit -m "piencrypt shell scripts";
echo -en '\n';
echo "piencrypt: -----> Commit completed";
echo -en '\n';
git push origin master;
echo -en '\n';
echo '---------------------------------------------'
echo "piencrypt: -----> Push Successfull";
echo -en '\n';
