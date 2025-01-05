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


class ZedIndustriesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zedindustries"

    @property
    def original_file_name(self) -> "str":
        return "zedindustries.svg"

    @property
    def title(self) -> "str":
        return "Zed Industries"

    @property
    def primary_color(self) -> "str":
        return "#084CCF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Zed Industries</title>
     <path d="M2.25 1.5a.75.75 0 0 0-.75.75v16.5H0V2.25A2.25 2.25 0 0
 1 2.25 0h20.095c1.002 0 1.504 1.212.795 1.92L10.764
 14.298h3.486V12.75h1.5v1.922a1.125 1.125 0 0 1-1.125
 1.125H9.264l-2.578 2.578h11.689V9h1.5v9.375a1.5 1.5 0 0 1-1.5
 1.5H5.185L2.562 22.5H21.75a.75.75 0 0 0 .75-.75V5.25H24v16.5A2.25
 2.25 0 0 1 21.75 24H1.655C.653 24 .151 22.788.86 22.08L13.19
 9.75H9.75v1.5h-1.5V9.375A1.125 1.125 0 0 1 9.375
 8.25h5.314l2.625-2.625H5.625V15h-1.5V5.625a1.5 1.5 0 0 1
 1.5-1.5h13.19L21.438 1.5z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/zed-industries/zed/blob/cc'''

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
