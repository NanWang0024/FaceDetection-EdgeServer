# Face Detection (FD) Edge Server
This is the Edge server of FD, which converts received video frames into grayscale and then send them to the Cloud server for further anlaysis.

## Tested Platform
We have tested the FD Edge server in [LXC](https://help.ubuntu.com/lts/serverguide/lxc.html) on [ODroid XU3](https://www.hardkernel.com/main/products/prdt_info.php?g_code=g140448267127) with [Alpine Linux](https://alpinelinux.org/) v3.4.

## Requirement
- [Python](https://www.python.org/), [py-pip](https://pkgs.alpinelinux.org/package/v3.4/main/armhf/py-pip), [py-pillow](https://pkgs.alpinelinux.org/package/v3.4/main/armhf/)

## How to use
FD Edge Server is deployed by the FD Cloud Manager when requesting Edge services.
