import pytest
from classes import *

class Test:
    def setup_method(self):
        self.t1 = Television()

    def teardown_method(self):
        del self.t1

    def test_init(self):
        assert self.t1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
    
    def test_power(self) -> None:
        self.t1.power()
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
        self.t1.power()
        assert self.t1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'

    def test_channel_up(self) -> None:
        self.t1.channel_up()
        assert self.t1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.t1.power()
        self.t1.channel_up()
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 1, Volume = 0'
        self.t1.channel_up()
        self.t1.channel_up()
        self.t1.channel_up()
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'

    def test_channel_down(self) -> None:
        self.t1.channel_up()
        assert self.t1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.t1.power()
        self.t1.channel_down()
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 3, Volume = 0'
        self.t1.channel_up()
        self.t1.channel_up()
        self.t1.channel_down()
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'

    def test_volume_up(self) -> None:
        self.t1.volume_up()
        assert self.t1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.t1.power()
        self.t1.volume_up()
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 1'
        self.t1.volume_up()
        self.t1.volume_up()
        self.t1.volume_up()
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 2'
        self.t1.volume_down()
        self.t1.volume_down()
        self.t1.volume_up()
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 1'

    def test_volume_down(self) -> None:
        self.t1.volume_down()
        assert self.t1.__str__() == 'TV status: Is on = False, Channel = 0, Volume = 0'
        self.t1.power()
        self.t1.volume_down()
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'
        self.t1.volume_up()
        self.t1.volume_up()
        self.t1.volume_down()
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 1'
        self.t1.volume_down()
        self.t1.volume_down()
        self.t1.volume_down()
        assert self.t1.__str__() == 'TV status: Is on = True, Channel = 0, Volume = 0'

    
