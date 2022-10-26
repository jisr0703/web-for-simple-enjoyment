from fastapi import APIRouter

router = APIRouter()


@router.get('/')
async def fortune_index():
    return {'message': 'here is fortune'}


@router.get('/checking')
async def fortune_checking():
    return {'message': 'here is fortune checking'}