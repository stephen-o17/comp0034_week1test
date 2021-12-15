# COMP0034: Code for activities in week 1

### Introduction

There are many ways you could use your programming skills to recreate some of these now famous charts. This term we will
learn techniques for doing this in Python using the Plotly chart libraries. There are lots of libraries or packages we
could use for data visualisation, each with their own strengths, for this first chart we are going to
use [Plotly Express](https://plotly.com/python/plotly-express/). Plotly Express includes access to a number of datasets,
including the data that Hans Rosling used in his talk.

### Create a bubble chart

Recreate the 'Life Expectancy v. Per Capita GDP, 2007' bubble chart using the gapminder data.

A bubble chart is a scatter plot in which a third dimension of the data is shown through the size of markers.

Open the file [code_examples/gapminder_charts.py](code_examples/gapminder_charts.py). Read through the code and then run
it. You should see the chart in a browser.

> **Challenge**: Change the chart to display the data for 1987. You will need to run the code again after you make your changes.

### Improve the chart appearance

With just a few lines of code we created a pretty reasonable chart. When we created the chart you may have noticed we
added a number of attributes such as `x="gdpPercap"` to specify the data column for the x-axis and `colour="continent"`
to specify how to apply colours to the bubbles. The attributes and options are all defined in
the [Plotly Express documentation](https://plotly.com/python-api-reference/generated/plotly.express.scatter.html#plotly.express.scatter)
.

Try and improve the appearance of the chart by adding a title and using more meaningful descriptions for the axes.

Add the code below to the `create_bubble_chart` function and re-run the code.

```python
# Add a title and change the x-axis name
fig.update_layout(
    title='Life Expectancy v. Per Capita GDP, 2007',
    xaxis=dict(
        title='GDP per capita',
    ),
)
```

> **Challenge** Modify the y-axis title to display as 'Life Expectancy (years)'

Have a go in the cell below.

### Animate the chart

Plotly Express provides the ability to animate the bubble chart using attributes for `animation_frame`
and `animation_group`.

Modify the scatter code to add animation, e.g.

```python
fig = px.scatter(df,
                 x="gdpPercap",
                 y="lifeExp",
                 animation_frame="year",
                 animation_group="country",
                 size="pop",
                 color="continent",
                 hover_name="country",
                 log_x=True,
                 size_max=60,
                 )
```

Re-run the code. Be patient, this chart will take a few minutes to display. Once the chart is displayed, press the play
button under the chart to start the animation.

### Challenges
There are no example solutions to these. These are challenges for you to try.
#### Can you create an animated map instead of a bubble chart of the Gapminder data?

Check out this [blog post on Medium](https://medium.com/plotly/introducing-plotly-express-808df010143d) and scroll down
the page to find guidance for creating an animated map.

#### Can you create an animated bubble chart using a different dataset?

There are many sources of datasets, [Plotly provides a number here](https://plotly.github.io/datasets/).

You could also head over to the [Gapminder website](https://www.gapminder.org/data/) and see what other data sets they
make available.

Remember that using pandas DataFrame you can read from a URL or a local file.

If the file is accessible via a URL then you can provide that as the location, for example the following reads a csv
file from the URL https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv:

```python
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')
```

To read from a file located in this project directory:

```python
import pandas as pd

df = pd.read_csv('data/math_achievement_8th_grade.csv')
```

The above both use code that reads a comma-separated variable (csv) format file. Pandas has read functions for other
formats which you can find in
the [Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/io.html).

## Acknowledgements

The introductory video is a TED talk given by Hans Rosling
called ['The best stats you have ever seen'](https://www.ted.com/talks/hans_rosling_the_best_stats_you_ve_ever_seen?utm_campaign=tedspread&utm_medium=referral&utm_source=tedcomshare)
.

The code examples make use of the [Plotly Express](https://plotly.com/python/plotly-express/) library. This library
provides direct access to the Gapminder data set. There are also examples for the use of the Gapminder data in their
help and documentation.

The Gapminder data can also be accessed freely at [Gapminder.org](https://www.gapminder.org/data/). The '
math_achievement_8th_grade.csv' file in this repository was downloaded from Gapminder.

## Feedback and corrections to files in this repository

Please report suggestions or errors
at [https://github.com/nicholsons/comp0034_week1/issues](https://github.com/nicholsons/comp0034_week1/issues).
