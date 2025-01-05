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


class MeizuIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "meizu"

    @property
    def original_file_name(self) -> "str":
        return "meizu.svg"

    @property
    def title(self) -> "str":
        return "Meizu"

    @property
    def primary_color(self) -> "str":
        return "#FF4132"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Meizu</title>
     <path d="M20.045 18.818h3.546A.41.41 0 0 0 24 18.41v-3.545a.41.41
 0 0 0-.41-.41h-3.545a.41.41 0 0 0-.409.41v3.545c0
 .226.184.41.41.41zM13.8 12.11a.095.095 0 0 1-.163-.068V5.591a.41.41 0
 0 0-.409-.41H10.59a.545.545 0 0 0-.385.16L.16 15.387a.545.545 0 0
 0-.16.385v2.638c0 .226.183.41.41.41h2.637a.547.547 0 0 0
 .385-.16l6.769-6.769a.096.096 0 0 1 .163.068v6.451c0
 .226.183.41.409.41h2.638a.547.547 0 0 0 .385-.16L23.84 8.613A.545.545
 0 0 0 24 8.23V5.59a.41.41 0 0 0-.41-.41h-2.637a.546.546 0 0
 0-.386.16z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Meizu'''

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
