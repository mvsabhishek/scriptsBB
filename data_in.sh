#! /bin/bash

file=/home/blender/scripts/data.json
echo 
echo
echo "Attention: The values you enter here for dimensions are multiplied by Pi"
echo "Please enter 10 if you are not sure."
echo "Caution: If you enter a value greater than 30, the application will take more time to export STL."
echo
echo "Enter value for x-dimension:"
read x
echo
echo "Enter value for y-dimension:"
read y
echo
echo "Enter value for z-dimension:"
read z
echo
echo "Enter value for thickness: (must be between 0.000 and 1.000)"
echo "Please enter 0.6 if you are not sure."
read t
echo
echo "Please enter 1.0 if you are not sure."
echo "Enter value for offset (thickness): (must be between -1.000 and 1.000)"
read off

echo '{ "x":"'$x'","y":"'$y'","z":"'$z'","thickness":"'$t'","offset":"'$off'", "collada":"../output/Object.dae", "objectName":"Object", "stlFile":"../output/Output" }' > /home/blender/scripts/data.json


