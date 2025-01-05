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


class NikeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nike"

    @property
    def original_file_name(self) -> "str":
        return "nike.svg"

    @property
    def title(self) -> "str":
        return "Nike"

    @property
    def primary_color(self) -> "str":
        return "#111111"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Nike</title>
     <path d="M24 7.8L6.442 15.276c-1.456.616-2.679.925-3.668.925-1.12
 0-1.933-.392-2.437-1.177-.317-.504-.41-1.143-.28-1.918.13-.775.476-1.6
 1.036-2.478.467-.71 1.232-1.643 2.297-2.8a6.122 6.122 0 00-.784
 1.848c-.28 1.195-.028 2.072.756 2.632.373.261.886.392 1.54.392.522 0
 1.11-.084 1.764-.252L24 7.8z" />
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
