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


class DuplicatiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "duplicati"

    @property
    def original_file_name(self) -> "str":
        return "duplicati.svg"

    @property
    def title(self) -> "str":
        return "Duplicati"

    @property
    def primary_color(self) -> "str":
        return "#1E3A8A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Duplicati</title>
     <path d="M8.571 1.286A1.72 1.72 0 0 0 6.857 3v10.286c0 .634.353
 1.183.868 1.48.251.144.538.234.846.234h13.715A1.72 1.72 0 0 0 24
 13.286V3a1.72 1.72 0 0 0-1.714-1.714Zm.56 12.087zm3.166
 0zm-10.583-.087A1.72 1.72 0 0 0 0 15v6a1.72 1.72 0 0 0 1.714
 1.714h8.572a1.715 1.715 0 0 0
 1.473-.857c.148-.253.241-.544.241-.857v-4.286H8.571c-.296
 0-.582-.042-.857-.114a3.439 3.439 0 0 1-2.571-3.314Zm18
 3.428h-6V21H18a1.72 1.72 0 0 0 1.714-1.714z" />
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
