import seaborn as sns
import pandas as pd

from . import sim


def fight(*args, **kwargs):
    df = pd.DataFrame(
        columns=["damage", "chance"], data=list(sim.fight(*args, **kwargs))
    )
    df["agg"] = df.damage * df.chance
    mean = df["agg"].sum()

    current_palette = sns.color_palette()

    print(f"Mean damage {mean}")
    ax = sns.barplot("damage", "chance", data=df, color=current_palette[0])
    ax.axvline(mean, color=current_palette[1], linestyle="--")
