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


class SnapcraftIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "snapcraft"

    @property
    def original_file_name(self) -> "str":
        return "snapcraft.svg"

    @property
    def title(self) -> "str":
        return "Snapcraft"

    @property
    def primary_color(self) -> "str":
        return "#82BEA0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Snapcraft</title>
     <path d="M13.804 13.367V5.69l5.292 2.362-5.292 5.315zM3.701
 23.514l6.49-12.22 2.847 2.843L3.7 23.514zM0 .486l13.355 4.848v8.484L0
 .486zM21.803 5.334H14.11L24 9.748z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/snapcore/snap-store-badges'''

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
