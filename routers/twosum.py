from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class TwoSum(BaseModel):
    nums: list[int]
    target: int

@router.post("/two-sum")
def solve(request: TwoSum):
        read_values = dict()

        nums = request.nums
        target = request.target
    
        position = 0
        for val in nums:
            remaining = target - val
            if remaining in read_values:
                return {"indices": [read_values[remaining], position]}    
            else:
                read_values[val] = position
            
            position += 1
      
        return {"indices": []}