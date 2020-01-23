class TestCase:
  def __init__(self, name):
    self.name = name

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def run(self):
    result = TestResult()
    result.testStarted()
    self.setUp()
    # Breaks assertions in TestCaseTest
    try:
      method = getattr(self, self.name)
      method()
    except:
      result.testFailed()
    self.tearDown()
    return result


class WasRun(TestCase):
  def __init__(self, name):
    TestCase.__init__(self, name)

  def setUp(self):
    self.wasRun = None
    self.log = "setUp "

  def testMethod(self):
    self.wasRun = 1
    self.log += "testMethod "

  def testBrokenMethod(self):
    raise Exception

  def tearDown(self):
    self.log += "tearDown "


class TestCaseTest(TestCase):
  def setUp(self):
    self.test = WasRun("testMethod")

  def testTemplateMethod(self):
    test = WasRun("testMethod")
    test.run()
    assert("setUp testMethod tearDown ")

  def testResult(self):
    test = WasRun("testMethod")
    result = test.run()
    assert("1 run, 0 failed" == result.summary())

  def testFailedResult(self):
    test = WasRun("testBrokenMethod")
    result = test.run()
    assert("1 run, 1 failed" == result.summary)

  def testFailedResultFormatting(self):
    result = TestResult()
    result.testStarted()
    result.testFailed()
    assert("1 run, 1 failed" == result.summary())

  def testSuite(self):
    suite = TestSuite()
    suite.add(WasRun("testMethod"))
    suite.add(WasRun("testBrokenMethod"))
    result = suite.run()
    assert("2 run, 1 failed qweqwe" == result.summary())


class TestResult:
  def __init__(self):
    self.runCount = 0
    self.errorCount = 0

  def testStarted(self):
    self.runCount += 1

  def testFailed(self):
    self.errorCount += 1

  def summary(self):
    return f"{self.runCount} run, {self.errorCount} failed"


class TestSuite:
  def __init__(self):
    self.tests = []

  def add(self, test):
    self.tests.append(test)

    def run(self):
      result = TestResult()
      for test in self.tests:
        test.run(result)
      print("result", result)
      return result


print(TestCaseTest("testTemplateMethod").run().summary())
print(TestCaseTest("testResult").run().summary())
print(TestCaseTest("testFailedResult").run().summary())
print(TestCaseTest("testFailedResultFormatting").run())
print(TestCaseTest("testSuite").run().summary())
