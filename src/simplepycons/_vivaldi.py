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


class VivaldiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vivaldi"

    @property
    def original_file_name(self) -> "str":
        return "vivaldi.svg"

    @property
    def title(self) -> "str":
        return "Vivaldi"

    @property
    def primary_color(self) -> "str":
        return "#EF3939"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Vivaldi</title>
     <path d="M12 0C6.75 0 3.817 0 1.912 1.904.007 3.81 0 6.75 0 12s0
 8.175 1.912 10.08C3.825 23.985 6.75 24 12 24c5.25 0 8.183 0
 10.088-1.904C23.993 20.19 24 17.25 24
 12s0-8.175-1.912-10.08C20.175.015 17.25 0 12 0zm-.168 3a9 9 0 016.49
 2.648 9 9 0 010 12.704A9 9 0 1111.832 3zM7.568 7.496a1.433 1.433 0
 00-.142.004A1.5 1.5 0 006.21 9.75l1.701 3c.93 1.582 1.839 3.202 2.791
 4.822a1.417 1.417 0 001.41.75 1.5 1.5 0 001.223-.81l4.447-7.762A1.56
 1.56 0 0018 8.768a1.5 1.5 0 10-2.828.914 2.513 2.513 0 01.256
 1.119v.246a2.393 2.393 0 01-2.52 2.13 2.348 2.348 0
 01-1.965-1.214c-.307-.51-.6-1.035-.9-1.553-.42-.72-.826-1.41-1.246-2.16a1.433
 1.433 0 00-1.229-.754Z" />
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
