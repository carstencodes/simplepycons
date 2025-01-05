#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class TestrailIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "testrail"

    @property
    def original_file_name(self) -> "str":
        return "testrail.svg"

    @property
    def title(self) -> "str":
        return "TestRail"

    @property
    def primary_color(self) -> "str":
        return "#65C179"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>TestRail</title>
     <path d="M7.27 23.896 4.5 21.124a.352.352 0 0 1
 0-.5l2.772-2.77a.352.352 0 0 1 .5 0l2.772 2.772a.352.352 0 0 1 0
 .5l-2.772 2.77a.352.352 0 0 1-.5
 0H7.27zm4.48-4.48-2.772-2.772a.352.352 0 0 1
 0-.498l2.772-2.772a.352.352 0 0 1 .5 0l2.77 2.772a.352.352 0 0 1 0
 .5l-2.77 2.77a.352.352 0 0 1-.499 0zm4.48-4.48-2.77-2.772a.352.352 0
 0 1 0-.498l2.771-2.772a.352.352 0 0 1 .5 0l2.77 2.772a.352.352 0 0 1
 0 .498l-2.772 2.772a.352.352 0 0 1-.5
 0h.002zm-8.876.084-2.772-2.77a.352.352 0 0 1
 0-.499l2.772-2.773a.352.352 0 0 1 .5 0l2.772 2.772a.352.352 0 0 1 0
 .498l-2.772 2.774a.352.352 0 0 1-.5 0v-.002zm4.48-4.48L9.062
 7.77a.352.352 0 0 1 0-.5l2.772-2.772a.352.352 0 0 1 .5 0l2.77
 2.772a.352.352 0 0 1 0 .498l-2.77 2.772a.352.352 0 0 1-.499
 0v-.002.001zM7.44 6.15 4.666 3.37a.352.352 0 0 1
 0-.5L7.44.104a.352.352 0 0 1 .5 0l2.772 2.772a.352.352 0 0 1 0
 .5L7.938 6.142a.352.352 0 0 1-.5 0l.002.006v.001z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.ideracorp.com/Legal/idera-tradema'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
