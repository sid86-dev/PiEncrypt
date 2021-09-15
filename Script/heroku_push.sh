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
cd web
echo "piencrypt: -----> Tracking files..";
echo -en '\n';
git add .;
echo -en '\n';
git commit -m "piencrypt webapp";
echo -en '\n';
echo "piencrypt: -----> Commit completed";
echo -en '\n';
git push heroku master;
echo -en '\n';
echo '---------------------------------------------'
echo "piencrypt: -----> Deployment Successfull";
echo -en '\n';
cd ..
