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


class IfoodIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ifood"

    @property
    def original_file_name(self) -> "str":
        return "ifood.svg"

    @property
    def title(self) -> "str":
        return "iFood"

    @property
    def primary_color(self) -> "str":
        return "#EA1D2C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>iFood</title>
     <path d="M8.428 1.67c-4.65 0-7.184 4.149-7.184 6.998 0 2.294 2.2
 3.299 4.25 3.299l-.006-.006c4.244 0 7.184-3.854 7.184-6.998
 0-2.29-2.175-3.293-4.244-3.293zm11.328 0c-4.65 0-7.184 4.149-7.184
 6.998 0 2.294 2.2 3.299 4.25 3.299l-.006-.006C21.061 11.96 24 8.107
 24 4.963c0-2.29-2.18-3.293-4.244-3.293zM14.172 14.52l2.435
 1.834c-2.17 2.07-6.124 3.525-9.353 3.17A8.913 8.913 0 01.23
 14.541H0a9.598 9.598 0 008.828 7.758c3.814.24 7.323-.905
 9.947-3.13l-.004.007 1.08 2.988 1.555-7.623-7.234-.02Z" />
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
