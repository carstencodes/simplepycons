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


class DlnaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dlna"

    @property
    def original_file_name(self) -> "str":
        return "dlna.svg"

    @property
    def title(self) -> "str":
        return "DLNA"

    @property
    def primary_color(self) -> "str":
        return "#48A842"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>DLNA</title>
     <path d="M23.255 12.667H13.02c-1.052 0-2.1.489-2.693
 1.266v-.017a3.24 3.24 0 01-2.629 1.353 3.25 3.25 0 010-6.502c1.085 0
 2.04.536 2.63 1.353v-.013c.591.776 1.64 1.273 2.692
 1.273h10.129c.186-.005.873-.095.848-.981-.884-5.086-5.88-8.987-11.923-8.987-3.722
 0-7.048 1.48-9.263 3.803-.356.527.014.689.35.734H9.77c1.05 0 2.1-.498
 2.692-1.277v.018a3.242 3.242 0 012.63-1.355 3.252 3.252 0 010 6.503
 3.24 3.24 0
 01-2.63-1.355v.019c-.592-.78-1.642-1.266-2.692-1.266H2.55l.028.003s-1.068-.06-1.719.859C.361
 8.9 0 10.62 0 12.002c0 1.388.198 2.65.867 3.923.564.908 1.71.85
 1.71.85l-.042.005h7.233c1.05 0 2.1-.49 2.692-1.268v.02a3.242 3.242 0
 012.63-1.356 3.251 3.251 0 010 6.502 3.242 3.242 0
 01-2.63-1.354v.018c-.592-.779-1.642-1.277-2.692-1.277H3.164c-.328.042-.698.198-.379.7
 2.216 2.336 5.555 3.823 9.289 3.823 6.054 0 11.056-3.91
 11.926-9.009-.004-.713-.489-.877-.745-.912" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:DLNA_'''

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
