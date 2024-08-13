from pydantic import BaseModel, Field
from datetime import datetime
from typing import Dict
class Target(BaseModel):
    signature : str = Field(...) 
    url : str = Field(...)

class Release(BaseModel):
    version : str = Field(...)
    notes  : str = Field(default=None)
    publish_date  : datetime = Field(default=datetime.now())
    platforms : Dict[str, Target] = Field(...)

    @classmethod
    def new(cls):
        data =  {
        "version": "1.0.0",
        "notes": "Initial release with several features.",
        "publish_data": "2024-08-13",
        "platforms": {
            "windows-x86_64": {
            "signature": "abcd1234signaturevalue",
            "url": "https://example.com/download/app-x86_64.zip",
            },
                    "macOS-x86_64": {
            "signature": "abcd1234signaturevalue",
            "url": "https://example.com/download/app-x86_64.dmg",
            },
            "macOS-arm64": {
            "signature": "efgh5678signaturevalue",
            "url": "https://example.com/download/app-arm64.dmg",
            },
            "linux-x86_64": {
            "signature": "ijkl9012signaturevalue",
            "url": "https://example.com/download/app-x86.zip",
            }
        }
        }

        return cls(**data)



        

