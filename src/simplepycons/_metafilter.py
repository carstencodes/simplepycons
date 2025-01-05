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


class MetafilterIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "metafilter"

    @property
    def original_file_name(self) -> "str":
        return "metafilter.svg"

    @property
    def title(self) -> "str":
        return "MetaFilter"

    @property
    def primary_color(self) -> "str":
        return "#065A8F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MetaFilter</title>
     <path d="M18.548 5.26l-.87 4.894h3.558l-.519 2.83h-3.592l-1.602
 8.639h-2.857l3.586-19.248H24l-.537 2.885h-4.915zm-7.331-2.884L7.19
 13.472V2.376H3.581L0 21.624h2.452L5.198 6.728l-.251
 14.896h1.421l5.225-14.896-2.786 14.896h2.48l3.581-19.248h-3.651z" />
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
