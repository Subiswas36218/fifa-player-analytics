
"""src/explainability.py

Model explainability utilities for the FIFA Player Analytics project.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import pandas as pd
import shap


class ModelExplainer:
    """Wrapper around SHAP explainers for tree-based models."""

    def __init__(self, model: Any, X: pd.DataFrame):
        self.model = model
        self.X = X
        self.explainer = shap.Explainer(model, X)
        self.shap_values = None

    def compute(self):
        """Compute SHAP values."""
        self.shap_values = self.explainer(self.X)
        return self.shap_values

    def summary_plot(self, show: bool = False, save_path: str | Path | None = None):
        if self.shap_values is None:
            self.compute()
        shap.summary_plot(self.shap_values, self.X, show=show)
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches="tight")
        fig = plt.gcf()
        if not show:
            plt.close(fig)
        return fig

    def bar_plot(self, show: bool = False, save_path: str | Path | None = None):
        if self.shap_values is None:
            self.compute()
        shap.plots.bar(self.shap_values, show=show)
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches="tight")
        fig = plt.gcf()
        if not show:
            plt.close(fig)
        return fig

    def dependence_plot(
        self,
        feature: str,
        show: bool = False,
        save_path: str | Path | None = None,
    ):
        if self.shap_values is None:
            self.compute()
        shap.dependence_plot(
            feature,
            self.shap_values.values,
            self.X,
            show=show,
        )
        if save_path:
            plt.savefig(save_path, dpi=300, bbox_inches="tight")
        fig = plt.gcf()
        if not show:
            plt.close(fig)
        return fig

    def local_explanation(self, index: int = 0):
        if self.shap_values is None:
            self.compute()
        return self.shap_values[index]

    def feature_importance(self) -> pd.DataFrame:
        if self.shap_values is None:
            self.compute()
        importance = (
            pd.DataFrame({
                "feature": self.X.columns,
                "importance": abs(self.shap_values.values).mean(axis=0),
            })
            .sort_values("importance", ascending=False)
            .reset_index(drop=True)
        )
        return importance

    @staticmethod
    def save_importance(df: pd.DataFrame, path: str | Path):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        df.to_csv(path, index=False)


__all__ = ["ModelExplainer"]
