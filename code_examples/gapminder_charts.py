import plotly.express as px


def gapminder_bubble_chart(df):
    """
    Takes the gapminder data, creates a figure that is a scatter plot and displays it in a
    browser.
    :parameter data: the gapminder data set
    :type data: DataFrame
    :return: None
    """
    data_2007 = df.query("year==2007")
    fig = px.scatter(data_2007,
                     x="gdpPercap",
                     y="lifeExp",
                     size="pop",
                     color="continent",
                     hover_name="country",
                     log_x=True,
                     size_max=60)

    fig.show()


if __name__ == '__main__':
    gapminder_df = px.data.gapminder()
    print(gapminder_df.info(verbose=True))
    gapminder_bubble_chart(gapminder_df)


