# draughts
Draughts game written in Python. 

It will play a game of draughts with each player controlled by an agent.

If you want to create your own agent to play draughts, create a sub-class of `Agent` and implement the `choose_move` method.

<img width="400" height="400" alt="Screenshot from 2025-12-06 13 05 50" src="https://github.com/user-attachments/assets/a5851cc1-e3cb-4426-9c61-a0ddbd547bda" />


## To run

Activate the virtual environment (here we assume it is in the `.venv` directory):
```
source .venv/bin/activate
```
Install draughts:
```
pip install .
```
Run draughts:
```
make run
```
Run tests (for developers):
```
make test
```
