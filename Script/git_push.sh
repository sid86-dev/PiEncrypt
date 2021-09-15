clear
cd ..
echo "piencrypt: -----> Starting Pie Test..";
cd Test
python pie_test.py; 
echo "piencrypt: -----> Test completed"
cd ..
echo "piencrypt: -----> Tracking files..";
git add .;
git commit -m "piencrypt shell scripts";
echo "piencrypt: -----> Commit completed";
git push origin master;
echo "piencrypt: -----> Push Successfull";
