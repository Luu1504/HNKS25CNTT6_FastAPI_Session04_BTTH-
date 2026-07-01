from fastapi import FastAPI

app = FastAPI(title="API Quản lý Khóa học")

courses = [
    {
        "id": 1,
        "name": "Python Basic",
        "category": "backend",
        "price": 3000000,
        "mode": "online"
    },
    {
        "id": 2,
        "name": "Java Web",
        "category": "backend",
        "price": 5000000,
        "mode": "offline"
    },
    {
        "id": 3,
        "name": "Web Frontend",
        "category": "frontend",
        "price": 4000000,
        "mode": "online"
    }
]

@app.get("/courses")
def get_all_courses():
    return {
        "message": "Lấy danh sách khóa học thành công",
        "data": courses
    }

@app.get("/courses/search")
def search_courses(mode: str = None, category: str = None):
    result_courses = courses

    if mode is not None:
        result_courses = [course for course in result_courses if course["mode"].lower() == mode.lower()]

    if category is not None:
        result_courses = [course for course in result_courses if course["category"].lower() == category.lower()]

    return {
        "message": "Lọc khóa học thành công",
        "data": result_courses
    }

@app.get("/courses/{course_id}")
def get_course_detail(course_id: int):
    for course in courses:
        if course["id"] == course_id:
            return {
                "message": "Tìm thấy khóa học",
                "data": course
            }
    
    return {
        "message": "Không tìm thấy khóa học"
    }