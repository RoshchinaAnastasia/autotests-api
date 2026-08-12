import uuid
from pydantic import BaseModel, Field, ConfigDict, computed_field, HttpUrl, EmailStr
from pydantic.alias_generators import to_camel

class FileShema(BaseModel):
    id: str
    url: HttpUrl
    filename: str
    directory: str

class UserSchema(BaseModel):
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

    @computed_field
    def username(self)-> str:
        return f"{self.first_name} {self.last_name}"


    def get_user_name(self)-> str:
        return f"{self.first_name} {self.last_name}"

class CourseSchema(BaseModel):
    model_config = ConfigDict(alias_generator=to_camel, populate_default=True)

    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    title: str = "Playwright"
    max_score: int = Field(alias="maxScore", default=1000)
    min_score: int = Field(alias="minScore", default=100)
    description: str = "Playwright"
    preview_file: FileShema = Field(alias="previewFile")
    estimated_time: str = Field(alias="estimatedTime", default="2 weeks")
    created_by_user: UserSchema = Field(alias="createdByUser")

course_default_model = CourseSchema(
    id="course_id",
    title="Playwright",
    maxScore=100,
    minScore=10,
    description="Playwright",
    previewFile=FileShema(
        id="preview_file_id",
        url="https://example.com/",
        filename="file.png",
        directory="courses"
    ),
    estimatedTime="1 week",
    createdByUser=UserSchema(
        id="created_by_user_id",
        email="user@example.com",
        lastName="Wick",
        firstName="John",
        middleName="Boogyman"
    )
)

print("Course default model: ", course_default_model)

course_dict = {
    "id": "course_id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile": {
        "id": "preview_file_id",
        "url": "https://example.com/",
        "filename": "file.png",
        "directory": "courses"
    },
    "estimatedTime": "1 week",
    "createdByUser": {
        "id": "created_by_user_id",
        "email": "user@example.com",
        "lastName": "Wick",
        "firstName": "John",
        "middleName": "Boogyman"
    }
}

course_dict_model = CourseSchema(**course_dict)
print("Course dict model: ", course_dict_model)

course_json ="""
{
    "id": "course_id",
    "title": "Playwright",
    "maxScore": 100,
    "minScore": 10,
    "description": "Playwright",
    "previewFile": {
        "id": "preview_file_id",
        "url": "https://example.com/",
        "filename": "file.png",
        "directory": "courses"},
    "estimatedTime": "1 week",
    "createdByUser": {
    "id": "created_by_user_id",
    "email": "user@example.com",
    "lastName": "Wick",
    "firstName": "John",
    "middleName": "Boogyman"}
}
"""

course_json_model = CourseSchema.model_validate_json(course_json)
print("Course json model: ", course_json_model)
print(course_json_model.model_dump(by_alias=True))
print(course_json_model.model_dump_json(by_alias=True))


user = UserSchema(
    id="created_by_user_id",
    email="user@example.com",
    lastName="Wick",
    firstName="John",
    middleName="Boogyman"
)
print(user.get_user_name(), user.username)