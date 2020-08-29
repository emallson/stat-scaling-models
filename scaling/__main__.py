#!/usr/bin/env python3
from scaling.plotting import build_eval_plot, plot_should_you_equip
from scaling.constants import SCALARS
from scaling import bfa, legion
from plotnine import ggtitle
import os

ilvls = [385, 415, 445, 475]
penalties = [-30, -15, 0, 15, 30]
systems = {
    'Shadowlands': [bfa, 1],
    'BFA': [bfa, 0],
    'Legion': [legion, 0],
}

slot_names = {
    'main': 'A Chestpiece',
    'off': 'Some Boots',
    'bracers': 'Some Bracers',
    'ring': 'A Ring'
}

title_format = '{} just dropped! Should You Equip It?\n\n{}'

for slot in SCALARS.keys():
    (build_eval_plot(systems, ilvls,
                     plot_should_you_equip,
                    [1, 1, 1, 1],
                    [0.25, 0.25, 0.25, 0.25],
                     slot,
                     penalties) + ggtitle(title_format.format(slot_names[slot],
                                                              'Your gear has balanced stats, and each stat is equally valuable.'))).save(f'results/{slot}_even.png')

    (build_eval_plot(systems, ilvls,
                     plot_should_you_equip,
                    [1, 1, 1, 1],
                    [0.35, 0.3, 0.2, 0.15],
                     slot,
                     penalties) + ggtitle(title_format.format(slot_names[slot],
                                                              'Your gear is skewed towards Crit/Haste, but each stat is equally valuable.'))).save(f'results/{slot}_skewed_stats.png')

    (build_eval_plot(systems, ilvls,
                     plot_should_you_equip,
                    [1, 0.8, 0.6, 0.5],
                    [0.25, 0.25, 0.25, 0.25],
                     slot,
                     penalties) + ggtitle(title_format.format(slot_names[slot],
                                                              'Your gear has balanced stats, but Crit/Haste are worth more than Mastery/Vers.'))).save(f'results/{slot}_skewed_secondaries.png')

    (build_eval_plot(systems, ilvls,
                     plot_should_you_equip,
                    [1, 0.8, 0.6, 0.5],
                    [0.35, 0.3, 0.2, 0.15],
                     slot,
                     penalties) + ggtitle(title_format.format(slot_names[slot],
                                                              'Your gear is skewed towards Crit/Haste, and Crit/Haste are worth more than Mastery/Vers.'))).save(f'results/{slot}_skewed_both.png')

    (build_eval_plot(systems, ilvls,
                     plot_should_you_equip,
                    [1, 0.9, 0.8, 0.6],
                    [0.25, 0.25, 0.25, 0.25],
                     slot,
                     penalties) + ggtitle(title_format.format(slot_names[slot],
                                                              'Your gear has balanced stats, but Crit/Haste are worth *slightly* more than Mastery/Vers.'))).save(f'results/{slot}_skewed-slight_secondaries.png')

    (build_eval_plot(systems, ilvls,
                     plot_should_you_equip,
                    [1, 0.9, 0.8, 0.6],
                    [0.35, 0.3, 0.2, 0.15],
                     slot,
                     penalties) + ggtitle(title_format.format(slot_names[slot],
                                                              'Your gear is skewed towards Crit/Haste, and Crit/Haste are worth *slightly* more than Mastery/Vers.'))).save(f'results/{slot}_skewed-slight_both.png')

    (build_eval_plot(systems, ilvls,
                     plot_should_you_equip,
                    [1, 0.9, 0.8, 0.6],
                    [0.35, 0.3, 0.2, 0.15],
                     slot,
                     [-10, -5, 0, 5, 10]) + ggtitle(title_format.format(slot_names[slot],
                                                              'Your gear is skewed towards Crit/Haste, and Crit/Haste are worth *slightly* more than Mastery/Vers.'))).save(f'results/{slot}_skewed-slight_both_reduced-penalty.png')
