import unittest
import scripts.data as dt
import scripts.groupActions as ga


class GroupActionsTest(unittest.TestCase):

    data = dt.GetData()
    group = ga.GActions()
    create = group.create_group()
    group_id = create['data']['Value']

    def test_1_createGroup(self):
        print(self.group_id)
        groups = self.data.get_groups()
        string = "'Id': " + str(self.group_id)
        assert string in str(groups['data']['Values'])

    def test_2_updateGroup(self):
        print(self.group_id)
        update = self.group.update_group(self.group_id)
        assert 'True' in str(update['data']['Value'])
        groups = self.data.get_groups()
        string = "'Limit': 20, 'Name': 'Группа обучения №15', 'Number': 15"
        assert string in str(groups['data']['Values'])

    def test_3_deleteGroup(self):
        print(self.group_id)
        self.group.delete_group(self.group_id)
        groups = self.data.get_groups()
        string = "'Limit': 20, 'Name': 'Группа обучения №15', 'Number': 15"
        self.assertNotIn(string, str(groups['data']['Values']))


