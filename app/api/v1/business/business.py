import logging
from fastapi import APIRouter
from app.cf_db.cf_db import ProjectDatabase
from app.schemas.base import Success



logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/test", summary="测试API")
async def test_api():
    return {"message": "Hello, World!"}

@router.get("/projects", summary="获取完整项目列表")
async def get_all_projects():
    db = ProjectDatabase()
    projects = db.list_all_projects()
    return Success(data=projects)

@router.get("/project/{uuid}", summary="获取项目详情")
async def get_project_details(uuid: str):
    db = ProjectDatabase()
    project = db.get_project_by_uuid(uuid)
    return Success(data=project)