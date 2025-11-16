import os
import sys
import pytest

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src"))

from train import train_and_evaluate


def test_accuracy_above_threshold():
    """Ensure the model achieves at least 0.90 accuracy."""
    accuracy = train_and_evaluate(test_size=0.2, random_state=42)
    assert accuracy >= 0.90
