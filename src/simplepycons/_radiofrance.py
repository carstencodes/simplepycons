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


class RadioFranceIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "radiofrance"

    @property
    def original_file_name(self) -> "str":
        return "radiofrance.svg"

    @property
    def title(self) -> "str":
        return "Radio France"

    @property
    def primary_color(self) -> "str":
        return "#2B00E7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Radio France</title>
     <path d="M12 24C6.144 24 1.397 19.497 1.397 13.94a9.6 9.6 0 0 1
 .208-1.991h5.99a4.4 4.4 0 0 0-.474 1.991c0 2.557 2.184 4.63 4.88
 4.63.6 0 1.175-.104 1.706-.292v5.592Q12.872 24 12
 24m10.355-7.888H16.31a4.4 4.4 0 0 0
 .57-2.172c0-2.557-2.184-4.63-4.879-4.63-.504
 0-.99.073-1.448.208V0h5.25v4.546c3.978 1.45 6.802 5.109 6.802
 9.394a9.6 9.6 0 0 1-.249 2.172" />
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
