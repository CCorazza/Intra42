import ldap

class Ldap(object):
  """Surcouche du module ldap"""

  __host = 'ldaps://ldap.42.fr:636'
  __base_dn = 'uid=%s,ou=2013,ou=people,dc=42,dc=fr'

  def __init__(self, username, password):
    'Constructeur: Ldap(username, password)'
    self.handler = None
    self.username = username
    self.password = password
    self.dn = self.__base_dn % username

  def __del__(self):
    'Destructeur'
    self.disconnect()

  def connect(self):
    'Retourne True si la connexion reussit ou False si elle echoue'
    try:
      self.handler = ldap.initialize(self.__host)
      self.handler.simple_bind_s(self.dn, self.password)
      return True
    except ldap.LDAPError, e:
      self.handler = None
      return False

  def disconnect(self):
    'Interrompt la connexion avec le ldap'
    if (self.handler is not None):
      self.handler.unbind()
      self.handler = None

  def get_by_uid(self, uid=None):
    'Retourne tous les champs disponibles dans le ldap pour un login donne'
    ret = []
    if (self.handler is None):
      return {}
    if (uid is None):
      uid = self.username
    result = self.handler.search(self.__base_dn[7:], ldap.SCOPE_SUBTREE,
                                 'uid=%s' % uid, ['*'])
    while (True):
      r_type, r_data = self.handler.result(result, 0)
      if (r_data == []): break
      elif (r_type == ldap.RES_SEARCH_ENTRY): ret.append(r_data)
    if (ret != []):
      ret = ret[0][0][1]
      clean_ret = {}
      for (k, v) in ret.items():
        clean_ret[k.replace('-', '_')] = v[0]
      return clean_ret
    return {}

  def search(self, search_attr=['*'], search_filter='uid=*'):
    'Retourne les champs demandes pour un filtre donne'
    ret = []
    data = []
    if (self.handler is None):
      return []
    result = self.handler.search(self.__base_dn[7:], ldap.SCOPE_SUBTREE,
                                 search_filter, search_attr)
    while (True):
      r_type, r_data = self.handler.result(result, 0)
      if (r_data == []): break
      elif (r_type == ldap.RES_SEARCH_ENTRY): data.append(r_data)
    for user in data:
      dico = {}
      for k,v in user[0][1].items():
        dico[k.replace('-', '_')] = v[0]
      ret.append(dico)
    return ret
