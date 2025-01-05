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


class CodemagicIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "codemagic"

    @property
    def original_file_name(self) -> "str":
        return "codemagic.svg"

    @property
    def title(self) -> "str":
        return "Codemagic"

    @property
    def primary_color(self) -> "str":
        return "#F45E3F"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Codemagic</title>
     <path d="M22.833 10.117L16.937
 7.24c-.07-.035-.106-.106-.142-.177l-2.912-5.896c-.498-1.03-1.776-1.457-2.807-.96a2.09
 2.09 0 0 0-.959.96L7.205 7.063a.81.81 0 0 1-.142.177l-5.896
 2.913c-1.03.497-1.457 1.776-.96 2.806a2.1 2.1 0 0 0 .96.96l5.896
 2.876c.07.036.106.107.142.142l2.948 5.896c.497 1.03 1.776 1.457
 2.806.96a2.09 2.09 0 0 0
 .959-.96l2.877-5.896c.036-.07.107-.142.142-.142l5.896-2.912c1.03-.498
 1.457-1.776.96-2.806-.178-.427-.533-.746-.96-.96zm-4.368.427l-2.735
 2.38c-.533.497-.924 1.136-1.066 1.847l-.71
 3.551c-.036.143-.178.25-.32.214-.071
 0-.107-.036-.142-.107l-2.38-2.735c-.497-.533-1.137-.923-1.847-1.066l-3.552-.71c-.142-.035-.249-.178-.213-.32
 0-.07.035-.106.106-.142l2.735-2.38c.533-.497.924-1.136
 1.066-1.847l.71-3.551c.036-.143.178-.25.32-.214a.27.27 0 0 1
 .142.071l2.38 2.735c.497.533 1.137.924 1.847
 1.066l3.552.71c.142.036.249.178.213.32a.38.38 0 0 1-.106.178z" />
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
