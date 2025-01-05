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


class FastlyIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "fastly"

    @property
    def original_file_name(self) -> "str":
        return "fastly.svg"

    @property
    def title(self) -> "str":
        return "Fastly"

    @property
    def primary_color(self) -> "str":
        return "#FF282D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Fastly</title>
     <path d="M13.919 3.036V1.3h.632V0H9.377v1.3h.631v1.749a10.572
 10.572 0 00-8.575 10.384C1.433 19.275 6.17 24 12 24c5.842 0
 10.567-4.737 10.567-10.567 0-5.186-3.729-9.486-8.648-10.397zm-1.628
 15.826v-.607h-.619v.607c-2.757-.158-4.955-2.38-5.101-5.137h.607v-.62h-.607a5.436
 5.436 0 015.101-5.089v.607h.62v-.607a5.435 5.435 0 015.137
 5.114h-.607v.619h.607a5.444 5.444 0 01-5.138
 5.113zm2.26-7.712l-.39-.389-1.979 1.725a.912.912 0 00-.316-.06c-.534
 0-.971.448-.971.995 0 .547.437.996.971.996.535 0
 .972-.45.972-.996a.839.839 0 00-.049-.304Z" />
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
