
## Configuration module for the FIFA Player Analytics project.

## This module centralizes project settings including:

## - Directory paths
## - Machine learning parameters
## - Feature definitions
## - Target columns

from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR = PROJECT_ROOT / "data"

RAW_DATA_DIR = DATA_DIR / "raw"

PROCESSED_DATA_DIR = DATA_DIR / "processed"

EXTERNAL_DATA_DIR = DATA_DIR / "external"

NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"

MODELS_DIR = PROJECT_ROOT / "models"

REPORTS_DIR = PROJECT_ROOT / "reports"

IMAGES_DIR = PROJECT_ROOT / "images"

DOCS_DIR = PROJECT_ROOT / "docs"

DATASET_FILENAME = "players.csv"

RAW_DATASET = RAW_DATA_DIR / DATASET_FILENAME

PROCESSED_DATASET = PROCESSED_DATA_DIR / "players_cleaned.csv"


RANDOM_STATE = 42

TEST_SIZE = 0.20

VALIDATION_SIZE = 0.10


TARGET_MARKET_VALUE = "value_eur"

TARGET_WAGE = "wage_eur"

TARGET_OVERALL = "overall"

TARGET_POTENTIAL = "potential"

IDENTIFIER_COLUMNS = [
    "short_name",
    "long_name",
    "club_name",
    "club_position",
    "nationality_name",
]

NUMERIC_FEATURES = [

    "age",

    "height_cm",

    "weight_kg",

    "overall",

    "potential",

    "value_eur",

    "wage_eur",

    "release_clause_eur",

    "pace",

    "shooting",

    "passing",

    "dribbling",

    "defending",

    "physic",

    "attacking_crossing",

    "attacking_finishing",

    "attacking_heading_accuracy",

    "attacking_short_passing",

    "attacking_volleys",

    "skill_dribbling",

    "skill_curve",

    "skill_fk_accuracy",

    "skill_long_passing",

    "skill_ball_control",

    "movement_acceleration",

    "movement_sprint_speed",

    "movement_agility",

    "movement_reactions",

    "movement_balance",

    "power_shot_power",

    "power_jumping",

    "power_stamina",

    "power_strength",

    "power_long_shots",

    "mentality_aggression",

    "mentality_interceptions",

    "mentality_positioning",

    "mentality_vision",

    "mentality_penalties",

    "mentality_composure",

    "defending_marking_awareness",

    "defending_standing_tackle",

    "defending_sliding_tackle",

    "goalkeeping_diving",

    "goalkeeping_handling",

    "goalkeeping_kicking",

    "goalkeeping_positioning",

    "goalkeeping_reflexes",
]


CATEGORICAL_FEATURES = [

    "preferred_foot",

    "work_rate",

    "body_type",

    "club_name",

    "league_name",

    "nationality_name",

    "club_position",
]


ENGINEERED_FEATURES = [

    "technical_score",

    "physical_score",

    "mental_score",

    "offensive_score",

    "defensive_score",

    "passing_score",

    "goalkeeping_score",

    "wage_value_ratio",

    "potential_gap",

    "experience_score",

    "age_group",
]


POSITION_GROUPS = {

    "Goalkeeper": [
        "GK",
    ],

    "Defender": [
        "CB",
        "LB",
        "RB",
        "LWB",
        "RWB",
    ],

    "Midfielder": [
        "CDM",
        "CM",
        "CAM",
        "LM",
        "RM",
    ],

    "Forward": [
        "LW",
        "RW",
        "CF",
        "ST",
    ],
}


FIGURE_WIDTH = 14

FIGURE_HEIGHT = 7

FIGURE_DPI = 120

PLOT_STYLE = "ggplot"

DEFAULT_CMAP = "viridis"

PLOTLY_TEMPLATE = "plotly_white"


HIGH_CORRELATION = 0.80

LOW_VARIANCE_THRESHOLD = 0.01

NUMERIC_IMPUTATION = "median"

CATEGORICAL_IMPUTATION = "most_frequent"

IQR_MULTIPLIER = 1.5


SCALER = "StandardScaler"

PCA_COMPONENTS = 2

N_CLUSTERS = 5

DBSCAN_EPS = 0.7

DBSCAN_MIN_SAMPLES = 8

RANDOM_FOREST_PARAMS = {

    "n_estimators": 300,

    "max_depth": 15,

    "random_state": RANDOM_STATE,

    "n_jobs": -1,
}

XGBOOST_PARAMS = {

    "n_estimators": 500,

    "learning_rate": 0.05,

    "max_depth": 6,

    "subsample": 0.8,

    "colsample_bytree": 0.8,

    "random_state": RANDOM_STATE,
}

LIGHTGBM_PARAMS = {

    "n_estimators": 500,

    "learning_rate": 0.05,

    "num_leaves": 31,

    "random_state": RANDOM_STATE,
}

TOP_K_SIMILAR_PLAYERS = 10

SIMILARITY_METRIC = "cosine"

MAX_SHAP_SAMPLES = 1000

CSV_INDEX = False

IMAGE_FORMAT = "png"

IMAGE_DPI = 300