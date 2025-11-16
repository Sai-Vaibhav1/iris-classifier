# Iris Classifier (Decision Tree)

End‑to‑end Iris decision‑tree ML example for AI Fundamentals course assessment

# Overview

A simple machine learning project using the **Iris dataset**. Trains a **Decision Tree Classifier** to predict iris species based on flower measurements. Demonstrates the full ML workflow: data loading, training, prediction, and evaluation.

# Quick Start

```bash
git clone https://github.com/<YOUR_USERNAME>/iris-classifier.git
cd iris-classifier

python -m venv venv

# windows
source venv/Scripts/activate

pip install -r requirements.txt

python src/train.py --test-size 0.2 --random-state 42
