import os

from fastapi import APIRouter


router = APIRouter(prefix="", tags=["sample"])


@router.get("/sample/{sample_name}")
def sample(sample_name: str):
    return f"Hello, {sample_name}"
