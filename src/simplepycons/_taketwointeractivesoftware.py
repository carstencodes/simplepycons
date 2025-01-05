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


class TaketwoInteractiveSoftwareIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "taketwointeractivesoftware"

    @property
    def original_file_name(self) -> "str":
        return "taketwointeractivesoftware.svg"

    @property
    def title(self) -> "str":
        return "Take-Two Interactive Software"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Take-Two Interactive Software</title>
     <path d="m17.012 16.776.417-.257 4.155-3.1c1.413-1.248
 2.293-2.686 2.293-4.607-.006-3.849-3.037-5.771-6.614-5.771-1.663
 0-3.122.447-4.283 1.256V2.852L0 2.86l.007 4.395 3.85-.008.016 13.886
 5.355-.008-.016-13.886h1.443a7.97 7.97 0 0 0-.516
 2.02l4.518.884c.076-1.376.547-3.102 2.219-3.102 1.101 0 1.753.832
 1.753 1.87 0 1.557-1.305 2.653-2.4 3.592l-6.082 4.56.006 4.085
 13.642-.016.205-4.371-6.988.015Z" />
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
