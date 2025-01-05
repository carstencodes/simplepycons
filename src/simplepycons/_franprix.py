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


class FranprixIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "franprix"

    @property
    def original_file_name(self) -> "str":
        return "franprix.svg"

    @property
    def title(self) -> "str":
        return "Franprix"

    @property
    def primary_color(self) -> "str":
        return "#EC6237"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Franprix</title>
     <path d="M12 6.305c3.691 0 6.323-3.071
 6.13-6.286-2.124-.17-5.069.791-6.13 3.79C10.939.81 7.993-.15 5.87.02
 5.677 3.234 8.309 6.305 12 6.305m11.002
 6.962c-.139-3.413-2.821-6.362-6.55-6.362-1.69 0-3.236.635-4.452
 1.744-1.217-1.11-2.763-1.744-4.452-1.744-3.729 0-6.412 2.949-6.55
 6.362C.758 19.19 5.913 24 12 24c6.087 0 11.242-4.81 11.002-10.733" />
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
