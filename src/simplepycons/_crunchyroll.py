#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class CrunchyrollIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "crunchyroll"

    @property
    def original_file_name(self) -> "str":
        return "crunchyroll.svg"

    @property
    def title(self) -> "str":
        return "Crunchyroll"

    @property
    def primary_color(self) -> "str":
        return "#FF5E00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Crunchyroll</title>
     <path d="M2.909 13.436C2.914 7.61 7.642 2.893 13.468
 2.898c5.576.005 10.137 4.339 10.51 9.819q.021-.351.022-.706C24.007
 5.385 18.64.006 12.012 0S.007 5.36 0 11.988 5.36 23.994 11.988
 24q.412 0
 .815-.027c-5.526-.338-9.9-4.928-9.894-10.538Zm16.284.155a4.1 4.1 0 0
 1-4.095-4.103 4.1 4.1 0 0 1 2.712-3.855 8.95 8.95 0 0 0-4.187-1.037
 9.007 9.007 0 1 0 8.997 9.016q-.001-.847-.15-1.651a4.1 4.1 0 0
 1-3.278 1.63Z" />
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
