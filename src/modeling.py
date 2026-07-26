
"""src/modeling.py

Reusable machine learning utilities for the FIFA Player Analytics project.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import joblib
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)
from sklearn.model_selection import GridSearchCV, cross_val_score
from xgboost import XGBRegressor


@dataclass(slots=True)
class ModelResult:
    model_name: str
    mae: float
    rmse: float
    r2: float


class ModelTrainer:
    """Train, evaluate and persist regression models."""

    def __init__(self, random_state: int = 42):
        self.random_state = random_state

    def linear_regression(self) -> LinearRegression:
        return LinearRegression()

    def random_forest(self) -> RandomForestRegressor:
        return RandomForestRegressor(
            n_estimators=300,
            random_state=self.random_state,
            n_jobs=-1,
        )

    def xgboost(self) -> XGBRegressor:
        return XGBRegressor(
            n_estimators=300,
            learning_rate=0.05,
            max_depth=6,
            subsample=0.8,
            colsample_bytree=0.8,
            random_state=self.random_state,
            objective="reg:squarederror",
        )

    @staticmethod
    def fit(model: Any, X_train: pd.DataFrame, y_train: pd.Series):
        model.fit(X_train, y_train)
        return model

    @staticmethod
    def predict(model: Any, X: pd.DataFrame):
        return model.predict(X)

    @staticmethod
    def evaluate(model: Any, X_test: pd.DataFrame, y_test: pd.Series) -> ModelResult:
        preds = model.predict(X_test)
        return ModelResult(
            model_name=model.__class__.__name__,
            mae=mean_absolute_error(y_test, preds),
            rmse=mean_squared_error(y_test, preds) ** 0.5,
            r2=r2_score(y_test, preds),
        )

    @staticmethod
    def cross_validate(model: Any, X: pd.DataFrame, y: pd.Series, cv: int = 5):
        return cross_val_score(model, X, y, cv=cv, scoring="r2")

    @staticmethod
    def feature_importance(model: Any, feature_names: list[str]) -> pd.DataFrame:
        if not hasattr(model, "feature_importances_"):
            raise ValueError("Model does not expose feature_importances_.")
        imp = pd.DataFrame(
            {
                "feature": feature_names,
                "importance": model.feature_importances_,
            }
        )
        return imp.sort_values("importance", ascending=False).reset_index(drop=True)

    @staticmethod
    def grid_search(model: Any, params: dict, X_train, y_train, cv: int = 5):
        search = GridSearchCV(
            estimator=model,
            param_grid=params,
            cv=cv,
            scoring="r2",
            n_jobs=-1,
        )
        search.fit(X_train, y_train)
        return search

    @staticmethod
    def save_model(model: Any, path: str | Path):
        Path(path).parent.mkdir(parents=True, exist_ok=True)
        joblib.dump(model, path)

    @staticmethod
    def load_model(path: str | Path):
        return joblib.load(path)


__all__ = [
    "ModelResult",
    "ModelTrainer",
]
