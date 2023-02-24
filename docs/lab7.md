---
layout: spec
title: Lab 7
sitemapOrder: 20
---

Lab 7
==========================
{: .primer-spec-toc-ignore }


## Task
For this lab, you'll explore data visualization in Python using the MatPlotLib library, which provides an easy way to graph data. As practice, you'll graph the results of a few trials from a reinforcement learning model I trained last year. Download these here (use `wget` in your terminal or `Right Click > Save As...` in your browser): [trial1.csv](https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/trial1.csv), [trial2.csv](https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/trial2.csv), and [trial3.csv](https://raw.githubusercontent.com/eecs298/eecs298.github.io/main/trial3.csv).

Each trial spanned 24900 timesteps, reporting the episode reward (`ep_rew`) itermittently at a set rate. The episode reward represents the model's proficiency at its task, and increases steadily throughout training. Your graph will place the timestep (the independent variable) on the X-axis and `ep_rew` (the dependent variable) on the Y-axis.

For each timestep, use Numpy to calculate the mean of the `ep_rew` value for each trial at that timestep and plot this curve. For example, at timestep `2800`, the three trials report `5.996785128`, `4.282292699`, and `5.123866481`, respectively. The average of these three is `5.134314769`, so you will plot the point (`2800`, `5.134314769`).

In addition to the mean, Numpy to calculate the standard deviation between the three `ep_rew` values for each trial at a given timestep. Then plot two additional curves: one standard deviation above the mean and one standard deviation below the mean. The standard deviation of `5.996785128`, `4.282292699`, and `5.123866481` is `0.699977593`, so for timestep `2800` you should plot the points (`2800`, `5.134314769 + 0.699977593`) and (`2800`, `5.134314769 - 0.699977593`). Finally, shade in the area between these two curves. Plotting our data in this way helps to visualize the stability of the model throughout training. 

Color these lines with your favorite color and give appropriate labels to the X- and Y-axes. Set the title of the graph to your uniqname and save it. Submit your plotting code and your final graph. Feel free to get creative with the presenation of your graph!

Your final graph should look something like this:

![Final graph](lab7.png)

## Tips
### Plotting a graph
```python
import matplotlib.pyplot # Import the library

# Data to graph
x = [1, 2, 3, 4, 5] 
y = [5, 10, 15, 20, 25]

matplotlib.pyplot.plot(x, y) # Create a graph
# Maps data pairs to x-y coordinates 
# graph will include the points (1, 5), (2, 10), and so on

# Once a graph is created, you have a few options:
matplotlib.pyplot.show() # Open the graph in a pop-up window
matplotlib.pyplot.savefig(filepath) # Save the figure to the specified filepath
```

### Advanced plotting
```python
# Data to graph
x = [1, 2, 3, 4, 5] 
top_line = [0, 5, 10, 15, 20]
bottom_line = [10, 15, 20, 25, 30]

# Shade in the area between the top and bottom line:
matplotlib.pyplot.fill_between(x, bottom_line, top_line, alpha=0.2)
# Alpha is an optional argument between 0 and 1 denoting opacity
```

### Customizing your graph
Find the list of all available colors [here](https://matplotlib.org/stable/gallery/color/named_colors.html).
```python
# Specify the color for your line
matplotlib.pyplot.plot(x1, y1, color="tab:blue") 

# Can plot multiple lines per graph
matplotlib.pyplot.plot(x2, y2, color="tab:green") 

# Label your axes as follows:
plt.xlabel('Name of X-axis') 
plt.ylabel('Name of Y-axis') 
  
# Display a title on the graph:
plt.title("Title of graph")
```

### Numpy functions
```python
# The numpy mean function returns the average of a list:
mean_of_list = numpy.mean(list1)
mean_of_some_numbers = numpy.mean([var1, var2, var3])

# likewise, the numpy std function returns the standard deviation of a list:
std_dev = numpy.std(list1)
```