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


class EducativeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "educative"

    @property
    def original_file_name(self) -> "str":
        return "educative.svg"

    @property
    def title(self) -> "str":
        return "Educative"

    @property
    def primary_color(self) -> "str":
        return "#4951F5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Educative</title>
     <path d="M20 0H4a4 4 0 0 0-4 4v16a4 4 0 0 0 3.998 4h16A4 4 0 0 0
 24 20V4a4 4 0 0 0-4-4ZM5.397 19.576l-1.828-1.673a.316.316 0 0
 1-.018-.445l4.004-4.376a.314.314 0 0 0 .009-.415L3.82 8.217a.315.315
 0 0 1 .038-.443l1.893-1.595a.315.315 0 0 1 .443.038l5.495
 6.537a.316.316 0 0 1-.008.417L5.84 19.559a.315.315 0 0
 1-.442.018zm15.147-.102c0 .174-.141.315-.315.315H11.74a.315.315 0 0
 1-.314-.315v-2.332c0-.174.14-.315.314-.315h8.488c.174 0
 .315.14.315.315z" />
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
