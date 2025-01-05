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


class ClubforceIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "clubforce"

    @property
    def original_file_name(self) -> "str":
        return "clubforce.svg"

    @property
    def title(self) -> "str":
        return "Clubforce"

    @property
    def primary_color(self) -> "str":
        return "#191176"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Clubforce</title>
     <path d="M1.4 0C.624 0 0 .624 0 1.4v21.2c0 .776.624 1.4 1.4
 1.4h21.2c.776 0 1.4-.624 1.4-1.4V1.4c0-.776-.624-1.4-1.4-1.4Zm4.778
 5.5h9.61l-2.83 2.112H8.331v3.472L6.18 12.72V5.5Zm11.644
 1.317v7.415L11.96 18.5l-4.786-3.629 1.675-1.317 3.111 2.354
 3.19-2.392-3.23-2.234 1.834-1.355 1.955 1.355v-2.87Z" />
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
