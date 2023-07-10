# colo

A simple script that prints out the 256 terminal colors in different formats.</br>
It can print the numbers, the hex value, rgb,hsi and the ansi escape sequence.</br>

```txt
colo --help
usage: colo [-h] [--ansi] [--hsi] [--rgb] [--number] [--name] [--hex]

optional arguments:
  -h, --help  show this help message and exit
  --ansi      bool
  --hsi       bool
  --rgb       bool
  --number    bool
  --name      bool
  --hex       bool
```

![Image](./img/ansi.png)

## How to get
```sh
pipx install colo
```
Also since this is a very small package without any dependencies you could always use `pipx run` without "installing the package":
```sh
pipx run colo
```
