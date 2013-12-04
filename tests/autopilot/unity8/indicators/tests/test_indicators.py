# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
#
# Unity Indicators Autopilot Test Suite
# Copyright (C) 2013 Canonical
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from __future__ import absolute_import

import autopilot.platform

from unity8.indicators.emulators.widget import DefaultIndicatorWidget
from unity8.process_helpers import unlock_unity
from unity8.shell.tests import UnityTestCase


class IndicatorTestCase(UnityTestCase):

    scenarios = [
        ('Bluetooth', dict(indicator_name='indicator-bluetooth')),
        ('Datetime', dict(indicator_name='indicator-datetime')),
        ('Location', dict(indicator_name='indicator-location')),
        ('Messaging', dict(indicator_name='indicator-messages')),
        ('Network', dict(indicator_name='indicator-network')),
        ('Power', dict(indicator_name='indicator-power')),
        ('Sound', dict(indicator_name='indicator-sound')),
    ]

    def setUp(self):
        if self.model() == "Desktop":
            self.skipTest("Test cannot be run on the desktop.")
        super(IndicatorTestCase, self).setUp()

    def test_indicator_exists(self):
        """The tab of a given indicator can be found."""
        unity_proxy = self.launch_unity()
        unlock_unity(unity_proxy)
        widget = self.main_window.get_indicator_widget(
            self.indicator_name
        )
        self.assertIsNotNone(widget)


class IndicatorPageTitleMatchesWidgetTestCase(UnityTestCase):

    scenarios = [
        ('Bluetooth', dict(indicator_name='indicator-bluetooth',
                           title='Bluetooth')),
        ('Datetime', dict(indicator_name='indicator-datetime',
                          title='Upcoming')),
        ('Location', dict(indicator_name='indicator-location',
                          title='Location')),
        ('Messaging', dict(indicator_name='indicator-messages',
                           title='Incoming')),
        ('Network', dict(indicator_name='indicator-network',
                         title='Network')),
        ('Power', dict(indicator_name='indicator-power',
                       title='Battery')),
        ('Sound', dict(indicator_name='indicator-sound',
                       title='Sound')),
    ]

    def setUp(self):
        if platform.model() == "Desktop":
            self.skipTest("Test cannot be run on the desktop.")
        super(IndicatorPageTitleMatchesWidgetTestCase, self).setUp()

    def test_indicator_page_title_matches_widget(self):
        """Swiping open an indicator must show its correct title.

        See https://bugs.launchpad.net/ubuntu-ux/+bug/1253804 .
        """
        unity_proxy = self.launch_unity()
        unlock_unity(unity_proxy)
        window = self.main_window.get_qml_view()
        widget = self.main_window.get_indicator_widget(self.indicator_name)
        self.assertIsNotNone(widget)
        widget.swipe_to_open_indicator(window)
        title = window.wait_select_single(
            "IndicatorPage",
            title=self.title
        )
