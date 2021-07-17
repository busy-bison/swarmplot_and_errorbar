#!/usr/bin/env python3

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

class _Swarmplot_And_Errorbar:
    def __init__(self):
        self._fig = None
        self._ax = None
        self._result = None

    def _plot(self, x, y, data, hue = None, ax = None, swarmplot_kwargs = dict(), errorbar_kwargs = dict()):

        # delete multiple values (if any, values in dictionary are used)
        swarmplot_kwargs, x = _pop_if_exists(swarmplot_kwargs, x, "x")
        swarmplot_kwargs, y = _pop_if_exists(swarmplot_kwargs, y, "y")
        swarmplot_kwargs, data = _pop_if_exists(swarmplot_kwargs, data, "data")
        swarmplot_kwargs, hue = _pop_if_exists(swarmplot_kwargs, hue, "hue")
        swarmplot_kwargs, ax = _pop_if_exists(swarmplot_kwargs, ax, "ax")

        # raise error
        if ("x" in errorbar_kwargs) or ("y" in errorbar_kwargs):
            raise TypeError("'x' and 'y' must be given as strings, not in dictionary")
        if ("xerr" in errorbar_kwargs) and ("yerr" in errorbar_kwargs):
            raise TypeError("'xerr' and 'yerr' cannot be given together")

        # check the orientation of swarmplot
        swarmplot_kwargs_new = _set_dict_as_default(swarmplot_kwargs, ["dodge", "alpha"], [True, 0.7])
        if "orient" in swarmplot_kwargs_new.keys():
            orient = swarmplot_kwargs_new["orient"]
        else:
            orient = "v"
        if orient == "v":
            axis0, axis1 = x, y
        else:
            axis0, axis1 = y, x

        # set default parameters (if not given)
        if orient == "v":
            errorbar_kwargs_new = _set_dict_as_default(errorbar_kwargs, ["fmt", "color", "markersize", "capsize"], ["_", "k", 10, 10])
        else:
            errorbar_kwargs_new = _set_dict_as_default(errorbar_kwargs, ["fmt", "color", "markersize", "capsize"], ["|", "k", 10, 10])

        # set some parameters required for swarmplot
        if "order" in swarmplot_kwargs_new.keys():
            order = swarmplot_kwargs_new.pop("order")
        else:
            order = sorted(list(pd.unique(data[axis0])))
        if hue:
            if "hue_order" in swarmplot_kwargs_new.keys():
                hue_order = swarmplot_kwargs_new.pop("hue_order")
            else:
                hue_order = sorted(list(pd.unique(data[hue])))
        else:
            hue_order = None

        # get values, mean, and err
        if hue_order and swarmplot_kwargs_new["dodge"]:
            values = [np.array(data[(data[axis0] == o) & (data[hue] == ho)][axis1]) for o in order for ho in hue_order if ho in list(pd.unique(data[data[axis0] == o][hue]))]
        else:
            values = [np.array(data[(data[axis0] == o)][axis1]) for o in order]
        mean = [v.mean() for v in values]
        err = [v.std(ddof = 1) / (len(v) ** 0.5) for v in values]

        # overwrite err if given (xerr and yerr are not given together)
        errorbar_kwargs, err = _pop_if_exists(errorbar_kwargs, err, "yerr")
        errorbar_kwargs, err = _pop_if_exists(errorbar_kwargs, err, "xerr")

        # draw swarmplot
        if ax == None:
            _, ax = plt.subplots()
        sns.swarmplot(x = x, y = y, data = data, ax = ax,
                      order = order, hue = hue, hue_order = hue_order, **swarmplot_kwargs_new)

        # check the orientation of swarmplot and get the positions to add errorbars
        swarm_pos = _get_swarm_pos(ax = ax, orient = orient)

        # draw errorbars
        if orient == "v":
            ax.errorbar(x = swarm_pos, y = mean, yerr = err, **errorbar_kwargs_new)
        else:
            ax.errorbar(x = mean, y = swarm_pos, xerr = err, **errorbar_kwargs_new)

        # make result table
        if hue_order and swarmplot_kwargs_new["dodge"]:
            label_list = [f"{o}_{ho}" for o in order for ho in hue_order if ho in list(pd.unique(data[data[axis0] == o][hue]))]
        else:
            label_list = order
        result = pd.DataFrame(index = ["mean", "SE", "n"],
                              columns = label_list,
                              data = [mean, err, [int(len(v)) for v in values]])
        result = result.T
        result = result.astype({"n": "int"})

        # assign values to attributes
        self._fig = ax.figure
        self._ax = ax
        self._result = result

    def _get_fig(self):
        return self._fig

    def _get_ax(self):
        return self._ax

    def _get_result(self):
        return self._result

_sae = _Swarmplot_And_Errorbar()

def plot(x, y, data, hue = None, ax = None, swarmplot_kwargs = dict(), errorbar_kwargs = dict()):
    _sae._plot(x, y, data, hue = hue, ax = ax, swarmplot_kwargs = swarmplot_kwargs, errorbar_kwargs = errorbar_kwargs)

def show():
    fig = _sae._get_fig()
    fig.show()

def get_fig():
    return _sae._get_fig()

def get_ax():
    return _sae._get_ax()

def get_result():
    return _sae._get_result()

def _pop_if_exists(dic, value, key):
    if key in dic.keys():
        value = dic.pop(key)
    return dic, value

def _get_swarm_pos(ax, orient):

    swarm_pos = []
    c = ax.get_children()

    i = 0
    while True:
        if isinstance(c[i], matplotlib.collections.PathCollection):
            x, y = c[i].get_offsets().T
            if len(x) != 0:
                if orient == "v":
                    swarm_pos.append(x.mean())
                else:
                    swarm_pos.append(y.mean())
        else:
            break
        i += 1

    return swarm_pos

def _set_dict_as_default(dic, keys, values):

    for k, v in zip(keys, values):
        if k not in dic.keys():
            dic[k] = v

    return dic
