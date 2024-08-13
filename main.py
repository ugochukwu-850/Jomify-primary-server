from fastapi import Body, FastAPI
from fastapi.responses import JSONResponse
from fastapi import status
from models.release import Release, Target
from packaging import version
app = FastAPI()


@app.get("/")
async def root():
    return {"message": "This would eventually be the renderer for the home page or landing page ."}

@app.get("/release/{target}/{arch}/{current_version}")
def get_release(target: str, arch: str, current_version: str) -> JSONResponse:
    """
    This route is supposed to handle  auto update requests from ever Jomify Client
    """
    latest_release_meta : Release = Release.new()
    # check that a version update is even needed by checking the current version 
    if version.parse(current_version) >= version.parse(latest_release_meta.version):
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content={"message": "No update it required"})
    if not target.lower() in ["windows", "linux", "macOs"]:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "You are not using a supported client"})

    try:
        meta = latest_release_meta.platforms[f"{target.lower()}-{arch}"]
        release_response_data = {
            "version": latest_release_meta.version,
            "pub_date": str(latest_release_meta.publish_date),
            "url": meta.url,
            "signature": meta.signature,
            "notes": latest_release_meta.notes
            }
        # print(meta)
        return JSONResponse(status_code=status.HTTP_200_OK, content=release_response_data)
    except KeyError:
        return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST, content={"message": "You are not using a supported client architecture"})

@app.post("/release")
async def release(release: Release = Body(...)):
    # saves the release to the mongo db
    release.model_dump()
    
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "successfully created a new release"})