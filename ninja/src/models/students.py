class Student (object):
  def __init__(self, **kwargs):
    self.indexes = kwargs.keys()

    if kwargs is not None:
      for key, value in kwargs.iteritems():
        self.key = value

  def __str__(self):
    return "%s, Github handle: %s" % (self.name, self.user)

  def __repr__(self):
    return self.__str__()

  @property
  def student_dict(self):
    return { attr : getattr(self, attr) for attr in self.indexes }

  def get_group(self):
    return self.group

  def get_user(self):
    return self.user