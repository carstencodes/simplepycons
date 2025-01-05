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


class RundeckIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rundeck"

    @property
    def original_file_name(self) -> "str":
        return "rundeck.svg"

    @property
    def title(self) -> "str":
        return "Rundeck"

    @property
    def primary_color(self) -> "str":
        return "#F73F39"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Rundeck</title>
     <path d="M19.35 4.8 16.325 0H.115L3.14 4.8h16.21zM.115
 24h16.21l3.025-4.8H3.14L.115 24zM6.163 9.6h16.21l1.512 2.4-1.512
 2.4H6.163L7.675 12 6.163 9.6z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/rundeck/docs/blob/a1c98b68
2eb6e82b60de0daa876133f390630821/docs/.vuepress/public/images/rundeck-'''

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
