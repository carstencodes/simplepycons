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


class KongregateIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "kongregate"

    @property
    def original_file_name(self) -> "str":
        return "kongregate.svg"

    @property
    def title(self) -> "str":
        return "Kongregate"

    @property
    def primary_color(self) -> "str":
        return "#F04438"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Kongregate</title>
     <path d="M2.667 0A2.667 2.667 0 0 0 0 2.667v18.666A2.667 2.667 0
 0 0 2.667 24h18.666A2.667 2.667 0 0 0 24 21.333V2.667A2.667 2.667 0 0
 0 21.333 0ZM5.6 5.333h2.667v5.334H13.6v2.666H8.267v5.334H5.6Zm8
 8h1.678a1.6 1.6 0 0 1 1.43.885L17.6 16h1.333v2.667h-2.666zm0-2.666
 2.667-5.334h2.666V8H17.6l-.891 1.782a1.6 1.6 0 0 1-1.431.885z" />
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
