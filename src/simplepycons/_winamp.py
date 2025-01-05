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


class WinampIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "winamp"

    @property
    def original_file_name(self) -> "str":
        return "winamp.svg"

    @property
    def title(self) -> "str":
        return "Winamp"

    @property
    def primary_color(self) -> "str":
        return "#F93821"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Winamp</title>
     <path d="M11.902 0a.987.987 0 0 0-.91.604l-6.139
 14.57c-.176.42.131.883.586.883H8.66a.987.987 0 0 0
 .91-.604L15.707.883A.636.636 0 0 0 15.12 0h-3.219Zm3.438
 7.943a.987.987 0 0 0-.91.604l-6.137
 14.57c-.177.42.13.883.586.883h3.219a.987.987 0 0 0
 .91-.604l6.138-14.57a.636.636 0 0 0-.586-.883h-3.22Z" />
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
