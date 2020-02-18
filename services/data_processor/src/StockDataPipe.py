import yfinance as yf
import pandas as pd
import plotly.express as px


# Wrapper to get a dataframe for the financial history of a company
def create_stock_data(company: str, period: str = "1y", interval: str = "1d") -> pd.DataFrame:
    return yf.Ticker(company).history(period, interval).T.transpose()


if __name__ == "__main__":
    # Fetches financial data from Tesla's stock price each day in the last year.
    # The .T fetches the dataframe for the data and transposing it makes it easier
    # to work with as that way you can have named columns
    tsla = yf.Ticker("TSLA").history(period="1y", interval="1d").T.transpose()

    # This creates the graph where the x axis is the datetime of the graph and the y
    # axis is the data from the open column
    fig = px.line(tsla, x=tsla.index, y="Open")

    # Show the data
    fig.show()