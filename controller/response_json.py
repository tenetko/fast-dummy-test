from fastapi import Response
from fastapi.responses import FileResponse
from fastapi_utils.cbv import cbv
from fastapi_utils.inferring_router import InferringRouter

router = InferringRouter()


@cbv(router)
class JsonHandler:
    def __init__(self):
        pass

    @router.get("/{response_type}")
    def return_dummy_response_with_recheck_only(self, response_type):
        file_name = f"static/json/{response_type}.json"
        return self.read_file(file_name)

    def read_file(self, file_name):
        with open(file_name, "r") as res:
            return Response(
                content=res.read(),
                media_type="application/json",
                headers={},
                status_code=200,
            )
