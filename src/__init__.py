"""
FIFA Player Analytics
=====================

A modular Python package supporting the FIFA Player Analytics project.

This package provides reusable utilities for:

- Data loading
- Data preprocessing
- Feature engineering
- Exploratory data analysis
- Visualization
- Machine learning
- Clustering
- Explainable AI
- Player similarity search

The project is designed to complement the accompanying Jupyter notebooks,
keeping reusable logic inside the `src` package while notebooks focus on
analysis and experimentation.
"""

from .config import (
    CATEGORICAL_FEATURES,
    DATA_DIR,
    DOCS_DIR,
    ENGINEERED_FEATURES,
    EXTERNAL_DATA_DIR,
    IDENTIFIER_COLUMNS,
    IMAGES_DIR,
    MODELS_DIR,
    NOTEBOOKS_DIR,
    NUMERIC_FEATURES,
    POSITION_GROUPS,
    PROCESSED_DATASET,
    PROCESSED_DATA_DIR,
    PROJECT_ROOT,
    RANDOM_STATE,
    RAW_DATASET,
    RAW_DATA_DIR,
    REPORTS_DIR,
    TARGET_MARKET_VALUE,
    TARGET_OVERALL,
    TARGET_POTENTIAL,
    TARGET_WAGE,
)

__author__ = "Subhankar Biswas"
__email__ = "subhankar@example.com"
__version__ = "1.0.0"
__license__ = "MIT"

__all__ = [
    "__author__",
    "__email__",
    "__license__",
    "__version__",
    "PROJECT_ROOT",
    "DATA_DIR",
    "RAW_DATA_DIR",
    "PROCESSED_DATA_DIR",
    "EXTERNAL_DATA_DIR",
    "NOTEBOOKS_DIR",
    "MODELS_DIR",
    "REPORTS_DIR",
    "IMAGES_DIR",
    "DOCS_DIR",
    "RAW_DATASET",
    "PROCESSED_DATASET",
    "RANDOM_STATE",
    "TARGET_MARKET_VALUE",
    "TARGET_WAGE",
    "TARGET_OVERALL",
    "TARGET_POTENTIAL",
    "IDENTIFIER_COLUMNS",
    "NUMERIC_FEATURES",
    "CATEGORICAL_FEATURES",
    "ENGINEERED_FEATURES",
    "POSITION_GROUPS",
]