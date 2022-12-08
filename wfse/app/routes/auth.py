from typing import Optional

from fastapi import APIRouter, Response, Request
from fastapi.responses import RedirectResponse
import requests

from wfse.app.common.consts import kakao


router = APIRouter()


@router.get('/kakao')
async def oauthInKakao():
    # kakaoAuthURL = f"https://kauth.kakao.com/oauth/authorize?client_id={kakao['CLIENT_ID']}&client_secret={kakao['CLIENT_SECRET']}&response_type=code&redirect_uri={kakao['REDIRECT_URI']}"
    kakaoAuthURL = f"https://kauth.kakao.com/oauth/authorize?client_id={kakao['CLIENT_ID']}&response_type=code&redirect_uri={kakao['REDIRECT_URI']}"
    print()
    print(kakaoAuthURL)
    response = RedirectResponse(url=kakaoAuthURL)
    return response


@router.get('/kakao/auth')
async def OauthURLInKakao(response: Response, code: Optional[str] = "NONE"):
    kakaoAuthURL = f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={kakao['CLIENT_ID']}&code={code}&redirect_uri={kakao['REDIRECT_URI']}&client_secret={kakao['CLIENT_SECRET']}"
    _response = requests.post(kakaoAuthURL)
    result = _response.json()
    response.set_cookie(key="kakao", value=str(result["access_token"]))
    return {"code": result}

# https://kauth.kakao.com/oauth/authorize?client_id=%s&redirect_uri=%s&response_type=code
# GET                    /oauth/authorize?client_id=${834309}&redirect_uri=${http://localhost:8000/oauth}&response_type=code HTTP/1.1


# CLIENT_ID = '834309'
# CLIENT_SECRET = 'LBp62OE9OjecHqPnTArIGUi1cHOFgWE9'
# REDIRECT_URI = 	'http://localhost:8000/oauth'