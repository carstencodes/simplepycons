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


class LetterboxdIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "letterboxd"

    @property
    def original_file_name(self) -> "str":
        return "letterboxd.svg"

    @property
    def title(self) -> "str":
        return "Letterboxd"

    @property
    def primary_color(self) -> "str":
        return "#202830"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Letterboxd</title>
     <path d="M8.224 14.352a4.447 4.447 0 0 1-3.775 2.092C1.992 16.444
 0 14.454 0 12s1.992-4.444 4.45-4.444c1.592 0 2.988.836 3.774
 2.092-.427.682-.673 1.488-.673 2.352s.246 1.67.673 2.352zM15.101
 12c0-.864.247-1.67.674-2.352-.786-1.256-2.183-2.092-3.775-2.092s-2.989.836-3.775
 2.092c.427.682.674 1.488.674 2.352s-.247 1.67-.674 2.352c.786 1.256
 2.183 2.092 3.775 2.092s2.989-.836 3.775-2.092A4.42 4.42 0 0 1 15.1
 12zm4.45-4.444a4.447 4.447 0 0 0-3.775 2.092c.427.682.673 1.488.673
 2.352s-.246 1.67-.673 2.352a4.447 4.447 0 0 0 3.775 2.092C22.008
 16.444 24 14.454 24 12s-1.992-4.444-4.45-4.444z" />
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
