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


class VintedIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vinted"

    @property
    def original_file_name(self) -> "str":
        return "vinted.svg"

    @property
    def title(self) -> "str":
        return "Vinted"

    @property
    def primary_color(self) -> "str":
        return "#007782"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Vinted</title>
     <path d="M19.316 0c-.258
 0-.571.217-1.415.953-.3.108-.627.027-1.008.613-2.15 3.09-3.825
 14.648-5.255
 17.984-.286-1.444-.885-10.837-1.116-13.41-.028-.477.027-1.076.027-1.43
 0-2.368-.516-3.567-2.886-3.567-1.198 0-2.382.436-3.008
 1.226-.299.408-.409.708-.409 1.443 0 4.915 1.171 12.973 2.478
 18.228C7.132 23.688 8.603 24 9.99 24c.654 0 1.307-.081 2.233-.544
 3.212-1.567 4.07-5.84 4.9-9.993.15-.749.899-4.37 1.253-6.275.476-2.6
 1.02-5.54 1.347-6.617C19.833.245 19.63 0 19.317 0z" />
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
