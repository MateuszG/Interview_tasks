
class FirstParent(object):
  def __init__(self):
    super(FirstParent, self).__init__()
    print ("P first")


class SecondParent(object):
  def __init__(self):
    super(SecondParent, self).__init__()
    print ("P second")


class First(FirstParent):
  def __init__(self):
    super(First, self).__init__()
    print ("first")


class Second(SecondParent):
  def __init__(self):
    super(Second, self).__init__()
    print ("second")


class Third(First, Second):
  def __init__(self):
    super(Third, self).__init__()
    print ("that's it")

a = Third()
# P second
# second
# P first
# first
# that's it
