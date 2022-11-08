from fastapi import APIRouter

from wfse.app.database import conn

router = APIRouter()


@router.get('/')
async def fortune_index():
    return {'message': 'here is fortune'}


@router.get('/checking')
async def fortune_checking():
    return {'message': 'here is fortune checking'}


@router.get('/result')
async def fortune_result():
    return {'message': 'here is fortune result'}

