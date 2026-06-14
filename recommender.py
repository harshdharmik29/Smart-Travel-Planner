"""
recommender.py
Simple rule-based recommendation logic (no ML yet).
Filters destinations based on user's budget and preferred trip type,
and assigns a basic suitability score.
"""

import pandas as pd


def load_destinations(csv_path: str = "data/destinations.csv") -> pd.DataFrame:
    """Loads the destinations dataset from CSV."""
    return pd.read_csv(csv_path)


def recommend_destinations(df: pd.DataFrame, user_budget: int, preferred_type: str = None) -> pd.DataFrame:
    """
    Filters and scores destinations based on user's daily budget and
    optional preferred trip type (e.g., 'City/Heritage').

    Scoring logic:
    - Destination is included if user_budget falls between budget_low and budget_high.
    - A 'budget_fit' score (0-100) shows how close the budget is to the mid-range.
    - If preferred_type is given, destinations matching that type get a small bonus.
    """
    results = df.copy()

    # Filter: budget should fall within the destination's range
    results = results[
        (results["budget_low"] <= user_budget) &
        (results["budget_high"] >= user_budget)
    ]

    if results.empty:
        return results

    # Score: closer to budget_mid = higher score
    results["budget_fit"] = results.apply(
        lambda row: 100 - abs(user_budget - row["budget_mid"]) / row["budget_mid"] * 100,
        axis=1
    )

    # Bonus if trip type matches user preference
    if preferred_type:
        results["budget_fit"] += results["type"].apply(
            lambda t: 10 if preferred_type.lower() in t.lower() else 0
        )

    results = results.sort_values(by="budget_fit", ascending=False)
    return results


def get_budget_label(user_budget: int, row: pd.Series) -> str:
    """Returns a human-friendly label for how the user's budget compares."""
    if user_budget <= row["budget_low"] + (row["budget_mid"] - row["budget_low"]) / 2:
        return "Budget"
    elif user_budget <= row["budget_mid"] + (row["budget_high"] - row["budget_mid"]) / 2:
        return "Mid-range"
    else:
        return "Luxury"
