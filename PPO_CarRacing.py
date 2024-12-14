import gymnasium as gym
import time

from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env
from stable_baselines3.common.evaluation import evaluate_policy
from stable_baselines3.common.monitor import Monitor


#Create an environment for racecar
env = make_vec_env("CarRacing-v3", n_envs=16)

#Creating and defining the model
model = PPO(
    policy = "CnnPolicy",
    env = env,
    n_steps = 1024, 
    batch_size = 64, 
    n_epochs = 4,
    gamma = 0.999,
    gae_lambda = 0.98,
    ent_coef = 0.01,
    verbose = 1 
)

#Training the model on 1 million timesteps
model.learn(total_timesteps=1_000_000)

#Saving the trained model
model.save("ppo-carracing-1")

#Evaluating the agent
#Creating a new environment for training
eval_env = Monitor(gym.make("CarRacing-v3", render_mode="rgb_array"))
mean_reward, std_reward = evaluate_policy(model, eval_env, deterministic=True)

#Printing the results
print(f"mean_reward={mean_reward:.2f}+/- {std_reward}")


# ------------------- To Visualise the Performance ------------------------

# Create the environment again to allow visualisation (using render_mode="human")
env = gym.make("CarRacing-v3", render_mode='human')


# Evaluate the model for 3 episodes
for i in range(3):
    obs, _ = env.reset()  #Reset environment and get initial observation
    done = False          #Track if the episode has ended
    episode_reward = 0    #Track cumulative reward for the episode

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