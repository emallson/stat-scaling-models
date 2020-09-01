from plotnine import ggplot, aes, geom_bar, facet_grid, theme_538, xlab, ylab, geom_hline, geom_bin2d, theme, scale_x_discrete, geom_line, facet_wrap
from scaling.eval import evaluate_point
import numpy as np
import pandas as pd


def plot_eval(eval_results):
    eval_results['penalty'] = pd.Categorical(eval_results['penalty'],
                                             categories=[-5, 0, 5])

    def diff(df):
        df['delta'] = df['delta'] - df[df['setting'] == 'basic']['delta'].values[0]
        return df

    eval_results_grouped = eval_results.groupby(['system', 'ilvl']).apply(diff).reset_index()
    eval_results_grouped = eval_results_grouped[eval_results_grouped['setting'] != 'basic']
    eval_results_grouped['setting'] = pd.Categorical(eval_results_grouped['setting'],
                                                     categories=['even',
                                                                 'semi-skewed',
                                                                 'skewed',
                                                                 'extreme'])

    hline_data = eval_results.loc[eval_results['setting'] == 'basic']
    hline_data['kind'] = 'worst'
    hline_data2 = hline_data.copy()
    hline_data2['kind'] = 'best'

    hline_data = pd.concat([hline_data, hline_data2])

    return ggplot(eval_results_grouped,
                  aes('penalty', 'delta', fill='setting')) +\
        geom_bar(stat='identity', position='dodge') +\
        geom_hline(hline_data, aes(yintercept='-delta'), linetype='dotted') +\
        facet_grid("system ~ ilvl + kind", scales='free_y') + theme_538() +\
        xlab('ilvl Relative to Current Gear') +\
        ylab('Avg Damage Relative to +5 ilvl Upgrade')

def plot_improvement(eval_results):
    eval_results['penalty'] = pd.Categorical(eval_results['penalty'],
                                             categories=[-5, 0, 5])
    eval_results['ilvl'] = pd.Categorical(eval_results['ilvl'], categories=eval_results['ilvl'].unique())

    eval_results['Upgrade?'] = 'Worse than ilvl Upgrade'
    eval_results.loc[eval_results['delta'] < 0, 'Upgrade?'] = 'Worse than Equipped'

    def diff(df):
        df['delta'] = df['delta'] - df[df['setting'] == 'basic']['delta'].values[0]
        return df

    eval_results_grouped = eval_results.groupby(['system', 'ilvl']).apply(diff).reset_index()
    eval_results_grouped.loc[eval_results_grouped['delta'] > 0, 'Upgrade?'] = 'Better than ilvl Upgrade'
    eval_results_grouped = eval_results_grouped[eval_results_grouped['setting'] != 'basic']
    eval_results_grouped['setting'] = pd.Categorical(eval_results_grouped['setting'],
                                                     categories=['even',
                                                                 'semi-skewed',
                                                                 'skewed',
                                                                 'extreme'])

    eval_results_grouped['Upgrade?'] = pd.Categorical(eval_results_grouped['Upgrade?'],
                                                      categories=[
                                                          'Worse than Equipped',
                                                          'Worse than ilvl Upgrade',
                                                          'Better than ilvl Upgrade'
                                                      ])

    eval_results_grouped['kind'].replace({'best': 'Best Stats',
                                          'worst': 'Worst Stats'},
                                         inplace=True)

    eval_results_grouped['setting'].replace({'even': '50 / 50',
                                             'semi-skewed': '60 / 40',
                                             'skewed': '80 / 20',
                                             'extreme': '100 / 0'},
                                            inplace=True)

    eval_results_grouped['setting'] = pd.Categorical(eval_results_grouped['setting'],
                                                     categories=['50 / 50',
                                                                 '60 / 40',
                                                                 '80 / 20',
                                                                 '100 / 0'])


    return ggplot(eval_results_grouped,
                  aes('penalty', 'ilvl', fill='Upgrade?')) +\
        geom_bin2d(color='black') +\
        facet_grid("system ~ kind + setting", scales='free_y') + theme_538() +\
        xlab('ilvl Relative to Equipped Gear') +\
        ylab('ilvl of Equipped Gear') +\
        theme(figure_size=(8.5, 5))


