# Accelerating Diffusion Sampling with Learned Step-Distillation

Reference implementation accompanying the paper *Accelerating Diffusion Sampling with Learned Step-Distillation*.

Training and sampling utilities for distilled diffusion models.

## Installation

```bash
git clone https://github.com/knobbyintens/diffusion-step-distill-emg2637.git
cd diffusion-step-distill-emg2637
pip install -r requirements.txt
```

## Repository layout

- `src/train_distill.py` — training / evaluation entry point
- `src/distill.py` — core implementation
- `tests/` — unit tests
