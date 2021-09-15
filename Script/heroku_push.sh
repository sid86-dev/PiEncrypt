clear
cd ..
echo "piencrypt: -----> Starting Pie Test..";
cd Test
python pie_test.py; 
echo "piencrypt: -----> Test completed"
cd ..
cd web
echo "piencrypt: -----> Tracking files..";
git add .;
git commit -m "piencrypt webapp";
echo "piencrypt: -----> Commit completed";
git push heroku master;
echo "piencrypt: -----> Deployment Successfull";
cd ..
