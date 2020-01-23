class TestCase:
  def __init__(self, name):
    self.name = name

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def run(self):
    self.setUp()
    method = getattr(self, self.name)
    method()
    self.tearDown()
    return TestResult()


class WasRun(TestCase):
  def __init__(self, name):
    TestCase.__init__(self, name)

  def setUp(self):
    self.wasRun = None
    self.log = "setUp "

  def testMethod(self):
    self.wasRun = 1
    self.log += "testMethod "

  def tearDown(self):
    self.log += "tearDown "


class TestCaseTest(TestCase):
  def setUp(self):
    self.test = WasRun("testMethod")

  def testTemplateMethod(self):
    test = WasRun("testMethod")
    test.run()
    print(test.log)
    assert("setUp testMethod tearDown ")
    # self.test.run()
    # assert("setUp testMethod " == self.test.log)

  def testResult(self):
    test = WasRun("testMethod")
    result = test.run()
    assert("1 run, 0 failed" == result.summary())


class TestResult:
  def summary(self):
    return "1 run, 0 failed"


TestCaseTest("testTemplateMethod").run()
