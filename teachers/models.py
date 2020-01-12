from students.models import Person


class Teacher(Person):
    class Meta:
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"
