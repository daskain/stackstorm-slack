import yaml
import json

from st2tests.base import BaseActionTestCase


class SlackBaseActionTestCase(BaseActionTestCase):
    __test__ = False

    def setUp(self):
        super(SlackBaseActionTestCase, self).setUp()

        self._config_blank = self.load_yaml('config_blank.yaml')
        self._config_token = self.load_yaml('config_token.yaml')

    def load_yaml(self, filename):
        return yaml.safe_load(self.get_fixture_content(filename))

    def load_json(self, filename):
        return json.loads(self.get_fixture_content(filename))

    @property
    def config_blank(self):
        return self._config_blank

    @property
    def config_token(self):
        return self._config_token
