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


class PaysafeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "paysafe"

    @property
    def original_file_name(self) -> "str":
        return "paysafe.svg"

    @property
    def title(self) -> "str":
        return "Paysafe"

    @property
    def primary_color(self) -> "str":
        return "#5A28FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Paysafe</title>
     <path d="m23.905 12.233-7.672 7.673a.16.16 0 0
 1-.115.047h-.048a.162.162 0 0 1-.162-.161v-7.787a.324.324 0 0
 1-.094.228L8.188 19.86a.332.332 0 0 1-.466 0L.095 12.235a.332.332 0 0
 1 0-.466L7.72 4.142a.334.334 0 0 1 .467 0l7.625
 7.625c.06.06.094.143.094.23V4.208c0-.089.073-.162.162-.162h.048c.043
 0 .084.018.115.048l7.672 7.672a.333.333 0 0 1 .002.467z" />
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
