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


class EngadgetIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "engadget"

    @property
    def original_file_name(self) -> "str":
        return "engadget.svg"

    @property
    def title(self) -> "str":
        return "Engadget"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Engadget</title>
     <path d="M0 20.067a3.9 3.9 0 0 0 4 3.866h16v-4H4v-4h15.733A4.231
 4.231 0 0 0 24 12.067V4.333A4.483 4.483 0 0 0 19.733.067H4a4.346
 4.346 0 0 0-4 4.266Zm20-8.134H4v-8h16Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://o.aolcdn.com/engadget/brand-kit/eng-l'''
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
