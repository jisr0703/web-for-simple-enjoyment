import random
from fastapi import APIRouter, Depends
from starlette.responses import Response, JSONResponse
from sqlalchemy.orm import Session

from wfse.app.models import Feeling
from wfse.app.database.schema import IPs, Feelings, FeelingsLog
from wfse.app.database.conn import db
router = APIRouter()


@router.get('/')
async def fortune_index():
    return {'message': 'here is fortune'}


@router.get('/checking')
async def fortune_checking():
    return {'hi': 'here is fortune checking'}


@router.get('/checking/test/{feeling_id}')
async def fortune_checking(feeling_id: Feeling):
    print(feeling_id)
    feeling = Feelings().get(id=feeling_id.Happiness)
    print(feeling)
    return dict(id=f'{feeling.id}', feeling=f'{feeling.feeling}')


@router.get('/result/{ip}', status_code=201)
async def fortune_result(ip: str, session: Session = Depends(db.session)):
    ip_row = IPs.get(ip=ip)
    if ip_row is None:
        ip_row = IPs.create(session, auto_commit=True, ip=ip)
    feelings_res_row = FeelingsLog.get(ip_id=ip_row.id)
    if feelings_res_row is None:
        feel = random.choices(range(1, 4), weights=[6.8, 1.2, 2.0])[0]
        feelings_res_row = FeelingsLog.create(session, auto_commit=True, ip_id=ip_row.id, feeling_id=feel)
        if is_feeling_exist(feel):
            return dict(feeling=f'feeling_id: {feelings_res_row.feeling_id}', exist=False)
    if is_feeling_exist(feelings_res_row.feeling_id):
        return dict(feeling=f'feeling_id: {feelings_res_row.feeling_id}', exist=True)
    return JSONResponse(status_code=400, content=dict(msg="INVALID_REQUEST"))


def is_feeling_exist(feeling: int) -> bool:
    for f in Feeling:
        if f.value == feeling:
            return True
    return False
