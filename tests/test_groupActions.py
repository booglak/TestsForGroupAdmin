import unittest
import scripts.data as dt
import scripts.groupActions as ga


class GroupActionsTest(unittest.TestCase):

    data = dt.GetData()
    group = ga.GActions()
    group_id = 0

    def test_createGroup(self):
        create = self.group.create_group()



