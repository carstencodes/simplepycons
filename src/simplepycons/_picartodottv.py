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


class PicartodottvIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "picartodottv"

    @property
    def original_file_name(self) -> "str":
        return "picartodottv.svg"

    @property
    def title(self) -> "str":
        return "Picarto.TV"

    @property
    def primary_color(self) -> "str":
        return "#1DA456"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Picarto.TV</title>
     <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12c6.628 0
 12-5.373 12-12S18.628 0 12 0zM7.08 4.182h2.781c.233 0
 .42.21.42.47v14.696c0 .26-.187.47-.42.47h-2.78c-.233
 0-.42-.21-.42-.47V4.652c0-.26.187-.47.42-.47zm4.664 0a.624.624 0 0 1
 .326.091c.355.209 7.451 4.42 8.057 4.78a.604.604 0 0 1 0
 1.039c-.436.264-7.558 4.495-8.074 4.789a.577.577 0 0
 1-.873-.512v-1.812c0-1.712 2.962-2.201 3.398-2.465a.604.604 0 0 0
 0-1.04c-.605-.36-3.398-.746-3.398-2.452V4.79c0-.334.251-.605.564-.61z"
 />
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
