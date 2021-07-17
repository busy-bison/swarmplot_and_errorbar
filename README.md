# swarmplot_and_errorbar
Automatically draw seaborn.swarmplot and matplotlib.pyplot.errorbar on a single

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
Note: As default, keywords *fmt*, *color*, *markersize*, and *capsize* are set as "_" (or "|", if *orient* in *swarmplot_kwargs* is "h"), "k", 10 and 10, respectively.

### swarmplot_and_errorbar.show
Show the plotted figure (using ```matplotlib.pyplot.show```). Return None if called before plotting.

### swarmplot_and_errorbar.get_fig
Return the plotted figure. Return None if called before plotting.

### swarmplot_and_errorbar.get_ax
Return the plotted axis. Return None if called before plotting.

### swarmplot_and_errorbar.get_table
Return the table describing mean values, standard errors, and the number of samples in each category. Return None if called before plotting.

## Example
```python
import swarmplot_and_errorbar

import seaborn as sns
data = sns.load_dataset("tips")
```

```
swarmplot_and_errorbar.plot(x = "time", y = "tip", data = data)
swarmplot_and_errorbar.show()
```
![e1](https://user-images.githubusercontent.com/87290343/126040310-840a844b-7ea5-46ba-8c73-0c0d383069f2.png)

```
swarmplot_and_errorbar.plot(x = "time", y = "tip", data = data, hue = "smoker")
swarmplot_and_errorbar.show()
```
![e2](https://user-images.githubusercontent.com/87290343/126040508-74ec4f7e-bcc3-465f-b0ce-126f07eb8b03.png)

# Requirement
- matplotlib
- seaborn
- pandas
- numpy
