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


class CastroIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "castro"

    @property
    def original_file_name(self) -> "str":
        return "castro.svg"

    @property
    def title(self) -> "str":
        return "Castro"

    @property
    def primary_color(self) -> "str":
        return "#00B265"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Castro</title>
     <path d="M12 0C5.372 0 0 5.373 0 12s5.372 12 12 12c6.627 0
 12-5.373 12-12S18.627 0 12 0zm-.002 13.991a2.052 2.052 0 1 1 0-4.105
 2.052 2.052 0 0 1 0 4.105zm4.995 4.853l-2.012-2.791a5.084 5.084 0 1
 0-5.982.012l-2.014 2.793A8.526 8.526 0 0 1 11.979 3.42a8.526 8.526 0
 0 1 8.526 8.526 8.511 8.511 0 0 1-3.512 6.898z" />
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
