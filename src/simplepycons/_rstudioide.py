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


class RstudioIdeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "rstudioide"

    @property
    def original_file_name(self) -> "str":
        return "rstudioide.svg"

    @property
    def title(self) -> "str":
        return "RStudio IDE"

    @property
    def primary_color(self) -> "str":
        return "#75AADB"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>RStudio IDE</title>
     <path d="M12.178.002a12.002 12.002 0 0 0-8.662 3.515 12.002
 12.002 0 0 0 0 16.97 12.002 12.002 0 0 0 16.97 0 12.002 12.002 0 0 0
 0-16.97A12.002 12.002 0 0 0 12.179.002zM7.77 5.995c.562.128 1.05.217
 1.663.217.921 0 1.863-.217 2.786-.217 1.79 0 3.45.814 3.45 2.8 0
 1.54-.921 2.517-2.35 2.93l2.788
 4.107h1.301v1.01h-1.986l-3.293-4.934h-1.757v3.924h1.718v1.01H7.77v-1.01h1.483V7.134L7.77
 6.951v-.957zm4.466 1.012c-.596
 0-1.213.053-1.864.127v3.798l.941.02c2.298.034 3.183-.85 3.183-2.026
 0-1.376-.997-1.919-2.26-1.919z" />
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
