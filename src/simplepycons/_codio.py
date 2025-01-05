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


class CodioIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "codio"

    @property
    def original_file_name(self) -> "str":
        return "codio.svg"

    @property
    def title(self) -> "str":
        return "Codio"

    @property
    def primary_color(self) -> "str":
        return "#4574E0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Codio</title>
     <path d="M11.997 24L1.605 17.997v-12L12 0l10.396 5.997L16.5 9.402
 12 6.8 7.496 9.4v5.2l4.502 2.6 4.5-2.6 5.895 3.397L12.003 24h-.006z"
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
