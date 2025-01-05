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


class BrexIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "brex"

    @property
    def original_file_name(self) -> "str":
        return "brex.svg"

    @property
    def title(self) -> "str":
        return "Brex"

    @property
    def primary_color(self) -> "str":
        return "#212121"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Brex</title>
     <path d="M18.69 2.319a3.868 3.868 0 0 0-3.108 1.547l-.759
 1.007a1.658 1.658 0 0 1-1.313.656H0V21.68h5.296a3.87 3.87 0 0 0
 3.108-1.547l.759-1.006a1.656 1.656 0 0 1
 1.313-.657H24V2.319h-5.31Zm1.108 11.949h-5.66a3.87 3.87 0 0 0-3.108
 1.547l-.759 1.007a1.658 1.658 0 0 1-1.313.656H4.202V9.731h5.661a3.868
 3.868 0 0 0 3.107-1.547l.759-1.006a1.658 1.658 0 0 1
 1.313-.657h4.771l-.015 7.747Z" />
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
