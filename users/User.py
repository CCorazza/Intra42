import Db
import json
import urllib
from Ldap import *
from models import Student
from django.contrib.auth.models import User as SU

class User(object):
  """Gestion des utilisateurs"""

  __crawler_url = 'https://dashboard.42.fr/crawler/pull/%s/'

  def __init__(self, username, password):
    'Constructeur: User(username, password)'
    self.db = None
    self.ldap = None
    self.infos = {}
    self.connected = False
    self.username = username
    self.password = password
    self.login()
    if (self.connected):
      self.infos['location'] = self.get_location()
      self.save_location()

  def __del__(self):
    'Destructeur'
    self.logout()

  def login(self):
    'Se connecte au ldap pour verifier les identifiants'
    self.ldap = Ldap(self.username, self.password)
    if (self.ldap.connect()):
      self.connected = True
      self.infos = self.get_info()
      if (not Student.objects.filter(uid=self.username)):
        Student(uid=self.username, privilege='etudiant').save()
      if (not SU.objects.filter(username=self.username)):
        user = SU.objects.create_user(self.username, '%s@student.42.fr' % self.username, self.password)
        user.first_name = self.infos['first_name']
        user.last_name = self.infos['last_name']
        user.save()
      user = SU.objects.get(username=self.username)
      user.set_password(self.password)
      user.save()

  def logout(self):
    'Se deconnecte'
    self.connected = False
    if (self.ldap is not None):
      self.ldap.disconnect()
      self.ldap = None

  def save_location(self):
    if (self.connected):
      Db.update(self.username,
                {'latest_location': self.infos['location'], 'latest_activity': 1})

  def get(self, field):
    'Retourne un champ precis sur le user actuel'
    if (field in self.infos):
      return self.infos[field]
    return ''

  def get_info(self, uid=None):
    'Retourne les infos du user (ldap) sous forme de dictionnaire: User.get_info(uid)'
    if (self.connected):
      return self.ldap.get_by_uid(uid)
    return {}

  def get_location(self, uid=None):
    "Retourne la localisation d'un eleve: User.get_location(uid)"
    if (uid is None):
      uid = self.username
    res = urllib.urlopen(self.__crawler_url % (uid))
    if (res.getcode() == 200):
      status = json.loads(res.read())
      return status['last_host'].split('.')[0]
    return 'Hors-Ligne'

  def get_trombi(self):
    "Retourne la liste de tous les utilisateurs"
    if (not self.connected):
      return []
    data = self.ldap.search(['uid', 'first-name', 'last-name'])
    uid_cmp = lambda x: x['uid']
    return sorted(data, key=uid_cmp)

  def dump_ldap(self):
    "Dump le ldap dans la base de donnees"
    if (self.connected):
      data = self.ldap.search()
      for user in data:
        if (not Student.objects.filter(uid=user['uid'])):
          Student(uid=user['uid'], privilege='etudiant').save()
        if (not SU.objects.filter(username=user['uid'])):
          u = SU.objects.create_user(user['uid'], '%s@student.42.fr' % user['uid'], 'NULL')
          print str(u)
          u.first_name = user['first_name'][:30]
          u.last_name = user['last_name'][:30]
          u.save()
      return True
    return False
