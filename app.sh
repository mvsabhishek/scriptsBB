#!/bin/bash

echo
echo

echo !!! Welcome to the Blender-Bender !!! 
echo Blender-Bender produces an STL file for a volumetric iso-surface with the help of Blender 2.79b.
echo Blender-Bender can generate STL files for Schwarz-D, Schwarz-P and Gyroid.
echo Just plug in the values and find your STL file sitting ready at /home/blender/output 
# run data_in.sh script to accept input
cd scripts/
./data_in.sh
cd ..


while true; do

	echo "Please enter:"
	echo "1 for Schwarz-D"
	echo "2 for Schwarz-P"
	echo "3 for Gyroid"
	echo "Enter Here:"
	read val
	
	if [ $val -eq 1 ]; then
	echo "Schwarz - D it is!!"
	echo "Please wait......."
	cd scripts/
	blender -b --python main-schwarzD.py
	cd ..
	break
        else
        echo "Re-enter correct input"
	fi 

	if [ $val -eq 2 ]; then
	echo "Schwarz - P it is!!"
	echo "Please wait......."
	cd scripts/
	blender -b --python main-schwarzP.py
	cd ..
	break
        else
        echo "Re-enter correct input"
	fi
 
	if [ $val -eq 3 ]; then
	echo "Schwarz - D it is!!"
	echo "Please wait......."
	cd scripts/
	blender -b --python main-gyroid.py
	cd ..
	break
        else
        echo "Re-enter correct input"

	fi

done
 

echo Your output is at /home/blender/output. 

