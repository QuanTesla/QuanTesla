import yfinance as yf
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# Wrapper to get a dataframe for the financial history of a company
def create_stock_data(company: str, period: str = "1y", interval: str = "1d") -> pd.DataFrame:
    return yf.Ticker(company).history(period, interval).T.transpose()


# Wrapper to create a candlestick graph
def create_candlestick_graph(stock_data: pd.DataFrame) -> go.Figure:
    return go.Figure(data=[go.Candlestick(
        x=stock_data.index,
        open=stock_data.Open,
        low=stock_data.Low,
        high=stock_data.High,
        close=stock_data.Close
        )])


if __name__ == "__main__":
    # Fetches financial data from Tesla's stock price each day in the last year.
    # The .T fetches the dataframe for the data and transposing it makes it easier
    # to work with as that way you can have named columns
    tsla = create_stock_data(company="TSLA", period="1y", interval="1d")

    # This creates the graph where the x axis is the datetime of the graph and the y
    # axis is the data from the open column
    fig = create_candlestick_graph(tsla)
    fig.update_layout(template="plotly_dark")

    # Show the data
    fig.show()