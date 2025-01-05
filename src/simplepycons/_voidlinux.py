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


class VoidLinuxIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "voidlinux"

    @property
    def original_file_name(self) -> "str":
        return "voidlinux.svg"

    @property
    def title(self) -> "str":
        return "Void Linux"

    @property
    def primary_color(self) -> "str":
        return "#478061"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Void Linux</title>
     <path d="M15.818 12a3.82 3.82 0 0 1-3.82 3.82A3.82 3.82 0 0 1
 8.178 12a3.82 3.82 0 0 1 3.82-3.82 3.82 3.82 0 0 1 3.82 3.82Zm3.179
 9.73-2.726-2.725A8.212 8.212 0 0 1 12 20.212 8.212 8.212 0 0 1 3.788
 12a8.212 8.212 0 0 1 1.209-4.269l-2.73-2.73A12 12 0 0 0 0 12c0 6.627
 5.373 12 12 12a12 12 0 0 0 6.997-2.27zM12 0a12 12 0 0 0-6.997
 2.27L7.73 4.994A8.212 8.212 0 0 1 12 3.788 8.212 8.212 0 0 1 20.212
 12a8.212 8.212 0 0 1-1.209 4.269l2.73 2.73A12 12 0 0 0 24
 12c0-6.627-5.373-12-12-12Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://alpha.de.repo.voidlinux.org/logos/voi'''

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
