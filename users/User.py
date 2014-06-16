import json
import urllib
from Ldap import *
from models import Student

class User(object):
  """Gestion des utilisateurs"""

  __crawler_url = 'https://dashboard.42.fr/crawler/pull/%s/'

  def __init__(self, username, password):
    'Constructeur: User(username, password)'
    self.my_ldap = None
    self.connected = False
    self.username = username
    self.password = password
    self.infos = {}
    self.login()
    if (self.connected):
      self.infos = self.get_info()
      self.infos['location'] = self.get_location()
      self.save_location()

  def __del__(self):
    'Destructeur'
    self.save_location()
    self.logout()

  def login(self):
    'Se connecte au ldap pour verifier les identifiants'
    self.my_ldap = Ldap(self.username, self.password)
    if (self.my_ldap.connect()):
      self.connected = True

  def logout(self):
    'Se deconnecte'
    self.connected = False
    if (self.my_ldap is not None):
      self.my_ldap.disconnect()
      self.my_ldap = None

  def save_location(self):
    if (self.connected):
      student = Student.objects.filter(uid=self.infos['uid'])
      if (student):
        student[0].latest_location = self.infos['location']
        student[0].save()

  def get(self, field):
    'Retourne un champ precis sur le user actuel'
    if (self.infos.has_key(field)):
      return self.infos[field]
    return ''

  def get_info(self, uid=None):
    'Retourne les infos du user (ldap) sous forme de dictionnaire: User.get_info(uid)'
    if (self.connected):
      return self.my_ldap.get_by_uid(uid)
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
    data = self.my_ldap.search(['uid', 'first-name', 'last-name'])
    uid_cmp = lambda x: x['uid']
    return sorted(data, key=uid_cmp)

  def dump_ldap(self):
    "Dump le ldap dans la base de donnees"
    if (self.connected):
      data = self.my_ldap.search()
      for user in data:
        if (not Student.objects.filter(uid=user['uid'])):
          Student(uid=user['uid'], privilege='etudiant').save()
      return True
    return False
