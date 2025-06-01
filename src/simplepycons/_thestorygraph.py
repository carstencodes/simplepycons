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


class TheStorygraphIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "thestorygraph"

    @property
    def original_file_name(self) -> "str":
        return "thestorygraph.svg"

    @property
    def title(self) -> "str":
        return "The StoryGraph"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>The StoryGraph</title>
     <path d="M18.1722.6246a.6788.6788 0 0 0-.1314.0252L14.095
 1.818c-.3504.1039-.545.4673-.4413.8178l5.1137
 17.3544c.104.3505.4673.5452.8178.4414l3.9455-1.1553c.3504-.1038.5451-.4673.4413-.8178L18.8584
 1.0911a.6522.6522 0 0 0-.6862-.4665zM.662 1.0522c-.3634
 0-.6619.2986-.6619.662v18.0944c0
 .3634.2985.6619.662.6619h4.1143c.3634 0
 .6619-.2985.6619-.662V1.7143c0-.3634-.2985-.662-.6619-.662zm6.9438
 0c-.3634 0-.662.2986-.662.662v18.0944c0
 .3634.2986.6619.662.6619H11.72c.3634 0
 .649-.2985.662-.662V1.7143c0-.3634-.2986-.662-.662-.662zM.3634
 21.431c-.1947 0-.3634.1558-.3634.3634v1.2202c0
 .1948.1558.3635.3634.3635h23.2712c.1947 0
 .3635-.1558.3635-.3635v-1.2202c0-.1947-.1557-.3634-.3635-.3634z" />
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
