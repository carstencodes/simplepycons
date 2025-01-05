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


class TutaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tuta"

    @property
    def original_file_name(self) -> "str":
        return "tuta.svg"

    @property
    def title(self) -> "str":
        return "Tuta"

    @property
    def primary_color(self) -> "str":
        return "#850122"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Tuta</title>
     <path d="m23.993 7.033-5.16 16.755-.043.12a.144.144 0 0
 1-.11.091H1.425a.14.14 0 0 1-.13-.191L6.441 6.98a.473.473 0 0 1
 .024-.076.134.134 0 0 1 .124-.091H23.82c.14 0 .202.086.173.22zM23.94
 4.25 19.885.146c-.178-.173-.192-.144-.384-.144H2.007a.14.14 0 0
 0-.14.14c0 .004-.004.061.044.114l.004.005L6
 4.393c.096.096.192.12.336.12h17.533c.12 0 .182-.153.072-.263zM4.127
 5.805.25 1.95c-.048-.043-.105-.038-.11-.038a.14.14 0 0
 0-.14.14v16.975c0 .077.063.14.14.14a.14.14 0 0 0
 .13-.092c.004-.005.004-.014.009-.024 0-.004.01-.038.01-.043L4.199
 6.164c.048-.144.048-.24-.072-.36z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/tutao/tutanota/blob/65d087'''

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
        yield from [
            "Tutanota",
        ]
