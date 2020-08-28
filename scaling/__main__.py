#!/usr/bin/env python3
from scaling.plotting import build_eval_plot
from scaling.constants import SCALARS
from scaling import bfa, legion
from plotnine import ggtitle

systems = {
    'shadowlands': [bfa, 1],
    'bfa': [bfa, 0],
    'legion': [legion, 0],
}

for slot in SCALARS.keys():
    (build_eval_plot(systems,
                    [1, 1, 1, 1],
                    470, [0.25, 0.25, 0.25, 0.25],
                     slot) + ggtitle(f'Even Secondary Values, Even Stat Distribution (Slot: {slot})')).save(f'{slot}_even.png')

    (build_eval_plot(systems,
                    [1, 1, 1, 1],
                    470, [0.35, 0.3, 0.2, 0.15],
                     slot) + ggtitle(f'Even Secondary Values, Skewed Stat Distribution (Slot: {slot})')).save(f'{slot}_skewed_stats.png')

    (build_eval_plot(systems,
                    [1, 0.8, 0.6, 0.2],
                    470, [0.25, 0.25, 0.25, 0.25],
                     slot) + ggtitle(f'Skewed Secondary Values, Even Stat Distribution (Slot: {slot})')).save(f'{slot}_skewed_secondaries.png')

    (build_eval_plot(systems,
                    [1, 0.8, 0.6, 0.2],
                    470, [0.35, 0.3, 0.2, 0.15],
                     slot) + ggtitle(f'Skewed Secondary Values, Skewed Stat Distribution (Slot: {slot})')).save(f'{slot}_skewed_both.png')
