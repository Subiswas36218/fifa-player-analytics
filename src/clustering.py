
"""src/clustering.py

Clustering utilities for the FIFA Player Analytics project.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler


@dataclass(slots=True)
class ClusteringResult:
    n_clusters: int
    inertia: float
    silhouette: float


class PlayerClusterer:
    """Utilities for clustering FIFA players."""

    def __init__(self, random_state: int = 42):
        self.random_state = random_state
        self.scaler = StandardScaler()

    def prepare_features(self, df: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
        cols = [c for c in columns if c in df.columns]
        data = df[cols].copy()
        return pd.DataFrame(
            self.scaler.fit_transform(data),
            columns=cols,
            index=df.index,
        )

    def fit_kmeans(
        self,
        X: pd.DataFrame,
        n_clusters: int = 5,
    ) -> tuple[KMeans, pd.Series]:
        model = KMeans(
            n_clusters=n_clusters,
            random_state=self.random_state,
            n_init=10,
        )
        labels = pd.Series(model.fit_predict(X), index=X.index, name="cluster")
        return model, labels

    @staticmethod
    def evaluate(model: KMeans, X: pd.DataFrame, labels: pd.Series) -> ClusteringResult:
        sil = silhouette_score(X, labels) if len(labels.unique()) > 1 else 0.0
        return ClusteringResult(
            n_clusters=model.n_clusters,
            inertia=float(model.inertia_),
            silhouette=float(sil),
        )

    def elbow_curve(
        self,
        X: pd.DataFrame,
        k_min: int = 2,
        k_max: int = 10,
    ) -> pd.DataFrame:
        rows = []
        for k in range(k_min, k_max + 1):
            model = KMeans(
                n_clusters=k,
                random_state=self.random_state,
                n_init=10,
            )
            labels = model.fit_predict(X)
            sil = silhouette_score(X, labels) if k > 1 else 0.0
            rows.append(
                {
                    "k": k,
                    "inertia": model.inertia_,
                    "silhouette": sil,
                }
            )
        return pd.DataFrame(rows)

    @staticmethod
    def add_cluster_labels(df: pd.DataFrame, labels: pd.Series) -> pd.DataFrame:
        out = df.copy()
        out["cluster"] = labels.values
        return out

    @staticmethod
    def cluster_summary(df: pd.DataFrame, cluster_col: str = "cluster") -> pd.DataFrame:
        numeric = df.select_dtypes(include="number").columns.tolist()
        if cluster_col in numeric:
            numeric.remove(cluster_col)
        return df.groupby(cluster_col)[numeric].mean()

    @staticmethod
    def pca_projection(
        X: pd.DataFrame,
        n_components: int = 2,
    ) -> pd.DataFrame:
        pca = PCA(n_components=n_components)
        coords = pca.fit_transform(X)
        cols = [f"PC{i+1}" for i in range(n_components)]
        return pd.DataFrame(coords, columns=cols, index=X.index)

    @staticmethod
    def predict(model: KMeans, X: pd.DataFrame):
        return model.predict(X)


__all__ = [
    "ClusteringResult",
    "PlayerClusterer",
]
