clear
cd ..
echo "Starting Pie Test..";
cd Test
python pie_test.py;
echo "Test completed"
cd ..
echo "Tracking files..";
git add .;
git commit -m "piencrypt shell scripts";
echo "Commit completed";
git push origin master;
echo "Push Successfull";
