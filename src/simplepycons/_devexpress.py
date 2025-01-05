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


class DevexpressIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "devexpress"

    @property
    def original_file_name(self) -> "str":
        return "devexpress.svg"

    @property
    def title(self) -> "str":
        return "DevExpress"

    @property
    def primary_color(self) -> "str":
        return "#FF7200"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>DevExpress</title>
     <path d="M1.4 0h21.2c.8 0 1.4.6 1.4 1.4v1.1c0 .8-.6 1-.9 1C11.7
 4.9 4.2 9.7 0 14.1V1.4C0 .6.6 0 1.4 0zm.022 19.567L1.7 19.2C5.3 14.6
 12.4 8.3 24 6.3v16.3c0 .8-.6 1.4-1.4 1.4H1.4C.6 24 0 23.4 0
 22.6v-.4c0-.3.2-.8.3-.9.252-.589.646-1.107 1.122-1.733z" />
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
