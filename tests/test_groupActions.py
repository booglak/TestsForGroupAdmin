import unittest
import scripts.data as dt
import scripts.groupActions as ga


class GroupActionsTest(unittest.TestCase):

    data = dt.GetData()
    group = ga.GActions()
    group_id = 1

    def createGroup(self):
        create = self.group.create_group()
        self.group_id = create['data']['Value']
        groups = self.data.get_groups()
        string = "'Id': "+ str(self.group_id)
        assert string in str(groups['data']['Values'])

    def test_updateGroup(self):
        update = self.group.update_group(self.group_id)
        groups = self.data.get_groups()
        string = "'Limit': 20, 'Name': 'Группа обучения №15', 'Number': 15"
        assert string in str(groups['data']['Values'])






