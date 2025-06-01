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


class NederlandseSpoorwegenIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nederlandsespoorwegen"

    @property
    def original_file_name(self) -> "str":
        return "nederlandsespoorwegen.svg"

    @property
    def title(self) -> "str":
        return "Nederlandse Spoorwegen"

    @property
    def primary_color(self) -> "str":
        return "#003082"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Nederlandse Spoorwegen</title>
     <path d="M10.494 11.812a2.602 2.602 0 0 0-1.835-.751H3.576L5.46
 9.184h4.753a.757.757 0 0 1 .516.234l2.777 2.77a2.602 2.602 0 0 0
 1.835.75h5.084l-1.884 1.878h-4.752a.757.757 0 0 1-.516-.235zm1.459
 4.083a2.863 2.863 0 0 0 1.835.798h5.506L24
 12l-4.706-4.694H16.66l3.764 3.755h-5.082a.99.99 0 0
 1-.516-.188l-2.778-2.769a2.863 2.863 0 0 0-1.835-.798H4.706L0
 12l4.706 4.693H7.34L3.577 12.94h5.082a.99.99 0 0 1 .516.187z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.ns.nl/platform/fundamentals/icons'''

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
