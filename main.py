import pandas as pd
import numpy as np
import yfinance as yf


class RollSpreadCalculator:
    def __init__(self, ticket:str):
        self.ticket = ticket

    def download_from_yfinance(self, price_type = "Close") -> pd.DataFrame:
        df = yf.download(self.ticket, period="1mo", interval="1d")
        self.data =  df[[price_type]]
        return self.data.copy()
    
    def calculate_returns(self):
        if not hasattr(self, 'data'):
            self.download_from_yfinance()
        
        self.returns = np.log(self.data / 
                              self.data.shift(1)).dropna()
        
        return self.returns.copy()


    

if __name__ == "__main__":
    ticket = "MSFT"
    calculator = RollSpreadCalculator(ticket)
    df = calculator.download_from_yfinance()
    calculator.calculate_returns()
    print(df)
    print(calculator.returns)