# RL_projects-PPO-CarRacing
This repository provides one of the simplest solutions for the CarRacing-v3 environment from Gymnasium, using the Proximal Policy Optimisation (PPO) algorithm, implemented with the Stable-Baselines3 library. The CarRacing-v3 task is a continuous control problem in which the agent must drive a car to maximise rewards by staying on track and avoiding collisions.

## Features
- Environment: Utilises the CarRacing-v3 environment, which provides visual (pixel-based) observations and requires efficient policy learning for continuous control.
- Reinforcement Learning: Implements PPO, a state-of-the-art on-policy algorithm known for its stability and sample efficiency.
- Customisation: Codebase allows easy adaptation for hyperparameter tuning and integration with other continuous control environments.
- Evaluation: Includes evaluation scripts to test the trained agent over multiple episodes with real-time visualisation (render_mode='human').

## Repository Content
- train.py: Script to train the PPO agent on the CarRacing-v3 environment.
- evaluate.py: Script to evaluate the trained policy with visual rendering and performance metrics.
- Pretrained Model: Includes a pretrained PPO model (ppo_carracing.zip) capable of solving the environment with high rewards.
- Environment Wrapper: Adds custom handling for resetting, stepping, and rendering the environment.
- Requirements: Dependencies are managed for seamless execution.

## Results
The PPO-trained agent successfully navigates the CarRacing-v3 track, achieving a high cumulative reward while staying on track. Evaluation metrics and training curves are included for detailed performance analysis.
