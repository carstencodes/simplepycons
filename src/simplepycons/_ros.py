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


class RosIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ros"

    @property
    def original_file_name(self) -> "str":
        return "ros.svg"

    @property
    def title(self) -> "str":
        return "ROS"

    @property
    def primary_color(self) -> "str":
        return "#22314E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ROS</title>
     <path d="M2.807 0C1.353 0 .173 1.22.173 2.722c0 1.504 1.18 2.723
 2.634 2.723 1.455 0 2.635-1.22 2.635-2.723S4.262 0 2.807 0zM12
 0c-1.455 0-2.634 1.22-2.634 2.722 0 1.504 1.18 2.723 2.634 2.723
 1.455 0 2.634-1.22 2.634-2.723S13.454 0 12 0zm9.193 0c-1.455 0-2.635
 1.22-2.635 2.722 0 1.504 1.18 2.723 2.635 2.723 1.455 0 2.634-1.22
 2.634-2.723S22.647 0 21.193 0zM2.807 9.277C1.353 9.277.173 10.497.173
 12s1.18 2.722 2.634 2.722c1.455 0 2.635-1.219 2.635-2.722
 0-1.504-1.18-2.723-2.635-2.723zm9.193 0c-1.455 0-2.634 1.22-2.634
 2.723s1.18 2.722 2.634 2.722c1.455 0 2.634-1.219 2.634-2.722
 0-1.504-1.18-2.723-2.634-2.723zm9.193 0c-1.455 0-2.635 1.22-2.635
 2.723s1.18 2.722 2.635 2.722c1.455 0 2.634-1.219 2.634-2.722
 0-1.504-1.18-2.723-2.634-2.723zM2.807 18.555c-1.454 0-2.634
 1.22-2.634 2.722C.173 22.781 1.353 24 2.807 24c1.455 0 2.635-1.22
 2.635-2.723s-1.18-2.722-2.635-2.722zm9.193 0c-1.455 0-2.634
 1.22-2.634 2.722C9.366 22.781 10.546 24 12 24c1.455 0 2.634-1.22
 2.634-2.723s-1.18-2.722-2.634-2.722zm9.193 0c-1.455 0-2.635
 1.22-2.635 2.722 0 1.504 1.18 2.723 2.635 2.723 1.455 0 2.634-1.22
 2.634-2.723s-1.18-2.722-2.634-2.722z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
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
