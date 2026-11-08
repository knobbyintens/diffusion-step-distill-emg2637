"""Entry point for Accelerating Diffusion Sampling with Learned Step-Distillation."""

from .distill import build_model


def main():
    model = build_model()
    print("ready:", model)


if __name__ == "__main__":
    main()
