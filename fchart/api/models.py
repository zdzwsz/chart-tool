from pydantic import BaseModel, Field
from typing import List, Literal, Optional, Union,Dict

class DataModel(BaseModel):
    title: str
    y:Union[Dict[str,List[float]],List[Dict[str,List[float]]]]
    x:Dict[str,List[Union[str,int,float]]]