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


class UdemyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "udemy"

    @property
    def original_file_name(self) -> "str":
        return "udemy.svg"

    @property
    def title(self) -> "str":
        return "Udemy"

    @property
    def primary_color(self) -> "str":
        return "#A435F0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Udemy</title>
     <path d="M12 0L5.81 3.573v3.574l6.189-3.574 6.191
 3.574V3.573zM5.81 10.148v8.144c0 1.85.589 3.243 1.741 4.234S10.177 24
 11.973 24s3.269-.482 4.448-1.474c1.179-.991 1.768-2.439
 1.768-4.314v-8.064h-3.242v7.85c0 2.036-1.509 3.055-2.948 3.055-1.428
 0-2.947-.991-2.947-3.027v-7.878z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://support.udemy.com/hc/en-us/articles/8'''
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
