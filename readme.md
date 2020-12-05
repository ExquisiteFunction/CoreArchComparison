### Introduction

This project collects mainstream CPU's core microarchitecture information in CSV form and provides a visualization tool helping comparison between different chips. Though there are only AMD's Zen, Zen2 and Zen3 described, I have prepared a dozen of chips made by Intel, IBM, Arm, RISCV and MIPS, which will be submitted in the future. All the architecture parameters should be labeled references clearly.

CSV is used to store data and I use python to plot. You can use command lines to filter parameters and specific chips in regular expression.

### Help

```shell
python3 CoreArchDataBase.py -h

Here is Core Architecture Infomation Database.
Use regular expression to query and save results.

	-r, --row	row_filter	row_filter in re format.
	-c, --column	column_filter	column_filter in re format.
	-s		filename	save figure with given name.
	-h, --help			print help infomation.
```

### Examples

```shell
python3 CoreArchDataBase.py -r "Front" -s "./image/AMD FrontEnd Comparation.png"
```

![AMD FrontEnd Comparation](https://github.com/ExquisiteFunction/CoreArchComparison/blob/main/image/AMD%20FrontEnd%20Comparation.png)

```shell
python3 CoreArchDataBase.py -r "(.*)INT(.*)" -s "./image/AMD INT Comparation.png"
```

![AMD INT Comparation](https://github.com/ExquisiteFunction/CoreArchComparison/blob/main/image/AMD%20INT%20Comparation.png)

```shell
python3 CoreArchDataBase.py -r "(.*)Cache(.*)" -c "(.*)Zen2" -s "./image/AMD Zen2 Cache Info.png"
```

![AMD Zen2 Cache Info](https://github.com/ExquisiteFunction/CoreArchComparison/blob/main/image/AMD%20Zen2%20Cache%20Info.png)

