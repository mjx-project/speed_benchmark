N=100
M=10

echo "====================================="
echo "mjai"
echo "====================================="
for x in $(seq 1 $M); do
    time ./run_mjai.sh $N 2>> mjai_results.txt
done

echo "====================================="
echo "mjx"
echo "====================================="
for x in $(seq 1 $M); do
    time python3.9 run_mjx.py $N 2>> mjx_results.txt
done
