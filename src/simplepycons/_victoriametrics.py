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


class VictoriametricsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "victoriametrics"

    @property
    def original_file_name(self) -> "str":
        return "victoriametrics.svg"

    @property
    def title(self) -> "str":
        return "VictoriaMetrics"

    @property
    def primary_color(self) -> "str":
        return "#621773"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>VictoriaMetrics</title>
     <path d="M1.893 3.078C.239 1.537 4.846.009 11.963
 0h.076c7.116.009 11.723 1.537 10.067 3.078 0 0-6.168 5.655-8.301
 7.473-.404.346-1.084.607-1.766.616h-.076c-.682-.009-1.362-.271-1.767-.616-2.132-1.818-8.301-7.473-8.303-7.473Zm20.549
 2.771V8.58c0 .3-.115.698-.319.885-1.332 1.222-6.47 5.925-8.319
 7.502-.405.345-1.085.606-1.767.615h-.072c-.683-.009-1.362-.27-1.767-.615-1.849-1.577-6.987-6.28-8.32-7.502-.204-.187-.318-.585-.318-.885V5.849c1.96
 1.788 7.163 6.505 8.638 7.764.404.346 1.084.607
 1.767.616h.072c.682-.009 1.362-.271 1.767-.616 1.474-1.258
 6.678-5.973 8.638-7.764Zm0 6.418v2.73c0 .301-.115.698-.319.885-1.332
 1.222-6.47 5.926-8.319
 7.502-.405.346-1.085.607-1.767.616h-.072c-.683-.009-1.362-.271-1.767-.616-1.849-1.576-6.987-6.28-8.32-7.502-.204-.187-.318-.585-.318-.885v-2.73c1.96
 1.788 7.163 6.505 8.638 7.764.404.346 1.084.606
 1.767.615h.072c.682-.009 1.362-.27 1.767-.615 1.474-1.258 6.678-5.976
 8.638-7.764Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://docs.victoriametrics.com/#victoriamet'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/VictoriaMetrics/VictoriaMe
trics/blob/24d61bf19374b42ef9839c13c7d35ce8888170e0/docs/assets/images'''

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
        yield from [
            "VM",
        ]
