#!/bin/bash

###############################################################################
#PART 2
###############################################################################
echo "$1 started" >> ballgs2status.out
sed -i "3s/.*/ bishop = 1/" eik.in
#Obtain equilibrium values of s_hat, beta_prime at each rho_c
for rho in $(seq 0.1 0.1 0.9); 
do
    sed -i "13s/.*/ rhoc = $rho/" eik.in
    echo "rho = $rho" >> $1et.out
    ./eiktest >> $1et.out
    echo "2A ./eiktest rho = $rho" >> ballgs2status.out
done
sed -i "13s/.*/ rhoc = 0.75/" eik.in
echo "rho = 0.75" >> $1et.out
./eiktest >> $1et.out
echo "2A ./eiktest rho = 0.75" >> ballgs2status.out
#generates .csv file with rho_c, s_hat, beta_prime at equilibrium
python eiktocsv.py $1et.out $1eqparams.csv
echo "2A $1eiktocsv.py executed, check $1eqparams.csv" >> ballgs2status.out
#test for ideal ballooning stability at equilibrium
echo "2A ideal ballooning stability at equilibrium testing started" >> ballgs2status.out 
while IFS=, read -r rho s_hat beta_prime
do
    sed -i "13s/.*/ rhoc = $rho/" eik.in
    sed -i "8s/.*/ s_hat_input = $s_hat/" eik.in
    ./ball >> ball$1.out
    echo "2A ./ball rho = $rho" >> ballgs2status.out
done < $1eqparams.csv
#add stability at equilibrium to .csv file
python balleq.py ball$1.out $1eqparams.csv
echo "2A balleq.py executed (adds stability at equilibrium to .csv file)" >> ballgs2status.out

###############################################################################
#PART 3
###############################################################################
sed -i "3s/.*/ bishop = 4/" eik.in
#Find beta' vs s_hat ballooning stability boundary at each rho 
{
    read
    while IFS=, read -r label rho s_hat3 beta_prime stable
    do
	sed -i "13s/.*/ rhoc = $rho/" eik.in
	for s_hat in $(seq -3.0 .1 5.0); do
	    sed -i "8s/.*/ s_hat_input = $s_hat/" eik.in
	    echo "s_hat = $s_hat" >> $1P3$rho.out
	    ./ball >> $1P3$rho.out
	done
	#make plot and save avg s_hat for gs2
	python plotballfile.py $1P3$rho.out $1avg.csv $rho $s_hat3 $beta_prime $1ballr
	echo "3 rho = $rho" >> ballgs2status.out
    done
} < $1eqparams.csv

###############################################################################
#PART 4A
###############################################################################

#Verify GS2 recovers ideal ballooning stability boundary at 3 radii
arr=( 0.5 0.75 0.9 )
#set bishop = 1 to get equilibrium values of gradient and beta at each rho
sed -i "3s/.*/ bishop = 1/" eik.in
for rho in "${arr[@]}"
do 
    sed -i "13s/.*/ rhoc = $rho/" eik.in
    ./eiktest >> ballgs2.out
    python eikout.py eik.out $1gradbeta.csv
done

#make csv of all parameters needed for gs2 loops over rho = 0.5, 0.75, 0.9
python part4a.py $1gradbeta.csv $1eqparams.csv $1avg.csv

#make plot of gamma vs beta_prim to recover stability boundary
{
read
while IFS=, read -r label grad beta rho s_hat beta_prime
do
cp r95eqlongestky.in $1part4Ar$rho.in
sed -i "103s/.*/ tprim = $grad/" $1part4Ar$rho.in
sed -i "118s/.*/ tprim = $grad/" $1part4Ar$rho.in
sed -i "14s/.*/ beta = $beta/" $1part4Ar$rho.in
sed -i "11s/.*/ rhoc = $rho/" $1part4Ar$rho.in
sed -i "30s/.*/ s_hat_input = $s_hat/" $1part4Ar$rho.in
sed -i "31s/.*/ beta_prime_input = $beta_prime/" $1part4Ar$rho.in
    for i in $(seq 0.1 .05 5.0); do
	newbprim=`echo "$i*$beta" | bc -l`
	newtprim=`echo "$i*$grad" | bc -l`
	#echo $newbprim
	#echo $newtprim
	cp $1part4Ar$rho.in $1part4Ar$rho-$i.in
	sed -i "31s/.*/ beta_prime_input = $newbprim/" $1part4Ar$rho-$i.in
	sed -i "103s/.*/ tprim= $newtprim/" $1part4Ar$rho-$i.in
	sed -i "118s/.*/ tprim= $newtprim/" $1part4Ar$rho-$i.in
        #./ingen $1part4Ar$rho-$i.in
	echo "$1part4Ar$rho-$i.out" >> $1part4Ar$rho-list.txt
	mpirun -np 4 ./gs2_new $1part4Ar$rho-$i
    done
python plotgammavsbprim.py $1part4Ar$rho-list.txt 0.1 5.0 0.05
done
} < $1gradbeta.csv

###############################################################################
#Part 4B
###############################################################################

#plot gamma vs ky for different radii and pressure contributions

#make csv file for inputs
python part4b.py $1part4b.csv
{
read
while IFS=, read -r label rho s_hat b_prim beta tprim fprim
do
    cp r95eqlongestky.in $1part4Br$rho-tp$tprim.in
    sed -i "75s/.*/ naky = 16/" $1part4Br$rho-tp$tprim.in
    sed -i "76s/.*/ aky_min = 0.1/" $1part4Br$rho-tp$tprim.in
    sed -i "77s/.*/ aky_max = 1.6/" $1part4Br$rho-tp$tprim.in
    sed -i "103s/.*/ tprim= $tprim/" $1part4Br$rho-tp$tprim.in
    sed -i "118s/.*/ tprim= $tprim/" $1part4Br$rho-tp$tprim.in
    sed -i "14s/.*/ beta = $beta/" $1part4Br$rho-tp$tprim.in
    sed -i "11s/.*/ rhoc = $rho/" $1part4Br$rho-tp$tprim.in
    sed -i "30s/.*/ s_hat_input = $s_hat/" $1part4Br$rho-tp$tprim.in
    sed -i "31s/.*/ beta_prime_input = $beta_prime/" $1part4Br$rho-tp$tprim.in
    sed -i "104s/.*/ fprim= $fprim/" $1part4Br$rho-tp$tprim.in
    sed -i "119s/.*/ fprim= $fprim/" $1part4Br$rho-tp$tprim.in
    mpirun -np 4 ./gs2_new $1part4Br$rho-tp$tprim
    python PlotOut.py $1part4Br$rho-tp$tprim ky gamma
done
} < $1part4b.csv