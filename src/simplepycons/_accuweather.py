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


class AccuweatherIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "accuweather"

    @property
    def original_file_name(self) -> "str":
        return "accuweather.svg"

    @property
    def title(self) -> "str":
        return "AccuWeather"

    @property
    def primary_color(self) -> "str":
        return "#FF6600"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AccuWeather</title>
     <path d="M6.74 6.772a7.436 7.436 0 0 1 10.519 0 7.432 7.432 0 0 1
 0 10.515 7.436 7.436 0 0 1-10.52 0c-2.904-2.905-2.904-7.64
 0-10.515M12 20.337c-4.59 0-8.338-3.747-8.338-8.337s3.748-8.308
 8.338-8.308c4.591 0 8.31 3.748 8.31 8.308 0 4.619-3.719 8.337-8.31
 8.337zm12-8.366L21.27 9.5l1.103-3.514-3.603-.784-.784-3.602-3.515
 1.133L11.97.004l-2.47 2.73L5.986 1.63 5.2 5.231l-3.602.785 1.133
 3.515L0 12.03l2.732 2.47-1.105 3.514 3.603.784.784 3.603 3.516-1.134
 2.5 2.731 2.468-2.73 3.516 1.103.785-3.602 3.603-.813-1.134-3.515L24
 11.97z" />
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
