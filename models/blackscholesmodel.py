class BlackScholesModel:

    def __init__(
            self,
            spot,    # current security price
            rate,    # current risk-free interest rate
            sigma,   # current volatility
            div = 0, # optional dividend yield 
            ):
        
        if spot <= 0:
            raise ValueError("Invalid Spot: spot price must be > 0")
        if sigma <= 0:
            raise ValueError("Invalid Volatility: sigma must be > 0 ")
        if div < 0:
            raise ValueError("Invalid Dividend Yield: div must be >= 0")
        
        self.spot = spot
        self.rate = rate
        self.sigma = sigma
        self.div = div

        

        
        


        
        

    

