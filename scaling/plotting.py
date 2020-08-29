from plotnine import ggplot, aes, geom_bar, facet_grid, theme_538, xlab, ylab, geom_hline, geom_bin2d, theme, scale_x_discrete
from scaling.eval import evaluate_point
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


def build_eval_plot(systems, ilvls, plotter, *args):
    results = []
    for ilvl in ilvls:
        for name, system in systems.items():
            res = evaluate_point(*system, ilvl, *args)
            res['system'] = name
            res['ilvl'] = ilvl
            results += [res]
    results = pd.concat(results)
    return plotter(results)
