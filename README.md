# AI_final_project_2024 <br> Generate text summaries from movie screenshots

## Member
- 111550049 林德倫
- 111550151 徐嘉亨
- 111550175 劉承翰
- 111550079 方品仁

## Introduction
We first train original BCQ algorithm with D4RL dataset to be our baseline. And we do ablation study based on three method different from original BCQ.
1. We replace the variational auto-encoder (VAE) with conditional generative adversarial nets (CGAN).
2. They modify the original Clipped Double Q-learning:
$$y = r + \gamma\max\limits_{a_i}\left[\min\limits_{j=1,2} Q_{\theta'_j} (s',a_i)\right]$$

into:
$$y = r + \gamma\max\limits_{a_i}\left[\lambda\min\limits_{j=1,2} Q_{\theta_j'} (s',a_i) + (1-\lambda) \max\limits_{j=1,2} Q_{\theta'_j} (s',a_i) \right]$$
You can notice that if $\lambda =1$, it just the original Clipped Double Q-learning. And we use four Q-networks to do Clipped Quadruple Q-learning:

$$y = r + \gamma\max\limits_{a_i}\left[\lambda\min\limits_{j=1,2, 3, 4} Q_{\theta_j'} (s',a_i) + (1-\lambda) \max\limits_{j=1,2, 3, 4} Q_{\theta'_j} (s',a_i) \right]$$

3. We make the Actor and Critic shared the first layer.

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
