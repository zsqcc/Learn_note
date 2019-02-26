# 学习了测试什么时候忽略
# setUp在测试用例执行前执行(多次加载),tearDown会在测试用例执行后执行
# 上下文管理器的使用(直接调用函数或者执行代码)
# with可以直接调用函数
# assertRaises：当错误是期待的错误时，不报错，反馈结果为 .
import unittest
import sys


def div_fun(seq):
    return sum(seq) / len(seq)


class SkipTest(unittest.TestCase):
    def setUp(self):
        self.stat = [1, 2, 3]

    @unittest.expectedFailure
    def test_fails(self):
        self.assertEqual(self.stat.length, 3)

    @unittest.skip("跳过")
    def test_skip(self):
        self.assertEqual(False, True)

    @unittest.skipIf(sys.version_info.minor == 6, "如果等于1跳过")
    def test_skipif(self):
        self.assertEqual(False, True)

    @unittest.skipUnless(sys.platform.startswith('win'), "windows 打断")
    def test_skipunless(self):
        with self.assertRaises(ZeroDivisionError): div_fun([])

    def test_with(self):
        with self.assertRaises(ZeroDivisionError): div_fun([])

    def tearDown(self):
        pass





if __name__ == "__main__":
    unittest.main()

