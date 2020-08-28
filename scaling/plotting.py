from plotnine import *
from scaling.eval import evaluate_point
import pandas as pd


def plot_eval(eval_results):
    eval_results['penalty'] = pd.Categorical(eval_results['penalty'], categories=[-5, 0, 5])
    eval_results['setting'] = pd.Categorical(eval_results['setting'], categories=['basic', 'even', 'semi-skewed', 'skewed', 'extreme'])
    return ggplot(eval_results, aes('penalty', 'delta', fill='setting')) +\
        geom_bar(stat='identity', position='dodge') + facet_grid("system ~ kind", scales='free_y') + theme_538()


def build_eval_plot(systems, *args):
    results = []
    for name, system in systems.items():
        res = evaluate_point(*system, *args)
        res['system'] = name
        results += [res]
    results = pd.concat(results)
    return plot_eval(results)
