def test_insert_and_delete_and_update(session):
    from repository import TeacherTable
    repo = TeacherTable()

    initial_count = repo.get_count(session)

    teacher_email = "test123@example.com"
    new_teacher_email = "test_test@mail.ru"

    # Добавляем — flush внутри метода сделает INSERT видимым
    repo.insert_teacher(session, teacher_email)
    assert repo.get_count(session) == initial_count + 1

    # Ищем по email — теперь он есть
    teacher_obj = repo.find_teacher_by_email(session, teacher_email)
    assert teacher_obj is not None
    teacher_id = teacher_obj.teacher_id

    # Обновляем
    repo.update_teacher_email(session, teacher_id, new_teacher_email)
    updated_teacher = repo.get_teacher_by_id(session, teacher_id)
    assert updated_teacher.email == new_teacher_email

    # Удаляем
    repo.delete_teacher(session, new_teacher_email)
    assert repo.get_count(session) == initial_count