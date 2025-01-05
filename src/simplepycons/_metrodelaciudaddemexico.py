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


class MetroDeLaCiudadDeMexicoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "metrodelaciudaddemexico"

    @property
    def original_file_name(self) -> "str":
        return "metrodelaciudaddemexico.svg"

    @property
    def title(self) -> "str":
        return "Metro de la Ciudad de México"

    @property
    def primary_color(self) -> "str":
        return "#F77E1C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Metro de la Ciudad de México</title>
     <path d="M3.965 8.704V24H.008V6.864h2.097c1.066 0 1.86.774 1.86
 1.84m2.366-1.84c.268.521.521 1.315.521 1.84V24h3.685V8.704a1.784
 1.784 0 0 0-1.84-1.84M17.4 24V8.704a1.795 1.795 0 0
 0-1.844-1.84h-2.382c.269.521.269 1.315.269 1.84V24M.008
 3.953V0h15.549c4.75 0 8.435 3.953 8.435 8.704V24h-3.685V8.704a4.735
 4.735 0 0 0-4.75-4.75z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://es.wikipedia.org/wiki/Archivo:Metro_d'''

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
