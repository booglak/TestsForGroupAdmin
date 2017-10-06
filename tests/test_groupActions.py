import unittest
import scripts.data as dt
import scripts.groupActions as ga


class GroupActionsTest(unittest.TestCase):

    data = dt.GetData()
    group = ga.GActions()
    group_id = 0

    def test_createGroup(self):
        create = self.group.create_group()
        self.group_id = create['data']['Value']
        groups = self.data.get_groups()
        string = "'Id': "+ str(self.group_id)
        assert string in str(groups['data']['Values'])




