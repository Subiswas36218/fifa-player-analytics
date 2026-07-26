"""
src/data_loader.py

Data loading and validation utilities for the FIFA Player Analytics project.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

import pandas as pd
from sklearn.model_selection import train_test_split

from .config import RANDOM_STATE
from .utils import (
    dataframe_summary,
    duplicate_report,
    file_exists,
    logger,
    missing_value_report,
    optimize_memory,
    read_csv,
)


@dataclass(slots=True)
class DatasetMetadata:
    rows: int
    columns: int
    memory_mb: float
    duplicate_rows: int


class DataLoader:
    """Load, validate and split FIFA datasets."""

    def __init__(self, dataset_path: str | Path):
        self.dataset_path = Path(dataset_path)

    def load(self, optimize: bool = True) -> pd.DataFrame:
        if not file_exists(self.dataset_path):
            raise FileNotFoundError(self.dataset_path)

        logger.info("Loading dataset: %s", self.dataset_path)
        df = read_csv(self.dataset_path)

        if optimize:
            df = optimize_memory(df)

        logger.info("Loaded %d rows and %d columns", *df.shape)
        return df

    @staticmethod
    def validate_columns(
        df: pd.DataFrame,
        required_columns: Iterable[str],
    ) -> None:
        missing = sorted(set(required_columns) - set(df.columns))
        if missing:
            raise ValueError(f"Missing required columns: {missing}")

    @staticmethod
    def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
        out = df.copy()
        out.columns = (
            out.columns.str.strip()
            .str.lower()
            .str.replace(" ", "_", regex=False)
        )
        return out

    @staticmethod
    def metadata(df: pd.DataFrame) -> DatasetMetadata:
        dup = duplicate_report(df)["duplicate_rows"]
        mem = df.memory_usage(deep=True).sum() / (1024 ** 2)
        return DatasetMetadata(
            rows=len(df),
            columns=len(df.columns),
            memory_mb=round(mem, 2),
            duplicate_rows=dup,
        )

    @staticmethod
    def quality_report(df: pd.DataFrame) -> dict:
        return {
            "summary": dataframe_summary(df),
            "missing": missing_value_report(df),
            "duplicates": duplicate_report(df),
        }

    @staticmethod
    def split(
        df: pd.DataFrame,
        target: str,
        test_size: float = 0.2,
        validation_size: float = 0.1,
        random_state: int = RANDOM_STATE,
    ):
        X = df.drop(columns=[target])
        y = df[target]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=test_size,
            random_state=random_state,
        )

        val_ratio = validation_size / (1 - test_size)

        X_train, X_val, y_train, y_val = train_test_split(
            X_train,
            y_train,
            test_size=val_ratio,
            random_state=random_state,
        )

        return (
            X_train,
            X_val,
            X_test,
            y_train,
            y_val,
            y_test,
        )


__all__ = [
    "DatasetMetadata",
    "DataLoader",
]