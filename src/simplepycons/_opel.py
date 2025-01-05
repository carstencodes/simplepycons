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


class OpelIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "opel"

    @property
    def original_file_name(self) -> "str":
        return "opel.svg"

    @property
    def title(self) -> "str":
        return "Opel"

    @property
    def primary_color(self) -> "str":
        return "#F7FF14"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Opel</title>
     <path d="M12.291 4.57a7.46 7.46 0 0 0-7.338 5.006h.568a6.926
 6.926 0 0 1 6.483-4.494 6.922 6.922 0 0 1 6.922 6.924c0 .116 0
 .234-.01.351l.533.059c0-.134.01-.273.01-.4a7.46 7.46 0 0
 0-7.168-7.446zM.869 10.113 0 10.566l13.25 1.44 3.63-1.893H.87zm3.682
 1.483v.41a7.46 7.46 0 0 0 14.498 2.441h-.57a6.924 6.924 0 0 1-6.475
 4.487 6.928 6.928 0 0 1-6.92-6.928v-.352l-.533-.058zm6.193.414-3.63
 1.898h16.011l.873-.453v-.006l-13.254-1.44zm13.254
 1.44H24l-.002-.007v.006z" />
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
