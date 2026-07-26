
"""
src/utils.py

Utility helpers for the FIFA Player Analytics project.
"""

from __future__ import annotations

import json
import logging
import pickle
import random
import time
from functools import wraps
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd

LOGGER_NAME = "fifa_player_analytics"


def get_logger(name: str = LOGGER_NAME) -> logging.Logger:
    logger = logging.getLogger(name)
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter(
                "[%(asctime)s] %(levelname)s - %(name)s - %(message)s"
            )
        )
        logger.addHandler(handler)
        logger.setLevel(logging.INFO)
    return logger


logger = get_logger()


def set_random_seed(seed: int = 42) -> None:
    random.seed(seed)
    np.random.seed(seed)


def ensure_directory(path: str | Path) -> Path:
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def file_exists(path: str | Path) -> bool:
    return Path(path).exists()


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        logger.info("%s finished in %.3fs", func.__name__, elapsed)
        return result

    return wrapper


@timer
def read_csv(path: str | Path, **kwargs) -> pd.DataFrame:
    return pd.read_csv(path, **kwargs)


def write_csv(df: pd.DataFrame, path: str | Path, **kwargs) -> None:
    ensure_directory(Path(path).parent)
    df.to_csv(path, index=False, **kwargs)


def read_excel(path: str | Path, **kwargs) -> pd.DataFrame:
    return pd.read_excel(path, **kwargs)


def write_excel(df: pd.DataFrame, path: str | Path, **kwargs) -> None:
    ensure_directory(Path(path).parent)
    df.to_excel(path, index=False, **kwargs)


def dataframe_summary(df: pd.DataFrame) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "dtype": df.dtypes.astype(str),
            "missing": df.isna().sum(),
            "missing_pct": (df.isna().mean() * 100).round(2),
            "unique": df.nunique(dropna=False),
        }
    )


def optimize_memory(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    for col in result.select_dtypes(include=["int"]).columns:
        result[col] = pd.to_numeric(result[col], downcast="integer")
    for col in result.select_dtypes(include=["float"]).columns:
        result[col] = pd.to_numeric(result[col], downcast="float")
    return result


def duplicate_report(df: pd.DataFrame) -> dict[str, Any]:
    dup = int(df.duplicated().sum())
    return {
        "duplicate_rows": dup,
        "duplicate_percentage": round(dup / max(len(df), 1) * 100, 2),
    }


def missing_value_report(df: pd.DataFrame) -> pd.DataFrame:
    rep = (
        df.isna()
        .sum()
        .rename("missing")
        .to_frame()
    )
    rep["percentage"] = (rep["missing"] / len(df) * 100).round(2)
    return rep.sort_values("missing", ascending=False)


def numeric_statistics(df: pd.DataFrame) -> pd.DataFrame:
    return df.describe(include=[np.number]).T


def categorical_statistics(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for c in df.select_dtypes(exclude=[np.number]).columns:
        rows.append(
            {
                "column": c,
                "unique": df[c].nunique(dropna=False),
                "top": df[c].mode(dropna=False).iloc[0] if not df[c].empty else None,
            }
        )
    return pd.DataFrame(rows)


def save_pickle(obj: Any, path: str | Path) -> None:
    ensure_directory(Path(path).parent)
    with open(path, "wb") as f:
        pickle.dump(obj, f)


def load_pickle(path: str | Path) -> Any:
    with open(path, "rb") as f:
        return pickle.load(f)


def save_joblib(obj: Any, path: str | Path) -> None:
    ensure_directory(Path(path).parent)
    joblib.dump(obj, path)


def load_joblib(path: str | Path) -> Any:
    return joblib.load(path)


def save_json(data: Any, path: str | Path) -> None:
    ensure_directory(Path(path).parent)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def load_json(path: str | Path) -> Any:
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_figure(fig, path: str | Path, dpi: int = 300) -> None:
    ensure_directory(Path(path).parent)
    fig.savefig(path, dpi=dpi, bbox_inches="tight")


def print_header(title: str) -> None:
    line = "=" * len(title)
    print(f"\n{line}\n{title}\n{line}")


__all__ = [
    "logger",
    "get_logger",
    "set_random_seed",
    "ensure_directory",
    "file_exists",
    "timer",
    "read_csv",
    "write_csv",
    "read_excel",
    "write_excel",
    "dataframe_summary",
    "missing_value_report",
    "duplicate_report",
    "numeric_statistics",
    "categorical_statistics",
    "optimize_memory",
    "save_pickle",
    "load_pickle",
    "save_joblib",
    "load_joblib",
    "save_json",
    "load_json",
    "save_figure",
    "print_header",
]
