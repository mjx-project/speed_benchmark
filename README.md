# Mjx Speed benchmark

- AWS `m6i.large` at `us-east-1`
- vCPU: 2
- mem: 8GiB
- Intel(R) Xeon(R) Platinum 8375C CPU @ 2.90GHz

![speed_benchmark](/results/speed_benchmark.png)

## How to use

On Ubuntu20.04

```sh
$ ./install.sh
$ ./run.sh
```

On Docker (ubuntu20.04)

```sh
$ ./build.sh
$ docker run -it --rm -v $(pwd):/tmp  mjx-mjai-benchmark /bin/bash -c "cd /tmp && ./run.sh"
```
