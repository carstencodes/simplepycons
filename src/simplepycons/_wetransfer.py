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


class WetransferIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wetransfer"

    @property
    def original_file_name(self) -> "str":
        return "wetransfer.svg"

    @property
    def title(self) -> "str":
        return "WeTransfer"

    @property
    def primary_color(self) -> "str":
        return "#409FFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>WeTransfer</title>
     <path d="M13.855 11.891c0-3.382 2.4-5.4 5.51-5.4C22.145 6.491 24
 7.91 24 9.873c0 1.855-1.582 3.055-3.328 3.055-.982
 0-1.69-.164-2.182-.546-.163-.164-.272-.109-.272.055 0 .709.272
 1.254.709 1.745.382.382 1.09.655 1.745.655.71 0 1.31-.164
 1.855-.437.545-.272.982-.163 1.254.273.328.49-.109 1.145-.49
 1.582-.71.763-2.073 1.309-3.819
 1.309-3.545-.11-5.618-2.51-5.618-5.673zm-7.254 2.237c.327 0
 .545.163.763.545l.982 1.582c.382.6.709 1.036 1.418 1.036.71 0
 1.091-.273 1.418-1.09a21.11 21.11 0
 001.31-3.873c.49-1.855.709-2.946.709-3.873s-.273-1.473-1.31-1.637c-1.363-.272-3.272-.381-5.29-.381-2.019
 0-3.928.109-5.291.327C.273 6.982 0 7.528 0 8.454c0 .928.219 2.019.655
 3.874a28.714 28.714 0 001.31 3.872c.381.818.708 1.091 1.417 1.091.71
 0 1.037-.436 1.419-1.036l.981-1.582c.273-.327.491-.545.819-.545z" />
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
