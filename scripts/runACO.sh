#!/bin/sh

RUNS=15
printf "Run, Ant ID, Partial Solution (S), Profit(Z), Capacity(V)" >> results/aco_results.csv
for ((i = 1; i <=$RUNS; i++)) do
    run=$(python aco_rep.py $i)
    printf "$run" >> results/aco_results.csv
done