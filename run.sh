N=1
M=1

echo "mjai"
for x in 1..${M}; do
    time ./run_mjai.sh $N
done

echo "mjx"
for x in 1..${M}; do
    time python3 run_mjx.py $N
done
