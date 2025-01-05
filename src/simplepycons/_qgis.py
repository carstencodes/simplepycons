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


class QgisIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "qgis"

    @property
    def original_file_name(self) -> "str":
        return "qgis.svg"

    @property
    def title(self) -> "str":
        return "Qgis"

    @property
    def primary_color(self) -> "str":
        return "#589632"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Qgis</title>
     <path d="M12.879 13.006v3.65l-3.004-3.048v-3.495h3.582l2.852
 2.893h-3.43zm10.886 7.606V24h-3.654l-5.73-5.9v-3.55h3.354l6.03
 6.062zm-10.828-1.448l3.372 3.371c-1.309.442-2.557.726-4.325.726C5.136
 23.26 0 18.243 0 11.565 0 4.92 5.136 0 11.984 0 18.864 0 24 4.952 24
 11.565c0 2.12-.523 4.076-1.457 5.759l-3.625-3.725a8.393 8.393 0 0 0
 .24-2.005c0-4.291-3.148-7.527-7.1-7.527-3.954 0-7.248 3.236-7.248
 7.527s3.33 7.6 7.247 7.6c.548 0 .661.017.88-.03z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.qgis.org/en/site/getinvolved/styl'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.qgis.org/en/site/getinvolved/styl'''

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
