from fastapi import APIRouter

router = APIRouter(tags=["tasks"])


@router.get("/tasks")
async def retrieve_tasks_list():
    return []
