import gymnasium as gym
import time

from stable_baselines3 import PPO
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.monitor import Monitor

# Create the environment
env = gym.make("CarRacing-v3", render_mode='human')

# Load the pre-trained model
model = PPO.load('ppo_carracing')

# Evaluate the model for 10 episodes
for i in range(10):
    obs, _ = env.reset()  # Reset environment and get initial observation
    done = False          # Track if the episode has ended
    episode_reward = 0    # Track cumulative reward for the episode

    print(f"Starting Episode {i + 1}")

    while not done:
        # Get action from the trained policy
        action, _ = model.predict(obs, deterministic=True)

        # Take a step in the environment
        obs, reward, terminated, truncated, info = env.step(action)
        done = terminated or truncated

        # Accumulate reward
        episode_reward += reward

        # Render the environment
        env.render()

        # Add a delay for smoother rendering
        time.sleep(0.01)

    print(f"Episode {i + 1} finished with reward: {episode_reward}")
    time.sleep(1)  # Pause between episodes

env.close()  # Close the environment after evaluation


#Evaluating the agent
#Creating a new environment for training
eval_env = Monitor(gym.make("CarRacing-v3", render_mode="rgb_array"))
mean_reward, std_reward = evaluate_policy(model, eval_env, deterministic=True)

#Printing the results
print(f"mean_reward={mean_reward:.2f}+/- {std_reward}")
