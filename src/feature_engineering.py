
"""
src/feature_engineering.py

Feature engineering utilities for the FIFA Player Analytics project.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd


@dataclass(slots=True)
class FeatureEngineeringConfig:
    age_bins: tuple = (0, 20, 24, 28, 32, 100)
    age_labels: tuple = (
        "Youth",
        "Rising Star",
        "Prime",
        "Experienced",
        "Veteran",
    )


class FeatureEngineer:
    """Create engineered football features."""

    def __init__(self) -> None:
        self.config = FeatureEngineeringConfig()

    @staticmethod
    def _mean(df: pd.DataFrame, cols: list[str]) -> pd.Series:
        cols = [c for c in cols if c in df.columns]
        if not cols:
            return pd.Series(np.nan, index=df.index)
        return df[cols].mean(axis=1)

    def add_age_group(self, df: pd.DataFrame) -> pd.DataFrame:
        out = df.copy()
        if "age" in out.columns:
            out["age_group"] = pd.cut(
                out["age"],
                bins=self.config.age_bins,
                labels=self.config.age_labels,
                include_lowest=True,
            )
        return out

    def add_scores(self, df: pd.DataFrame) -> pd.DataFrame:
        out = df.copy()

        out["technical_score"] = self._mean(
            out,
            [
                "skill_ball_control",
                "skill_dribbling",
                "attacking_short_passing",
                "skill_long_passing",
            ],
        )

        out["physical_score"] = self._mean(
            out,
            [
                "power_strength",
                "power_stamina",
                "movement_sprint_speed",
                "movement_acceleration",
            ],
        )

        out["mental_score"] = self._mean(
            out,
            [
                "mentality_composure",
                "mentality_vision",
                "movement_reactions",
            ],
        )

        out["offensive_score"] = self._mean(
            out,
            [
                "attacking_finishing",
                "attacking_volleys",
                "power_shot_power",
                "attacking_positioning",
            ],
        )

        out["defensive_score"] = self._mean(
            out,
            [
                "defending_standing_tackle",
                "defending_sliding_tackle",
                "mentality_interceptions",
                "defending_marking_awareness",
            ],
        )

        out["passing_score"] = self._mean(
            out,
            [
                "attacking_short_passing",
                "skill_long_passing",
                "mentality_vision",
            ],
        )

        return out

    @staticmethod
    def add_financial_features(df: pd.DataFrame) -> pd.DataFrame:
        out = df.copy()

        if {"wage_eur", "value_eur"}.issubset(out.columns):
            out["wage_value_ratio"] = (
                out["wage_eur"] / out["value_eur"].replace(0, np.nan)
            )

        if {"potential", "overall"}.issubset(out.columns):
            out["potential_gap"] = out["potential"] - out["overall"]

        return out

    @staticmethod
    def add_bmi(df: pd.DataFrame) -> pd.DataFrame:
        out = df.copy()
        if {"height_cm", "weight_kg"}.issubset(out.columns):
            h = out["height_cm"] / 100
            out["bmi"] = out["weight_kg"] / (h * h)
        return out

    @staticmethod
    def add_is_young_talent(df: pd.DataFrame) -> pd.DataFrame:
        out = df.copy()
        if {"age", "potential"}.issubset(out.columns):
            out["young_talent"] = (
                (out["age"] <= 23) & (out["potential"] >= 80)
            ).astype(int)
        return out

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        out = self.add_age_group(df)
        out = self.add_scores(out)
        out = self.add_financial_features(out)
        out = self.add_bmi(out)
        out = self.add_is_young_talent(out)
        return out


__all__ = [
    "FeatureEngineeringConfig",
    "FeatureEngineer",
]
