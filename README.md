# Secondary Stat Scaling Models

This repository includes implementations of the BFA, Legion, and Shadowlands
secondary stat models, along with a very basic damage model.


| Model | Secondary Scaling Type | DRs? |
|-------|------------------------|------|
| Legion | Exponential | No |
| BFA | Linear | No |
| Shadowlands | Linear | Yes |

## Damage Model

These results use a basic damage model:

```python
damage = ap * prod(1 + pct(stat) * value(stat) for stat in [crit, haste, vers, mastery])
```

## Rating Calculations

I borrowed my code from azerite trait calculations for this. All numbers use BFA values. When calculating Legion values, secondary stats are delinearized but not relinearzed. (BFA values are delinearized then linearized).

## Results

The `results/` folder contains some estimated results.

- X axis: ilvl change
- Y axis: damage change
- rows: model used
- columns: stats used (see below)
- colors: setting used (see below)

Additionally, the title describes how secondary values (`value(stat)`) and
initial stats from gear are set.

### Initial Gear

Gear is determined entirely based on an avg ilvl in combination with a secondary stat *rating* distribution.

The stat distributions used in the results folder are:

- **Even:** `[0.25, 0.25, 0.25, 0.25]` (Crit, Haste, Vers, Mastery)
- **Skewed:** `[0.35, 0.3, 0.2, 0.15]` (Crit, Haste, Vers, Mastery)

Remember that different stats have different rating->percentage conversion rates.

### Secondary Values

Secondary values are used to impose relative values on *stat percentages* (not ratings!).

The stat values used in the results folder are:

- **Even:** `[1, 1, 1, 1]` (aka everything is full value)
- **Skewed:** `[1, 0.8, 0.6, 0.2]` (Crit, Haste, Vers, Mastery)

### Settings Used

The different settings describe different ways of distributing the stats used.

- **Basic:** Use existing stat distribution.
- **Even:** 50/50 split between two stats.
- **Semi-Skewed:** 60/40 split between two stats.
- **Skewed:** 80/20 split between two stats.
- **Extreme:** 100/0 split between two stats.

### Stats Used

- **Average:** use the avg stat distribution from current gear
- **Best:** use the 2 best secondaries
- **Worst:** use the 2 worst secondaries

The best/worst stats are calculated by taking the gradient with no changes to current gear.

The *basic* setting and *average* stats always appear together.
