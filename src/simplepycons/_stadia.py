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


class StadiaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "stadia"

    @property
    def original_file_name(self) -> "str":
        return "stadia.svg"

    @property
    def title(self) -> "str":
        return "Stadia"

    @property
    def primary_color(self) -> "str":
        return "#CD2640"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Stadia</title>
     <path d="M6.5253 10.0302a18.279 18.279 0 0 1
 15.7805.263c.263.1973.6575 0 .7233-.263l.9205-2.8273c.1315-.263
 0-.6576-.3288-.789A22.3557 22.3557 0 0 0 .2788 8.6493a.6575.6575 0 0
 0-.1972.8548l2.1698 4.7999c.1315.3287.526.526.8548.3945 2.4328-.9205
 6.1807-1.841 9.9943-1.315-2.63.4602-4.6684 1.3807-6.3122
 2.367a.6575.6575 0 0 0-.1972.8548L7.906
 19.63c.1315.263.4603.3288.6575.1315.526-.526 1.052-.9205
 1.5123-1.1835 2.104-1.1836 4.9972-2.1041 8.8765-1.9068a.6575.6575 0 0
 0 .6576-.4603l.9862-2.9589c.1316-.263 0-.6575-.263-.789a20.0544
 20.0544 0 0 0-13.8737-2.4328z" />
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
