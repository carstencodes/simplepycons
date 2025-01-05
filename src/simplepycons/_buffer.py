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


class BufferIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "buffer"

    @property
    def original_file_name(self) -> "str":
        return "buffer.svg"

    @property
    def title(self) -> "str":
        return "Buffer"

    @property
    def primary_color(self) -> "str":
        return "#231F20"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Buffer</title>
     <path d="M1.371 5.476L11.943 0l10.686 5.476-10.686 5.495zm3.36
 4.81l7.212 3.547 7.288-3.547 3.398 1.655-10.686 5.202L1.371 11.94zm0
 6.171l7.212 3.911 7.288-3.91 3.398 1.815L11.943 24 1.371 18.273z" />
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
