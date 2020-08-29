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

I borrowed my code from azerite trait calculations for this. All numbers use BFA
values. When calculating Legion values, secondary stats are delinearized but not
relinearzed. (BFA values are delinearized then relinearized).
