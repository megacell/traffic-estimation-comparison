import unittest
try:
    from comparison.src.scenario_utils import parser
    from comparison.src.Scenario import Scenario
except ImportError:
    from src.scenario_utils import parser
    from src.Scenario import Scenario

__author__ = 'cathywu'

class TestSolverCS(unittest.TestCase):

    def setUp(self):
        # use argparse object as default template
        p = parser()
        self.args, unknown = p.parse_known_args()
        self.args.solver = 'CS'

    def test_p(self):
        self.args.model = 'P'
        self.args.nrow = 5
        self.args.ncol = 2
        self.args.use_L = False
        self.args.sparse = True
        scen = Scenario(args=self.args)
        scen.run()
        self.assertTrue(True)

    def test_ue(self):
        self.args.model = 'UE'
        scen = Scenario(args=self.args)
        scen.run()
        self.assertTrue(True)

    def test_so(self):
        self.args.model = 'SO'
        scen = Scenario(args=self.args)
        scen.run()
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()