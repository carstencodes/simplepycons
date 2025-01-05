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


class LydiaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "lydia"

    @property
    def original_file_name(self) -> "str":
        return "lydia.svg"

    @property
    def title(self) -> "str":
        return "Lydia"

    @property
    def primary_color(self) -> "str":
        return "#0180FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Lydia</title>
     <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373
 12-12S18.627 0 12 0zm5.895 17.611a.421.421 0
 01-.168.035h-1.155a.608.608 0 01-.56-.377l-4-9.613-3.991 9.607a.61.61
 0 01-.56.377H6.273a.42.42 0 01-.385-.59L10.91 5.575a.793.793 0
 01.726-.475h.748a.792.792 0 01.726.48l5.003 11.482a.42.42 0
 01-.218.549z" />
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
