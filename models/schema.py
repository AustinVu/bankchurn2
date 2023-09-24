from pydantic import BaseModel

# Type hint for attributes of a house
class ChurnInfo(BaseModel):
    CreditScore: int = 461
    Age: int = 25
    Tenure: int = 6
    Balance: int = 0
    NumOfProducts: float = 2
    EstimatedSalary: int = 15306.29
    BalanceSalaryRatio: int = 0
    TenureByAge: int = 0.24
    CreditScoreGivenAge: int = 18.44
    HasCrCard: float = 1
    IsActiveMember: float = 1

# Type hint for all the predictions of a house
class ChurnPrediction(BaseModel):
    Price: float
