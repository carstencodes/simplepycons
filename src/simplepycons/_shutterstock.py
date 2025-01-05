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


class ShutterstockIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "shutterstock"

    @property
    def original_file_name(self) -> "str":
        return "shutterstock.svg"

    @property
    def title(self) -> "str":
        return "Shutterstock"

    @property
    def primary_color(self) -> "str":
        return "#EE2B24"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Shutterstock</title>
     <path d="M9.839 18.761h5.313a1.53 1.53 0 0 0
 1.527-1.528v-5.76h5.237v5.76A6.767 6.767 0 0 1 15.152
 24H9.839v-5.239M14.16 5.237H8.85a1.53 1.53 0 0 0-1.53
 1.527v5.761H2.085V6.764A6.763 6.763 0 0 1 8.85 0h5.31v5.237Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://shutterstock.com/es/discover/brand-do'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://shutterstock.com/es/discover/brand-do'''

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
