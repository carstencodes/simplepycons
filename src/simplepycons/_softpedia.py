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


class SoftpediaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "softpedia"

    @property
    def original_file_name(self) -> "str":
        return "softpedia.svg"

    @property
    def title(self) -> "str":
        return "Softpedia"

    @property
    def primary_color(self) -> "str":
        return "#002873"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Softpedia</title>
     <path d="M1.88 18.093V24c4.526 0 9.959-.326 13.765-1.628a14.698
 14.698 0 0 0 2.708-1.23c1.255-.752 2.208-1.668
 2.844-2.763.317-.533.559-1.107.725-1.709l.197-1.723c0-.63-.09-1.23-.257-1.819a6.72
 6.72 0 0 0-.696-1.531c-.484-.78-1.165-1.45-2.012-2.024a12.187 12.187
 0 0
 0-1.95-.999c-1.722-.642-4.38-1.295-5.356-1.654-.882-.294-1.784-.738-1.784-1.012H20.59V0H10.11C7.522
 0 5.677 1.148 4.573 3.46c-1.18 2.461-.741 4.704 1.286 6.714.56.561
 1.24 1.053 2.042 1.477.862.452 2.072.903 3.615 1.34 1.664.493
 2.465.712 2.374.684.56.178 1 .342
 1.332.493l.62.328c.272.191.332.506.18.957-.165.22-.437.452-.8.67-.938.574-2.375
 1.026-4.311 1.34-2.39.424-5.4.63-9.03.63z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Softp'''

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
