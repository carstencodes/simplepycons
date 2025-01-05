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


class WakatimeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wakatime"

    @property
    def original_file_name(self) -> "str":
        return "wakatime.svg"

    @property
    def title(self) -> "str":
        return "WakaTime"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>WakaTime</title>
     <path d="M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12 12-5.373
 12-12S18.627 0 12 0zm0 2.824a9.176 9.176 0 1 1 0 18.352 9.176 9.176 0
 0 1 0-18.352zm5.097 5.058c-.327 0-.61.19-.764.45-1.025 1.463-2.21
 3.162-3.288 4.706l-.387-.636a.897.897 0 0 0-.759-.439.901.901 0 0
 0-.788.492l-.357.581-1.992-2.943a.897.897 0 0 0-.761-.446c-.514
 0-.903.452-.903.96a1 1 0 0 0 .207.61l2.719
 3.96c.152.272.44.47.776.47a.91.91 0 0 0
 .787-.483c.046-.071.23-.368.314-.504l.324.52c-.035-.047.076.113.087.13.024.031.054.059.078.085.019.019.04.036.058.052.036.033.08.056.115.08.025.016.052.028.076.04.029.015.06.024.088.035.058.025.122.027.18.04.031.004.064.003.092.005.29
 0 .546-.149.707-.36 1.4-2 2.842-4.055 4.099-5.849A.995.995 0 0 0 18
 8.842c0-.508-.389-.96-.903-.96" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://wakatime.com/legal/logos-and-trademar'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://wakatime.com/legal/logos-and-trademar'''

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
