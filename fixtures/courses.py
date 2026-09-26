import pytest
from pydantic import BaseModel
from clients.courses.courses_client import CreateCourseRequestSchema, CreateCourseResponseSchema
from clients.courses.courses_client import CoursesClient, get_courses_client
from fixtures.users import UserFixture
from fixtures.files import FilesFixture

class CourseFixture(BaseModel):
    request: CreateCourseRequestSchema
    response: CreateCourseResponseSchema

@pytest.fixture
def courses_client(function_user: UserFixture) -> CoursesClient:
    return get_courses_client(function_user.authentication_user)

@pytest.fixture
def function_course(
        courses_client: CoursesClient,
        function_user: UserFixture,
        function_file: FilesFixture
) -> CourseFixture:
    request = CreateCourseRequestSchema()
    response = courses_client.create_course(request)
    return CourseFixture(response=response, request=request)
