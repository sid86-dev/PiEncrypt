SECONDS=0
# declare initial seconds
clear
cd ..
echo "piencrypt: -----> Starting Pie Test..";
echo -en '\n';
pip install --upgrade piencrypt;
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
read -p "Enter the push reason: " push_type
git commit -m "$push_type";
echo -en '\n';
echo "piencrypt: -----> Commit completed";
echo -en '\n';
git push origin master;
echo -en '\n';
echo "..";
echo '----------------------------------------------------------------------';
echo "piencrypt: -----> Push Successfull";
echo -en '\n';
# get elapsed time
duration=$SECONDS
echo "$(($duration / 60)) minutes and $(($duration % 60)) seconds elapsed."
