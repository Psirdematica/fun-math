#! /bin/bash


#this bash script will help determine the nature of the quadratic roots
#using the descriminant 
# b^2 -4ac


descriminant(){
    a=$1
    b=$2
    c=$3

    des=$(echo "$b^2 - (4*$a*$c)" | bc -l)
    if [ $des -gt 0 ]
    then
        echo "Real and distinct roots"
    elif [ $des -lt 0 ]
    then
        echo "Complex roots"
    else
        echo "Real repeated roots"
    fi    
}

descriminant 3 2 1 
descriminant 1 -7 10 
descriminant 3 2 -1 
