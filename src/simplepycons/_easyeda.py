#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class EasyedaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "easyeda"

    @property
    def original_file_name(self) -> "str":
        return "easyeda.svg"

    @property
    def title(self) -> "str":
        return "EasyEDA"

    @property
    def primary_color(self) -> "str":
        return "#1765F6"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>EasyEDA</title>
     <path d="M13.31 3.108a7.67 7.67 0 0 0-3.015.545 7.67 7.67 0 0
 0-1.73.951 7.865 7.865 0 0 0-1.59 1.567 6.308 6.308 0 0
 0-.764-.047C2.78 6.124 0 8.91 0 12.35a6.217 6.217 0 0 0 4.146 5.868
 3.759 3.759 0 0 0
 7.326-1.574l5.3-2.673-.04-.078.499-.257-1.021-2.027-.499.25-.047-.086-5.291
 2.658a3.727 3.727 0 0 0-2.627-1.076 3.77 3.77 0 0 0-3.42 2.198 3.723
 3.723 0 0 1-1.7-4.146 3.71 3.71 0 0 1 5.549-2.214 5.211 5.211 0 0 1
 6.585-3.32 5.24 5.24 0 0 1 3.538 4.373 2.913 2.913 0 0 1 3.188 2.899
 2.909 2.909 0 0 1-2.65 2.899h-2.135v2.517h2.244l.11-.016a5.407 5.407
 0 0 0 4.925-5.852 5.459 5.459 0 0 0-1.574-3.375A5.355 5.355 0 0 0
 20.3 8.01a7.725 7.725 0 0 0-6.99-4.901ZM7.748 15.367c.965 0 1.753.791
 1.753 1.761a1.748 1.748 0 0 1-1.753 1.753 1.748 1.748 0 0
 1-1.754-1.753 1.756 1.756 0 0 1 1.754-1.753Z" />
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
