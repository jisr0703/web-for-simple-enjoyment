from fastapi import APIRouter

router = APIRouter()


@router.get('/')
async def index():
    return {'message': 'welcome to Web For Simple Enjoy'}
