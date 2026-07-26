
"""src/similarity.py

Player similarity search utilities for the FIFA Player Analytics project.
"""

from __future__ import annotations

from dataclasses import dataclass

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import StandardScaler


@dataclass(slots=True)
class SimilarPlayer:
    index: int
    score: float


class PlayerSimilarity:
    """Compute player similarity using cosine similarity."""

    def __init__(self) -> None:
        self.scaler = StandardScaler()
        self.feature_columns: list[str] = []
        self.matrix = None
        self.data = None

    def fit(self, df: pd.DataFrame, feature_columns: list[str]) -> "PlayerSimilarity":
        self.feature_columns = [c for c in feature_columns if c in df.columns]
        self.data = df.reset_index(drop=True).copy()
        X = self.data[self.feature_columns].fillna(0)
        X = self.scaler.fit_transform(X)
        self.matrix = cosine_similarity(X)
        return self

    def similar_by_index(self, index: int, top_n: int = 10) -> pd.DataFrame:
        if self.matrix is None or self.data is None:
            raise RuntimeError("Call fit() before querying.")
        scores = pd.Series(self.matrix[index], index=self.data.index)
        scores = scores.drop(index).sort_values(ascending=False).head(top_n)
        result = self.data.loc[scores.index].copy()
        result["similarity_score"] = scores.values
        return result

    def similar_by_name(
        self,
        player_name: str,
        name_column: str = "short_name",
        top_n: int = 10,
    ) -> pd.DataFrame:
        if self.data is None:
            raise RuntimeError("Call fit() before querying.")
        matches = self.data.index[
            self.data[name_column].astype(str).str.lower() == player_name.lower()
        ]
        if len(matches) == 0:
            raise ValueError(f"Player '{player_name}' not found.")
        return self.similar_by_index(int(matches[0]), top_n)

    @staticmethod
    def similarity_matrix(df: pd.DataFrame, feature_columns: list[str]) -> pd.DataFrame:
        cols = [c for c in feature_columns if c in df.columns]
        scaled = StandardScaler().fit_transform(df[cols].fillna(0))
        sim = cosine_similarity(scaled)
        return pd.DataFrame(sim, index=df.index, columns=df.index)

    @staticmethod
    def top_pairs(
        sim_matrix: pd.DataFrame,
        top_n: int = 20,
    ) -> pd.DataFrame:
        pairs = []
        for i in range(len(sim_matrix)):
            for j in range(i + 1, len(sim_matrix)):
                pairs.append((i, j, sim_matrix.iat[i, j]))
        out = (
            pd.DataFrame(pairs, columns=["player_1", "player_2", "similarity"])
            .sort_values("similarity", ascending=False)
            .head(top_n)
            .reset_index(drop=True)
        )
        return out


__all__ = [
    "SimilarPlayer",
    "PlayerSimilarity",
]
