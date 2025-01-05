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


class NpmIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "npm"

    @property
    def original_file_name(self) -> "str":
        return "npm.svg"

    @property
    def title(self) -> "str":
        return "npm"

    @property
    def primary_color(self) -> "str":
        return "#CB3837"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>npm</title>
     <path d="M1.763 0C.786 0 0 .786 0 1.763v20.474C0 23.214.786 24
 1.763 24h20.474c.977 0 1.763-.786 1.763-1.763V1.763C24 .786 23.214 0
 22.237 0zM5.13 5.323l13.837.019-.009
 13.836h-3.464l.01-10.382h-3.456L12.04 19.17H5.113z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://docs.npmjs.com/policies/logos-and-usa'''
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
