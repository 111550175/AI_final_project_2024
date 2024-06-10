import numpy as np
import argparse

def compute(args):
    rewards = np.array([np.load("./results/baseline/BCQ_baseline_{}-v0_{}.npy".format(args.data, seed)) for seed in range(3)]).transpose()
    rewards_avg = np.mean(rewards, axis = 1)
    print(np.round(np.mean(rewards_avg[99:109]), 3))

    rewards = np.array([np.load("./results/GAN/BCQ_GAN_{}-v0_{}.npy".format(args.data, seed)) for seed in range(3)]).transpose()
    rewards_avg = np.mean(rewards, axis = 1)
    print(np.round(np.mean(rewards_avg[99:109]), 3))

    rewards = np.array([np.load("./results/quadruple/BCQ_quadruple_{}-v0_{}.npy".format(args.data, seed)) for seed in range(3)]).transpose()
    rewards_avg = np.mean(rewards, axis = 1)
    print(np.round(np.mean(rewards_avg[99:109]), 3))

    rewards = np.array([np.load("./results/shared/BCQ_shared_{}-v0_{}.npy".format(args.data, seed)) for seed in range(3)]).transpose()
    rewards_avg = np.mean(rewards, axis = 1)
    print(np.round(np.mean(rewards_avg[99:109]), 3))

if __name__ == "__main__":
	
	parser = argparse.ArgumentParser()
	parser.add_argument("--data", default='hopper-random')
	args = parser.parse_args()
	compute(args)