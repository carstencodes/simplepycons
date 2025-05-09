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


class InformaticaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "informatica"

    @property
    def original_file_name(self) -> "str":
        return "informatica.svg"

    @property
    def title(self) -> "str":
        return "Informatica"

    @property
    def primary_color(self) -> "str":
        return "#FF4D00"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Informatica</title>
     <path d="M12 0l3.547 10.788-4.5-1.255-.25 4.43 7.121
 4.035V18h.001l5.919-6zm-.64.65L.162 12l6.32 6.407L12
 24l5.184-5.255-9.736-3.856z" />
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
