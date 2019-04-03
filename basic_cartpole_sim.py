#!/usr/bin/env python3

import gym

def main():
    env = gym.make("CartPole-v0")
    n_episodes = 20
    n_timeSteps = 100
    for e in range(n_episodes):
        observation = env.reset()
        for t in range(n_timeSteps):
            env.render()
            print(observation)
            action = env.action_space.sample()
            observation, reward, done, info = env.step(action)
            if done:
                print("Episode finished after {} timesteps".format(t+1))
                break


main()
