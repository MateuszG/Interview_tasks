
class FirstParent(object):
  def __init__(self):
    print ("P first")


class SecondParent(object):
  def __init__(self):
    print ("P second")


class First(FirstParent):
  def __init__(self):
    print ("first")


class Second(SecondParent):
  def __init__(self):
    print ("second")


class Third(First, Second):

  def __init__(self):
    super(Third, self).__init__()
    print ("that's it")

a = Third()
# first
# that's it
