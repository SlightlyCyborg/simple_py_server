# simple_py_server

## Dependencies

- python 2,7
- pyserial


## Installation
```
sudo pip install pyserial
```

## Usage

Open 2 terminals

Terminal 1
```
mkfifo comm_pipe
python server.py
```

Terminal 2
```
printf ”80,60\n” > comm_fifo
```

This will move the motor to z position 80 and y position 60
