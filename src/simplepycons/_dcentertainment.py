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


class DcEntertainmentIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "dcentertainment"

    @property
    def original_file_name(self) -> "str":
        return "dcentertainment.svg"

    @property
    def title(self) -> "str":
        return "DC Entertainment"

    @property
    def primary_color(self) -> "str":
        return "#0078F0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>DC Entertainment</title>
     <path d="M5.215 8.787h2.154c.601 0 1.088.487 1.088 1.088v4.954c0
 .6-.487 1.088-1.088 1.088H6.05V9.475a.159.159 0 00-.066-.129zM12
 23.099a11.078 11.078 0 01-8.659-4.155.046.046 0
 01.036-.074h5.936a.26.26 0 00.153-.05l2.27-1.648a.159.159 0
 00.064-.128V7.616a.159.159 0 00-.065-.129L9.466 5.84a.261.261 0
 00-.153-.05H2.886a.046.046 0 01-.037-.071A11.087 11.087 0 0112
 .9c3.798 0 7.15 1.907 9.151 4.817a.046.046 0 01-.038.071h-1.597c-.052
 0-.1.03-.123.079l-.353.757-1.082-.786a.26.26 0
 00-.153-.05h-2.553a.261.261 0 00-.154.05L12.83 7.487a.159.159 0
 00-.065.129v9.428c0 .05.024.098.065.128l2.27 1.648a.26.26 0
 00.153.05h5.371c.038 0 .06.045.036.074A11.078 11.078 0 0112
 23.1zM1.602 8.3l1.038.755c.043.03.068.08.068.132v8.73c0
 .046-.06.063-.084.025A11.046 11.046 0 01.901
 12c0-1.289.22-2.526.624-3.677a.05.05 0
 01.077-.024zm13.67.488h3.225v1.776c0
 .046.038.084.084.084h2.701a.098.098 0
 00.096-.083l.535-3.374c.007-.044.066-.053.086-.013a11.053 11.053 0
 011.1 4.823 11.05 11.05 0 01-1.39
 5.382c-.022.04-.084.024-.084-.023v-3.084a.084.084 0
 00-.084-.084h-2.96a.084.084 0 00-.084.084v1.642h-1.301a1.089 1.089 0
 01-1.089-1.088V9.475a.159.159 0 00-.065-.129zM12 0C5.373 0 0 5.373 0
 12s5.373 12 12 12 12-5.373 12-12S18.627 0 12 0Z" />
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
