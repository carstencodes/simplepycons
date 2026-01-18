#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class ChinaRailwayIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "chinarailway"

    @property
    def original_file_name(self) -> "str":
        return "chinarailway.svg"

    @property
    def title(self) -> "str":
        return "China Railway"

    @property
    def primary_color(self) -> "str":
        return "#FF2600"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>China Railway</title>
     <path d="M15.642 18.64a8.035 8.035 0 1 0-7.284 0l-1.476
 1.932a10.435 10.435 0 0 1 3.136-19.339 1.043 1.043 0 0 1 .939-1.186
 11.478 11.478 0 0 1 2.086 0 1.043 1.043 0 0 1 .939 1.186 10.435
 10.435 0 0 1 3.136 19.339zm2.805 4.04a.417.417 0 0 1
 .336.41V24H5.217v-.91a.417.417 0 0 1 .336-.41l4.438-.887a1.46 1.46 0
 0 0 1.174-1.432v-5.934a1.043 1.043 0 0
 0-.757-1.003l-2.06-.59V10.94a1.46 1.46 0 0 1 1.345-1.456 29.217
 29.217 0 0 1 4.614 0 1.46 1.46 0 0 1 1.345
 1.456v1.896l-2.06.589a1.043 1.043 0 0 0-.757 1.003v5.934a1.46 1.46 0
 0 0 1.174 1.432z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:China'''

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
