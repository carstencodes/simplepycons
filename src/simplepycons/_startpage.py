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


class StartpageIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "startpage"

    @property
    def original_file_name(self) -> "str":
        return "startpage.svg"

    @property
    def title(self) -> "str":
        return "Startpage"

    @property
    def primary_color(self) -> "str":
        return "#6563FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Startpage</title>
     <path d="m16.885 14.254.04-.06a8.723 8.723 0 0 0
 1.851-4.309c-1.334 0-2.648 0-3.982.04a4.901 4.901 0 0 1-4.758 3.696
 4.948 4.948 0 0 1-4.56-3.044 89.632 89.632 0 0 0-3.941.514c1.035
 3.697 4.46 6.405 8.501 6.405a8.76 8.76 0 0 0 3.743-.83l.06-.02.04.04
 5.455 6.603c.378.454.916.711 1.513.711.458 0 .896-.158
 1.234-.435.399-.336.657-.79.697-1.304.04-.514-.1-1.009-.438-1.424zM5.118
 8.56c.1-2.59 2.27-4.685 4.918-4.685a4.911 4.911 0 0 1 4.898
 4.389c1.314.02 2.608.04 3.922.099C18.616 3.717 14.754 0 10.036
 0c-4.858 0-8.82 3.934-8.82 8.758v.178a86.7 86.7 0 0 1 3.902-.376z" />
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
