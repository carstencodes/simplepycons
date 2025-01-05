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


class RiveIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rive"

    @property
    def original_file_name(self) -> "str":
        return "rive.svg"

    @property
    def title(self) -> "str":
        return "Rive"

    @property
    def primary_color(self) -> "str":
        return "#1D1D1D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Rive</title>
     <path d="M.643 1.475c0 .814.668 1.475 1.49 1.475H14.49c1.408 0
 2.568.43 3.48 1.29.91.861 1.366 1.967 1.366 3.32 0 1.25-.456
 2.274-1.367 3.072-.911.78-2.07 1.168-3.479 1.168H9.12c-.824
 0-1.491.66-1.491 1.475 0 .815.667 1.475 1.491 1.475h5.93l5.342
 8.482c.332.512.797.768 1.398.768.663 0 1.129-.256
 1.398-.768.269-.533.217-1.096-.155-1.69l-4.753-7.56c1.284-.574
 2.299-1.414 3.044-2.52.746-1.127 1.119-2.427 1.119-3.902
 0-1.496-.342-2.807-1.026-3.934-.662-1.127-1.594-2.008-2.795-2.643C17.42.327
 16.044 0 14.49 0H2.134C1.311 0 .643.66.643 1.475Z" />
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
