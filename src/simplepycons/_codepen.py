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


class CodepenIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "codepen"

    @property
    def original_file_name(self) -> "str":
        return "codepen.svg"

    @property
    def title(self) -> "str":
        return "CodePen"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>CodePen</title>
     <path d="M18.144 13.067v-2.134L16.55 12zm1.276 1.194a.628.628 0
 01-.006.083l-.005.028-.011.053-.01.031c-.005.016-.01.031-.017.047l-.014.03a.78.78
 0 01-.021.043l-.019.03a.57.57 0 01-.08.1l-.026.025a.602.602 0
 01-.036.03l-.029.022-.01.008-6.782 4.522a.637.637 0 01-.708 0L4.864
 14.79l-.01-.008a.599.599 0
 01-.065-.052l-.026-.025-.032-.034-.021-.028a.588.588 0
 01-.067-.11l-.014-.031a.644.644 0
 01-.017-.047l-.01-.03c-.004-.018-.008-.036-.01-.054l-.006-.028a.628.628
 0
 01-.006-.083V9.739c0-.028.002-.055.006-.083l.005-.027.011-.054.01-.03a.574.574
 0 01.12-.217l.031-.034.026-.025a.62.62 0 01.065-.052l.01-.008
 6.782-4.521a.638.638 0 01.708 0l6.782
 4.521.01.008.03.022.035.03c.01.008.017.016.026.025a.545.545 0
 01.08.1l.019.03a.633.633 0
 01.021.043l.014.03c.007.016.012.032.017.047l.01.031c.004.018.008.036.01.054l.006.027a.619.619
 0 01.006.083zM12 0C5.373 0 0 5.372 0 12 0 18.627 5.373 24 12 24c6.628
 0 12-5.372 12-12 0-6.627-5.372-12-12-12m0 10.492L9.745 12 12 13.51
 14.255 12zm.638 4.124v2.975l4.996-3.33-2.232-1.493zm-6.272-.356l4.996
 3.33v-2.974l-2.764-1.849zm11.268-4.52l-4.996-3.33v2.974l2.764
 1.85zm-6.272-.356V6.41L6.366 9.74l2.232 1.493zm-5.506
 1.549v2.134L7.45 12Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://blog.codepen.io/documentation/brand-a'''

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
