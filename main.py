from datetime import datetime, time, timedelta
from fastapi import Body, FastAPI, Query
from uuid import UUID


app = FastAPI()


@app.put('/dogs/{dog_id}')
async def update_dog(
    *,
    dog_id: UUID,
    dog_name: str = Query(..., min_length=2, max_length=20),
    start_datetime: datetime = Body(None),
    end_datetime: datetime = Body(None),
    repeat_at: time = Body(None),
    process_after: timedelta = Body(None),
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "dog_id": dog_id,
        "dog_name": dog_name,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }
