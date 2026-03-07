class EuropeanOption:

    def __init__(
            self, 
            option_type: str, 
            strike: float , 
            maturity: float 
            ):
        
        option_type = option_type.lower()

        if option_type not in ("call", "put") :
            raise ValueError("Invalid option_type input, valid inputs -> call/put")
        
        if strike <= 0:
            raise ValueError("Invalid strike input, valid input must be > 0")
        
        if maturity <= 0: 
            raise ValueError("Invalid maturity input, valid input must be > 0")
        
        
        self.option_type = option_type     # option type -- call or put 
        self.strike = strike               # strike price 
        self.maturity = maturity           # time to expiration, proportional annually, ex: 1.0 -> 1 yr

    def payoff(self,S: float): #S -> current stock price
        if self.option_type == 'call':
            return max(0 , S - self.strike)
        else:
            return max(0 , self.strike - S)
    

option = EuropeanOption("put", 100 , 1.0)
print(option.payoff(80))



        








    
    