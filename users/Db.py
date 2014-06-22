from models import Student
from datetime import datetime

def update(uid, fields = {}):
  "Actualise une entree dans la base de donnees"
  student = Student.objects.filter(uid=uid)
  if (student):
    student = student[0]
    for k, v in fields.items():
      if hasattr(student, k):
        if (k == 'latest_activity'):
          now = datetime.now()
          attr = '%d/%d/%d : %02dh%02d' \
                 % (now.day, now.month, now.year, now.hour, now.minute)
          setattr(student, k, attr)
        else:
          setattr(student, k, v)
    student.save()

def get(uid, fields = ()):
  "Recupere une entree dans la base de donnes"
  ret = {}
  student = Student.objects.filter(uid=uid)
  if (student):
    student = student[0]
    for i in fields:
      if hasattr(student, i):
        ret[i] = getattr(student, i)
  return ret
