# swarmplot_and_errorbar
Automatically draw seaborn.swarmplot and matplotlib.pyplot.errorbar on a single figure

## Usage
### swarmplot_and_errorbar.plot
Plot swarmplot and errorbar.
- *x*, *y*: str  
Names of the column of *data*
- *data*: pd.DataFrame  
Data to use
- *hue*: str (optional)  
Keyword *hue* to pass to ```seaborn.swarmplot```
- *ax*: (optional)  
Axis to plot on to. If None, new one will be created.
- *swarmplot_kwargs*: dictionary (optional)  
Other keywords to pass to ```seaborn.swarmplot```. Example: *order*, *palette*, *orient*  
Note: As dafault, keywords *dodge* and *alpha* are set as True and 0.7, respectively.
- *errorbar_kwargs*: dictionary (optional)
Other keywords to pass to ```matplotlib.pyplot.errorbar```. Example: *color*, *capsize*  
Note: As default, keywords *fmt*, *color*, *markersize*, and *capsize* are set as "_" (or "|", if *orient* in *swarmplot_kwargs* is "h"), "k", 10 and 10, respectively. Also, The size of errorbars are calculated as standard error (standard deviation devided by a square root of "the number of samples minus 1"). If *yerr* or *xerr* (depending on *orient* in *swarmplot_kwargs*) is given, errorbars are drawn using the given value.

### swarmplot_and_errorbar.show
Show the plotted figure (using ```matplotlib.pyplot.show```). Return None if called before plotting.

### swarmplot_and_errorbar.get_fig
Return the plotted figure. Return None if called before plotting.

### swarmplot_and_errorbar.get_ax
Return the plotted axis. Return None if called before plotting.

### swarmplot_and_errorbar.get_table
Return the table (pd.DataFrame) describing mean values, errors, and the number of samples in each category. Return None if called before plotting.

## Example
```python
import swarmplot_and_errorbar

import seaborn as sns
data = sns.load_dataset("tips")
```

```python
swarmplot_and_errorbar.plot(x = "time", y = "tip", data = data)
swarmplot_and_errorbar.show()
```
![e1](https://user-images.githubusercontent.com/87290343/126040310-840a844b-7ea5-46ba-8c73-0c0d383069f2.png)

```python
swarmplot_and_errorbar.get_result()
```
| | mean | error | n |
| ---: | ---: | ---: | ---: |
| Dinner | 3.102670 | 0.108261 | 176 |
| Lunch | 2.728088 | 0.146170 | 68 |

```python
swarmplot_and_errorbar.plot(x = "time", y = "tip", data = data, hue = "smoker")
swarmplot_and_errorbar.show()
```
![e2](https://user-images.githubusercontent.com/87290343/126040508-74ec4f7e-bcc3-465f-b0ce-126f07eb8b03.png)

Note: As in this example, sometimes the order of the labels or hues differs from the result returened by calling ```seaborn.swarmplot``` directly ("Yes" appears first). You can customize these orders by setting *order* and *hue_order* in the parameter *swarmplot_kwargs*.

```python
swarmplot_and_errorbar.plot(x = "tip", y = "time", data = data, hue = "sex", swarmplot_kwargs = {"orient": "h"}, errorbar_kwargs = {"color": "g"})
swarmplot_and_errorbar.show()
```
![e3](https://user-images.githubusercontent.com/87290343/126040868-9949131a-8f02-4210-adf9-fb4ebd14b010.png)

```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots(1, 2, figsize = (18, 6))

swarmplot_and_errorbar.plot(x = "time", y = "tip", data = data, hue = "smoker", ax = ax[0])
swarmplot_and_errorbar.plot(x = "time", y = "tip", data = data, hue = "sex", ax = ax[1])
fig.tight_layout()
fig.show()
```
![e4](https://user-images.githubusercontent.com/87290343/126041099-8422314c-e6f5-40aa-9f9d-b9f3af846ec3.png)

# Requirement
- matplotlib
- seaborn
- pandas
- numpy
