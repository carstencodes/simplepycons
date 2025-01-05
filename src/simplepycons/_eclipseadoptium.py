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


class EclipseAdoptiumIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "eclipseadoptium"

    @property
    def original_file_name(self) -> "str":
        return "eclipseadoptium.svg"

    @property
    def title(self) -> "str":
        return "Eclipse Adoptium"

    @property
    def primary_color(self) -> "str":
        return "#FF1464"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Eclipse Adoptium</title>
     <path d="m11.98 14.013-2.632 5.729 6.813
 3.058c-1.55-2.754-2.82-5.852-4.18-8.787Zm11.033 4.645L16.277
 4.064a3.952 3.952 0 0 1-.387 1.471l-3.6 7.82 3.871 8.361a3.76 3.76 0
 0 0 3.445 2.245 3.734 3.734 0 0 0
 3.755-3.755c0-.542-.155-1.045-.348-1.548zM15.735 3.755A3.734 3.734 0
 0 0 11.982 0C10.51 0 9.27.852 8.65 2.052 6.119 7.582 3.544 13.127.988
 18.658c-.232.464-.348 1.006-.348 1.587A3.734 3.734 0 0 0 4.394
 24a3.76 3.76 0 0 0
 3.445-2.245l7.587-16.413c.193-.503.31-1.045.31-1.587z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.eclipse.org/legal/logo_guidelines'''
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
