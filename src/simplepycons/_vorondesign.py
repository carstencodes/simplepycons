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


class VoronDesignIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vorondesign"

    @property
    def original_file_name(self) -> "str":
        return "vorondesign.svg"

    @property
    def title(self) -> "str":
        return "Voron Design"

    @property
    def primary_color(self) -> "str":
        return "#ED3023"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Voron Design</title>
     <path d="M12 0 1.6078 6v12L12 24l10.3922-6V6L12.0001 0zM8.3242
 5.3765h3L7.5 12.0001h-3l3.8241-6.6236zm6 0h3L9.676
 18.6235h-3l7.6482-13.247zm2.176 6.6236h3l-3.8242 6.6235h-3L16.5 12z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/VoronDesign/Voron-Extras/b
lob/d8591f964b408b3da21b6f9b4ab0437e229065de/Images/Logo/SVG/Voron_Des'''

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
