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


class StackExchangeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "stackexchange"

    @property
    def original_file_name(self) -> "str":
        return "stackexchange.svg"

    @property
    def title(self) -> "str":
        return "Stack Exchange"

    @property
    def primary_color(self) -> "str":
        return "#1E5397"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Stack Exchange</title>
     <path d="M21.728 15.577v1.036c0 1.754-1.395 3.177-3.1
 3.177h-.904L13.645 24v-4.21H5.371c-1.704
 0-3.099-1.423-3.099-3.181v-1.032h19.456zM2.275
 10.463h19.323v3.979H2.275v-3.979zm0-5.141h19.323v3.979H2.275V5.322zM18.575
 0c1.681 0 3.023 1.42 3.023 3.178v1.034H2.275V3.178C2.275 1.422 3.67 0
 5.375 0h13.2z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://stackoverflow.com/legal/trademark-gui'''
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
