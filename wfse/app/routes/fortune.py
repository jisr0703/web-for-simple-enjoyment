import random
from fastapi import APIRouter, Depends
from starlette.responses import Response, JSONResponse
from sqlalchemy.orm import Session

from wfse.app.models import Feelings
from wfse.app.database.schema import IPs
from wfse.app.database.conn import db
router = APIRouter()


@router.get('/')
async def fortune_index():
    return {'message': 'here is fortune'}


@router.get('/checking')
async def fortune_checking():
    return {'hi': 'here is fortune checking'}


@router.get('/result/{ip}', status_code=201)
async def fortune_result(ip: str, session: Session = Depends(db.session)):
    new_ip = IPs.create(session, auto_commit=False, ip=ip)
    feel = random.choices(range(1, 4), weights=[6.8, 1.2, 2.0])[0]
    for f in Feelings:
        if f.value == feel:
            return dict(Feeling=f'{feel}, {new_ip.id}')

    return JSONResponse(status_code=400, content=dict(msg="INVALID_REQUEST"))


