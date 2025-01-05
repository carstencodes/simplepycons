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


class OpenlayersIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "openlayers"

    @property
    def original_file_name(self) -> "str":
        return "openlayers.svg"

    @property
    def title(self) -> "str":
        return "Openlayers"

    @property
    def primary_color(self) -> "str":
        return "#1F6B75"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Openlayers</title>
     <path d="M23.7 13.08a3.498 3.498 0 0 1-1.119 1.619l-7.426
 6.196a5.137 5.137 0 0 1-6.317 0L1.412 14.7a3.578 3.578 0 0
 1-1.12-1.62 3.298 3.298 0 0 0 1.12 3.639l7.426 6.196a5.137 5.137 0 0
 0 6.317 0l7.426-6.196a3.298 3.298 0 0 0 1.12-3.639M8.838 1.086a5.137
 5.137 0 0 1 6.317 0l7.426 6.196a3.298 3.298 0 0 1 0 5.258l-7.426
 6.187a5.137 5.137 0 0 1-6.317 0L1.412 12.53a3.298 3.298 0 0 1
 0-5.248z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/openlayers/openlayers.gith'''

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
