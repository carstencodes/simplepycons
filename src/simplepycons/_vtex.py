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


class VtexIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vtex"

    @property
    def original_file_name(self) -> "str":
        return "vtex.svg"

    @property
    def title(self) -> "str":
        return "VTEX"

    @property
    def primary_color(self) -> "str":
        return "#ED125F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>VTEX</title>
     <path d="M22.2027 1.7925H4.2812c-1.3897 0-2.2795 1.4698-1.6293
 2.6917l1.7927 3.3773H1.1947a1.2 1.2 0 0 0-.5873.1537 1.1924 1.1924 0
 0 0-.4356.421 1.1847 1.1847 0 0 0-.0342 1.1683l5.766
 10.858c.1017.191.2537.3507.4399.4622a1.1996 1.1996 0 0 0 1.2326 0
 1.1913 1.1913 0 0 0 .4398-.4623l1.566-2.933 1.9647 3.7006c.6914
 1.3016 2.5645 1.304 3.2584.0038L23.7878
 4.416c.635-1.1895-.2314-2.6235-1.5851-2.6235ZM14.1524 8.978l-3.8733
 7.2533a.7932.7932 0 0 1-.2927.3074.7986.7986 0 0 1-.82 0 .7933.7933 0
 0 1-.2927-.3074L5.0378 9.0086a.7883.7883 0 0 1 .0208-.7776.7933.7933
 0 0 1 .2891-.281.7985.7985 0 0 1 .3906-.1033h7.7307a.7769.7769 0 0 1
 .381.0998.7717.7717 0 0 1 .2823.2736.7672.7672 0 0 1 .02.758z" />
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
