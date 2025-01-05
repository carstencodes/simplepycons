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


class KagiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "kagi"

    @property
    def original_file_name(self) -> "str":
        return "kagi.svg"

    @property
    def title(self) -> "str":
        return "Kagi"

    @property
    def primary_color(self) -> "str":
        return "#FFB319"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Kagi</title>
     <path d="M14.4829 18.392h-5.109c-1.3827
 0-1.6231-1.5076-1.3827-2.1106.1203-.3015.4208-.7236.6612-1.0251.9618.5427
 2.1039.8442 3.306.8442 3.847 0 6.9126-3.1357 6.9126-6.9347
 0-2.0502-.9016-3.8593-2.2843-5.186l.1805-.1808c.3605-.3618.9016-.603
 1.4426-.5427l.8414.0603V0h-1.4425c-1.683 0-3.0656 1.0251-3.6667
 2.4724-.6011-.181-1.2622-.3016-1.9234-.3016-3.847 0-6.9126
 3.1357-6.9126 6.9347 0 1.5076.481 2.9548 1.3225
 4.1005-.1203.1206-.3005.2412-.4208.3015l-.1803.181c-1.3826
 1.3266-2.0436 3.015-1.6832 4.9448.1805 1.025 1.0821 2.1105 1.9838
 2.7134.601.4222 1.3824.6031 2.1637.6031l5.7706-.2413c.6612 0
 1.2623.3015 1.6228.9046L16.4065
 24l3.5464-1.206-.6011-1.3268c-.9016-1.8692-2.765-3.0752-4.869-3.0752M12.0186
 5.8493c1.8033 0 3.306 1.5075 3.306 3.3165s-1.5027 3.3166-3.306
 3.3166-3.306-1.5075-3.306-3.3166c0-1.8693 1.4426-3.3166 3.306-3.3166"
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
