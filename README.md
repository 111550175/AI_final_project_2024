# AI_final_project_2024 <br> Generate text summaries from movie screenshots

## Member
- 111550049 林德倫
- 111550151 徐嘉亨
- 111550175 劉承翰
- 111550079 方品仁

## Introduction
We first train original BCQ algorithm with D4RL dataset to be our baseline. And we do ablation study based on three method different from original BCQ.
1. aa

## Train
- Original BCQ
```
python main.py
```
- BCQ with CGAN
```
python main.py --method BCQ_GAN
```
- BCQ with quadruple Q-networks
```
python main.py --method BCQ_quadruple
```
- BCQ with shared layer
```
python main.py --method BCQ_shared
```
