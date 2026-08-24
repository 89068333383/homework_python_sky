from sqlalchemy.orm import Session
from models import Teacher

class TeacherTable:
    @staticmethod
    def get_count(session: Session) -> int:
        return session.query(Teacher).count()

    @staticmethod
    def insert_teacher(session: Session, email: str, group_id: int = None) -> Teacher:
        new_teacher = Teacher(email=email, group_id=group_id)
        session.add(new_teacher)
        # flush() отправляет INSERT в БД, чтобы COUNT его увидел, но не делает COMMIT
        session.flush()
        return new_teacher

    @staticmethod
    def find_teacher_by_email(session: Session, email: str):
        return session.query(Teacher).filter_by(email=email).first()

    @staticmethod
    def update_teacher_email(session: Session, teacher_id: int, new_email: str):
        teacher = session.query(Teacher).filter_by(teacher_id=teacher_id).first()
        if teacher:
            teacher.email = new_email
            session.flush()  # тоже делаем flush, чтобы изменения были видны в этом же тесте

    @staticmethod
    def get_teacher_by_id(session: Session, teacher_id: int):
        return session.query(Teacher).filter_by(teacher_id=teacher_id).first()

    @staticmethod
    def delete_teacher(session: Session, email: str):
        teacher = session.query(Teacher).filter_by(email=email).first()
        if teacher:
            session.delete(teacher)
            session.flush() 