# RL_projects-PPO-CarRacing
This repository provides one of the simplest solutions for the CarRacing-v3 environment from Gymnasium, using the Proximal Policy Optimisation (PPO) algorithm, implemented with the Stable-Baselines3 library. The CarRacing-v3 task is a continuous control problem in which the agent must drive a car to maximise rewards by staying on track and avoiding collisions. [Game Environment here.](https://gymnasium.farama.org/environments/box2d/car_racing/)

For 

## Features
- Environment: Utilises the CarRacing-v3 environment, which provides visual (pixel-based) observations and requires efficient policy learning for continuous control.
- Reinforcement Learning: Implements PPO, a state-of-the-art on-policy algorithm known for its stability and sample efficiency.
- Customisation: Codebase allows easy adaptation for hyperparameter tuning and integration with other continuous control environments.
- Evaluation: Includes evaluation scripts to test the trained agent over multiple episodes with real-time visualisation (render_mode='human').

### Action Space
If continuous there are 3 actions :

- 0: steering, -1 is full left, +1 is full right

- 1: gas

- 2: braking

### State Space
A top-down 96x96 RGB image of the car and race track.

### Rewards
The reward is -0.1 every frame and +1000/N for every track tile visited, where N is the total number of tiles visited in the track. For example, if you have finished in 732 frames, your reward is 1000 - 0.1*732 = 926.8 points.

# Getting Started

## Prerequisites
- Python 3.8+
- gymnasium
  ```bash
  pip install gymnasium
- stable_baselines3
  ``` bash
  pip install stable_baselines3

## Training the agent
In order to train the PPO agent from scratch, download the train+evaluate.py file and run the following command:
```bash
python3 train+evaluate.py
```
## Evaluating and Visualising the trained agent
In order to evaluate the trained agent, down the evaluate.py file and run the following command:
```bash
python3 evaluate.py
```





## Results
The PPO-trained agent successfully navigates the CarRacing-v3 track, achieving a high cumulative reward while staying on track. Evaluation metrics and training curves are included for detailed performance analysis.
I trained my model on a 1 million timesteps
[You can watch my model's performance here.](https://youtu.be/3GlNIYZ7EUc)

