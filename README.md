# AI_final_project_2024 <br> Batch-Constrained deep Q-learning(BCQ) on D4RL and ablation study

## Member
- 111550049 林德倫
- 111550151 徐嘉亨
- 111550175 劉承翰
- 111550079 方品仁

## Introduction
We first train original BCQ algorithm with D4RL dataset to be our baseline. And we do ablation study based on three methods different from original BCQ.
1. We replace the variational auto-encoder(VAE) with conditional generative adversarial nets(CGAN).
2. They modify the original Clipped Double Q-learning:
   $$y = r + \gamma\max\limits_{a_i}\left[\min\limits_{j=1,2} Q_{\theta'_j} (s',a_i)\right]$$

   into:
   $$y = r + \gamma\max\limits_{a_i}\left[\lambda\min\limits_{j=1,2} Q_{\theta_j'} (s',a_i) + (1-\lambda) \max\limits_{j=1,2} Q_{\theta'_j} (s',a_i) \right]$$
   You can notice that if $\lambda =1$, it just the original Clipped Double Q-learning. And we use four Q-networks to do Clipped Quadruple Q-learning:

   $$y = r + \gamma\max\limits_{a_i}\left[\lambda\min\limits_{j=1,2, 3, 4} Q_{\theta_j'} (s',a_i) + (1-\lambda) \max\limits_{j=1,2, 3, 4} Q_{\theta'_j} (s',a_i) \right]$$

4. We make the Actor and Critic shared the first layer.

## Setup for Mujoco and D4RL
Because setup for D4RL is a bit complicated and it can't be installed in Windows. We install it under Ubuntu 20.04, but you can also install it in mac. You can refer to this link [An Installation Guide for MuJoCo and D4RL](https://docs.google.com/document/d/1yo4O9M0s-bUtiBRJLTAsi9_4UaEzf5yc8c5q-Ble3VU/edit). Based on the guide, our coding environment is a conda virtual environment where the version of python is 3.8.

## Other requirement
You should first enter the conda virtual environment and install the required packages in requirements.txt one by one. Or you can just run the following:
```
pip install -r requirements.txt
```

## Dataset
We use ten datasets based on two tasks in mujoco: 1. Hopper 2. Walker2d

- hopper-random-v0
- hopper-medium-v0
- hopper-expert-v0
- hopper-medium-replay-v0
- hopper-medium-expert-v0
- walker2d-random-v0
- walker2d-medium-v0
- walker2d-expert-v0
- walker2d-medium-replay-v0
- walker2d-medium-expert-v0

## Train
- Original BCQ
```
python main.py
```
- BCQ with CGAN
```
python main.py --method BCQ_GAN
```
- BCQ with clipped quadruple Q-learning
```
python main.py --method BCQ_quadruple
```
- BCQ with shared layer
```
python main.py --method BCQ_shared
```

## Plot the result
- Original BCQ
```
python plot.py
```
- BCQ with CGAN
```
python plot.py --method GAN
```
- BCQ with clipped quadruple Q-learning
```
python plot.py --method quadruple
```
- BCQ with shared layer
```
python plot.py --method shared
```
- Compare CGAN with baseline
```
python compare_with_baseline.py --method GAN
```
- Compare clipped quadruple Q-learning with baseline
```
python compare_with_baseline.py --method quadruple
```
- Compare shared layer with baseline
```
python compare_with_baseline.py --method shared
```
- Compare all results together
```
python compare.py
```
