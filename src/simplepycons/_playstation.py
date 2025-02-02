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


class PlaystationIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "playstation"

    @property
    def original_file_name(self) -> "str":
        return "playstation.svg"

    @property
    def title(self) -> "str":
        return "PlayStation"

    @property
    def primary_color(self) -> "str":
        return "#0070D1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PlayStation</title>
     <path d="M8.984 2.596v17.547l3.915
 1.261V6.688c0-.69.304-1.151.794-.991.636.18.76.814.76
 1.505v5.875c2.441 1.193 4.362-.002 4.362-3.152
 0-3.237-1.126-4.675-4.438-5.827-1.307-.448-3.728-1.186-5.39-1.502zm4.656
 16.241l6.296-2.275c.715-.258.826-.625.246-.818-.586-.192-1.637-.139-2.357.123l-4.205
 1.5V14.98l.24-.085s1.201-.42 2.913-.615c1.696-.18 3.785.03 5.437.661
 1.848.601 2.04 1.472 1.576 2.072-.465.6-1.622 1.036-1.622
 1.036l-8.544 3.107V18.86zM1.807
 18.6c-1.9-.545-2.214-1.668-1.352-2.32.801-.586 2.16-1.052
 2.16-1.052l5.615-2.013v2.313L4.205
 17c-.705.271-.825.632-.239.826.586.195 1.637.15 2.343-.12L8.247
 17v2.074c-.12.03-.256.044-.39.073-1.939.331-3.996.196-6.038-.479z" />
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
