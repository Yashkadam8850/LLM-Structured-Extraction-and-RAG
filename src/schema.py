from enum import Enum
from pydantic import BaseModel

class Category (str,Enum):
    DELIVERY = "Delivery"
    PRODUCT = "Product"
    REFUND = "Refund"
    PAYMENT =  "Payment"
    CUSTOMER_SUPPORT = "Customer_Support"
    APP = "App"

class Urgency(str,Enum):
    LOW="Low"
    MEDIUM="Medium"
    HIGHT="High"

class Sentiment(str,Enum):
    POSITIVE="Positive"
    NEUTRAL="Neutral"
    NEGATIVE="Negative"

class ReviewSchema(BaseModel):
    category:Category
    urgency:Urgency
    sentiment:Sentiment
    summary: str




    