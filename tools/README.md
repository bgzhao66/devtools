# Dev within a docker env
```sh
cd path/to/src
devcc
```

# Trace calls with GDB

1. Go to a directory of source code
```sh
cd path/to/src
trace | tee gdb.cmds
```
2. Go to the directory of build, start the program with GDB
```sh
cd path/to/build
gdb bin/demo -x ../path/to/src/gdb.cmds -x ../another/../gdb.cmds
```
3. the call traces are logged to `gdb.txt` too.
