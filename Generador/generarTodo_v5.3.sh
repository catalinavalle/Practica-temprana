#!/bin/bash

#paramsList=("10 10 8 0.8" "20 20 16 0.7" "30 30 25 0.9" "50 50 40 0.85")
paramsList=("50 25" "60 30")
nList="10 12 14 16 18 20"
perList="0.6 0.65 0.7 0.75 0.8 0.85 0.9 0.95"

#50 20 10 0.9 137

#Rehaciendo las mas grandes.
seedList="129 137"

for params in "${paramsList[@]}"; do
    for n in ${nList}; do
        for per in ${perList}; do

            params2="${params} ${n} ${per}"

            echo "${params}"
            bloques=$(echo "${params}" |awk '{print $1}')
            echo "bloques: ${bloques}"
            
            refugios=$(echo "${params}" |awk '{print $2}')
            echo "refugios: ${refugios}"

            echo "n: ${n}"   
            
            echo "per: ${per}"       
            
            for seed in ${seedList}; do
                echo "python3 generador_v5.3.py ${params2} ${seed}"
                python3 generador_v5.3.py ${params2} ${seed}
            done
        done
    done
done


