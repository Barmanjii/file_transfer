# Python Import
import os

# FastAPI Import
from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter(prefix="/file_transfer", tags=["File Transfer"])
# local_path = "/peppermint_ws/install/robot_params/share/robot_params/maps" # For Robot
local_path = "/home/barmanji/SD0452026/deployment"  # For local testing


@router.get("/")
def test(folder_name: str, file_name: str):
    try:
        check_deployement = _exist(path=local_path)
        if check_deployement is not None:
            full_path = local_path + "/" + folder_name
            find = _exist(full_path)
            if find is not None:
                file_path = full_path + "/" + file_name
                file_check = _exist(file_path)
                if file_check is not None:
                    headers = {
                        "Content-Disposition": f"attachment; filename={file_path}",
                        "Content-Type": "application/octet-stream",
                    }
                return FileResponse(file_path, headers=headers)
            else:
                return "Not found!!"
        else:
            return "Doesn't Exist"
    except Exception as e:
        return str(e)


def _exist(path):
    try:
        if os.path.exists(path):
            return "found"
        else:
            return "File not found!!!"
    except Exception as e:
        return f"Doesn't Exist {str(e)}"
