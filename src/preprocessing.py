
"""
src/preprocessing.py

Preprocessing utilities for the FIFA Player Analytics project.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler


@dataclass(slots=True)
class PreprocessingArtifacts:
    numeric_imputer: SimpleImputer
    categorical_imputer: SimpleImputer
    scaler: StandardScaler | None = None
    encoder: OneHotEncoder | None = None


class Preprocessor:
    """Reusable preprocessing pipeline for FIFA datasets."""

    def __init__(self) -> None:
        self.numeric_imputer = SimpleImputer(strategy="median")
        self.categorical_imputer = SimpleImputer(strategy="most_frequent")
        self.scaler = StandardScaler()

    @staticmethod
    def drop_duplicates(df: pd.DataFrame) -> pd.DataFrame:
        return df.drop_duplicates().reset_index(drop=True)

    @staticmethod
    def remove_empty_columns(df: pd.DataFrame) -> pd.DataFrame:
        return df.dropna(axis=1, how="all")

    @staticmethod
    def standardize_strings(df: pd.DataFrame, columns: Iterable[str]) -> pd.DataFrame:
        out = df.copy()
        for col in columns:
            if col in out.columns:
                out[col] = out[col].astype("string").str.strip().str.replace(r"\s+", " ", regex=True)
        return out

    @staticmethod
    def convert_numeric(df: pd.DataFrame, columns: Iterable[str]) -> pd.DataFrame:
        out = df.copy()
        for col in columns:
            if col in out.columns:
                out[col] = pd.to_numeric(out[col], errors="coerce")
        return out

    def impute(self, df: pd.DataFrame) -> pd.DataFrame:
        out = df.copy()
        num = out.select_dtypes(include=np.number).columns
        cat = out.select_dtypes(exclude=np.number).columns
        if len(num):
            out[num] = self.numeric_imputer.fit_transform(out[num])
        if len(cat):
            out[cat] = self.categorical_imputer.fit_transform(out[cat])
        return out

    def scale(self, df: pd.DataFrame, columns: Iterable[str]) -> pd.DataFrame:
        out = df.copy()
        cols = [c for c in columns if c in out.columns]
        if cols:
            out[cols] = self.scaler.fit_transform(out[cols])
        return out

    @staticmethod
    def clip_outliers_iqr(df: pd.DataFrame, columns: Iterable[str], multiplier: float = 1.5) -> pd.DataFrame:
        out = df.copy()
        for col in columns:
            if col not in out.columns:
                continue
            q1 = out[col].quantile(0.25)
            q3 = out[col].quantile(0.75)
            iqr = q3 - q1
            out[col] = out[col].clip(q1 - multiplier * iqr, q3 + multiplier * iqr)
        return out

    def fit_transform(self, df: pd.DataFrame, numeric_columns: Iterable[str], categorical_columns: Iterable[str]) -> pd.DataFrame:
        out = self.drop_duplicates(df)
        out = self.remove_empty_columns(out)
        out = self.standardize_strings(out, categorical_columns)
        out = self.convert_numeric(out, numeric_columns)
        out = self.impute(out)
        out = self.scale(out, numeric_columns)
        return out

    def artifacts(self) -> PreprocessingArtifacts:
        return PreprocessingArtifacts(
            numeric_imputer=self.numeric_imputer,
            categorical_imputer=self.categorical_imputer,
            scaler=self.scaler,
        )


__all__ = ["PreprocessingArtifacts", "Preprocessor"]