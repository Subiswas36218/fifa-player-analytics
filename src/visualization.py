
"""src/visualization.py

Reusable visualization helpers for FIFA Player Analytics.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px


class Visualizer:
    """Collection of reusable plotting utilities."""

    def __init__(self, figsize: tuple[int, int] = (12, 6)) -> None:
        self.figsize = figsize

    def correlation_heatmap(self, df: pd.DataFrame, output: str | Path | None = None):
        corr = df.select_dtypes("number").corr()
        fig, ax = plt.subplots(figsize=self.figsize)
        im = ax.imshow(corr, aspect="auto")
        ax.set_xticks(range(len(corr.columns)))
        ax.set_xticklabels(corr.columns, rotation=90, fontsize=7)
        ax.set_yticks(range(len(corr.columns)))
        ax.set_yticklabels(corr.columns, fontsize=7)
        fig.colorbar(im)
        fig.tight_layout()
        if output:
            fig.savefig(output, dpi=300, bbox_inches="tight")
        return fig

    def histogram(self, df: pd.DataFrame, column: str):
        fig, ax = plt.subplots(figsize=self.figsize)
        ax.hist(df[column].dropna(), bins=30)
        ax.set_title(column)
        return fig

    def boxplot(self, df: pd.DataFrame, column: str):
        fig, ax = plt.subplots(figsize=self.figsize)
        ax.boxplot(df[column].dropna())
        ax.set_title(column)
        return fig

    def scatter(self, df: pd.DataFrame, x: str, y: str, color: str | None = None):
        return px.scatter(df, x=x, y=y, color=color,
                          title=f"{y} vs {x}")

    def bar(self, df: pd.DataFrame, category: str, value: str):
        agg = df.groupby(category, dropna=False)[value].mean().reset_index()
        return px.bar(agg, x=category, y=value,
                      title=f"Average {value} by {category}")

    def top_players(self, df: pd.DataFrame, metric: str, n: int = 10):
        cols = [c for c in ["short_name", metric] if c in df.columns]
        top = df[cols].nlargest(n, metric)
        return px.bar(top, x="short_name", y=metric,
                      title=f"Top {n} Players by {metric}")

    def position_distribution(self, df: pd.DataFrame):
        col = "club_position" if "club_position" in df.columns else "player_positions"
        counts = df[col].value_counts().reset_index()
        counts.columns = ["position", "count"]
        return px.bar(counts, x="position", y="count",
                      title="Position Distribution")

    def nationality_distribution(self, df: pd.DataFrame, n: int = 15):
        counts = (
            df["nationality_name"]
            .value_counts()
            .head(n)
            .reset_index()
        )
        counts.columns = ["nationality", "count"]
        return px.bar(counts, x="nationality", y="count",
                      title="Top Nationalities")

    def radar_dataframe(self, player: pd.Series, attributes: list[str]) -> pd.DataFrame:
        return pd.DataFrame({
            "attribute": attributes,
            "value": [player.get(a, 0) for a in attributes],
        })

    def radar_chart(self, player: pd.Series, attributes: list[str]):
        rdf = self.radar_dataframe(player, attributes)
        return px.line_polar(
            rdf,
            r="value",
            theta="attribute",
            line_close=True,
            title=player.get("short_name", "Player"),
        )

    @staticmethod
    def save_plotly(fig, path: str | Path):
        fig.write_html(str(path))


__all__ = ["Visualizer"]
