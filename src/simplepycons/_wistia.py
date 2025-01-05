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


class WistiaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wistia"

    @property
    def original_file_name(self) -> "str":
        return "wistia.svg"

    @property
    def title(self) -> "str":
        return "Wistia"

    @property
    def primary_color(self) -> "str":
        return "#58B7FE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wistia</title>
     <path d="M23.69 6.605c.507-3.094-1.24-3.944-1.24-3.944s.073
 2.519-4.555 3.053C13.787 6.188 0 5.83 0 5.83l4.43 5.081c1.2 1.378
 1.838 1.537 3.187 1.633 1.349.09 4.327.058 6.345-.096 2.206-.169
 5.35-.888 7.477-2.535 1.09-.843 2.039-2.016 2.25-3.308m.284
 3.205s-.556 1.105-3.33 2.853c-1.182.744-3.637 1.535-6.793
 1.84-1.705.166-4.842.031-6.188.031-1.354 0-1.974.285-3.187 1.652L0
 21.23s1.55.008 2.72.008c1.17 0 8.488.425 11.735-.468 10.546-2.899
 9.518-10.96 9.518-10.96Z" />
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
