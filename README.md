# Mjx Speed benchmark

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
