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


class MaasIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "maas"

    @property
    def original_file_name(self) -> "str":
        return "maas.svg"

    @property
    def title(self) -> "str":
        return "MAAS"

    @property
    def primary_color(self) -> "str":
        return "#E95420"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MAAS</title>
     <path d="M12 0C5.383 0 0 5.384 0 12s5.383 12 12 12 12-5.384
 12-12S18.617 0 12 0zM6.343 6.257h11.314c.284 0 .514.23.514.515v.685c0
 .285-.23.515-.514.515H6.343a.515.515 0 0
 1-.515-.515v-.685c0-.284.23-.515.515-.515zm0 3.257h11.314c.284 0
 .514.23.514.515v.685c0 .285-.23.515-.514.515H6.343a.515.515 0 0
 1-.515-.515v-.685c0-.284.23-.515.515-.515zm0 3.257h11.314c.284 0
 .514.23.514.515v.685c0 .285-.23.515-.514.515H6.343a.515.515 0 0
 1-.514-.515v-.685c0-.284.23-.515.514-.515zm0 3.258h11.314c.284 0
 .514.23.514.513v.687c0 .284-.23.515-.514.515H6.343a.515.515 0 0
 1-.514-.515v-.687c0-.284.23-.513.514-.513z" />
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
