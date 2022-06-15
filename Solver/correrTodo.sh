#!/bin/bash

instanceList=$(ls *.dat)
runFile="prueba.run"
summary="resumen.out"

for instance in $instanceList; do
       echo "instance: ${instance}"  
       rm -rf ${runFile}
       echo "reset ;" >> ${runFile}
       echo "model modelo_kocatepe.mod;" >> ${runFile}
       line="data ${instance} ;" 
       echo "${line}" >> ${runFile}
       cat prueba_base.run >> ${runFile}
       echo "./ampl ${runFile} > ${instance}.res"
       ./ampl ${runFile} > ${instance}.res
       resultsLine=$(tail -1 ${instance}.res) 
       echo "${instance} ${resultsLine}" >> ${summary}
done



