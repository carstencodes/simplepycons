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


class StartdotggIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "startdotgg"

    @property
    def original_file_name(self) -> "str":
        return "startdotgg.svg"

    @property
    def title(self) -> "str":
        return "start.gg"

    @property
    def primary_color(self) -> "str":
        return "#2E75BA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>start.gg</title>
     <path d="M6 0A5.999 5.999 0 00.002 6v5.252a.75.75 0
 00.75.748H5.25a.748.748 0 00.75-.747V6.749C6 6.334 6.336 6 6.748
 6h16.497a.748.748 0 00.749-.748V.749A.743.743 0 0023.247 0zm12.75
 12a.748.748 0 00-.75.75v4.5a.748.748 0 01-.747.748H.753a.754.754 0
 00-.75.751v4.5a.75.75 0 00.75.751H18a5.999 5.999 0
 005.999-6v-5.25a.75.75 0 00-.75-.75z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://help.start.gg/en/articles/1716774-sta'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://help.start.gg/en/articles/1716774-sta'''

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
