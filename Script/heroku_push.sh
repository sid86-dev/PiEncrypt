clear
cd ..
echo "Starting Pie Test..";
cd Test
python pie_test.py; 
echo "Test completed"
cd ..
cd web
echo "Tracking files..";
git add .;
git commit -m "piencrypt webapp";
echo "Commit completed";
git push heroku master;
echo "Deployment Successfull";
cd ..