def plot_should_you_equip(eval_results):
    eval_results['penalty'] = pd.Categorical(eval_results['penalty'],
                                             categories=sorted(eval_results['penalty'].unique()))
    eval_results['ilvl'] = pd.Categorical(eval_results['ilvl'],
                                          categories=eval_results['ilvl'].unique())

    eval_results['Equip?'] = 'No'
    eval_results.loc[eval_results['delta'] > 0, 'Equip?'] = 'Yes'

    eval_results = eval_results[eval_results['setting'] != 'basic']

    eval_results['Equip?'] = pd.Categorical(eval_results['Equip?'],
                                            categories=[
                                                'No',
                                                'Yes',
                                            ])

    eval_results['kind'].replace({'best': 'Best Stats',
                                  'worst': 'Worst Stats'},
                                 inplace=True)

    eval_results['setting'].replace({'even': '50 / 50',
                                     'semi-skewed': '60 / 40',
                                     'skewed': '80 / 20',
                                     'extreme': '100 / 0'},
                                    inplace=True)

    eval_results['setting'] = pd.Categorical(eval_results['setting'],
                                             categories=['50 / 50',
                                                         '60 / 40',
                                                         '80 / 20',
                                                         '100 / 0'])

    eval_results['system'] = pd.Categorical(eval_results['system'],
                                            categories=['Legion', 'BFA', 'Shadowlands'])

    return ggplot(eval_results,
                  aes('penalty', 'ilvl', fill='Equip?')) +\
        geom_bin2d(color='black') +\
        facet_grid("system ~ kind + setting", scales='free_y') + theme_538() +\
        scale_x_discrete(name='Relative ilvl of Drop', labels=lambda xs: ['{:+d}'.format(x) for x in xs]) +\
        ylab('ilvl of Equipped Gear') +\
        theme(figure_size=(14, 5))


def build_eval_plot(systems, plotter, *args):
    results = []
    for name, system in systems.items():
        for ilvl in system[0].ILVLS:
            res = evaluate_point(*system, ilvl, *args)
            res['system'] = name
            res['ilvl'] = ilvl
            results += [res]
    results = pd.concat(results)
    return plotter(results)


def plot_jewelry_points(systems):
    dfs = []
    for name, system in systems.items():
        ilvls = np.arange(system.ILVLS[0], system.ILVLS[-1])
        points = [system.points('jewelry', ilvl, [1, 0, 0, 0], 1)[1][0] for ilvl in ilvls]

        df = pd.Series(ilvls, name='ilvls').to_frame()
        df['points'] = points
        df['points'] = df['points'] / df['points'].min()
        df['model'] = name
        dfs.append(df)

    df = pd.concat(dfs)
    return ggplot(df, aes('ilvls', 'points')) + geom_line() + facet_wrap('~ model', scales='free_x') + xlab('ilvl') + ylab('Secondary Rating Relative to First Tier')


def plot_jewelry_rand_prop(systems):
    def scale_reference(points, base, ilvl):
        gap = ilvl - base
        return points[base - 1] * 1.15 ** (gap / 15)

    dfs = []
    for name, system in systems.items():
        ilvls = np.arange(system.ILVLS[0], system.ILVLS[-1])
        points = [system.RAND_PROP_POINTS[ilvl-1] for ilvl in ilvls]

        ref = [scale_reference(system.RAND_PROP_POINTS, ilvls[0], ilvl) for ilvl in ilvls]

        df = pd.Series(ilvls, name='ilvls').to_frame()
        df['points'] = points
        df['points'] = df['points'] / df['points'].min()
        df['ref'] = ref
        df['ref'] = df['ref'] / df['ref'].min()
        df['model'] = name
        dfs.append(df)

    df = pd.concat(dfs)
    return ggplot(df, aes('ilvls', 'points')) + geom_line() + geom_line(aes(y='ref'), color='red') + facet_wrap('~ model', scales='free_x') + xlab('ilvl') + ylab('Random Property Points Relative to First Tier')
