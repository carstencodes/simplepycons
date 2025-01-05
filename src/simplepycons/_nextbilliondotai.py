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


class NextbilliondotaiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "nextbilliondotai"

    @property
    def original_file_name(self) -> "str":
        return "nextbilliondotai.svg"

    @property
    def title(self) -> "str":
        return "NextBillion.ai"

    @property
    def primary_color(self) -> "str":
        return "#8D5A9E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>NextBillion.ai</title>
     <path d="M22.399 13.3694a6.3067 6.3067 0 0 0-.5655-.567 6.3754
 6.3754 0 0 0-4.2337-1.5994h-4.7989V6.4007a6.3783 6.3783 0 0
 0-1.5993-4.2338 6.1066 6.1066 0 0 0-.567-.5641A6.3973 6.3973 0 0 0
 .002 6.4016v4.7989a1.5994 1.5994 0 0 0 1.5993
 1.5993h9.5959v4.7989a6.3696 6.3696 0 0 0 .855
 3.1985l.0842.1453a6.3445 6.3445 0 0 0 .6615.8942 6.6637 6.6637 0 0 0
 .5641.5641 6.4689 6.4689 0 0 0 .8913.6586l.1453.0858a6.4074 6.4074 0
 0 0 7.4324-.7444 6.6963 6.6963 0 0 0 .5655-.5655 6.3973 6.3973 0 0 0
 0-8.4677zm-11.198-2.1708H1.6052v-4.799a4.7989 4.7989 0 0 1 9.5958
 0zm6.3965 11.1951a4.7703 4.7703 0 0 1-3.1986-1.2243 4.1977 4.1977 0 0
 1-.378-.3766 4.782 4.782 0 0 1-1.2211-3.1985v-4.7964h4.7988a4.7989
 4.7989 0 0 1 0 9.5958z" />
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
