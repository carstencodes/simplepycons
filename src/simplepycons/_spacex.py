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


class SpacexIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "spacex"

    @property
    def original_file_name(self) -> "str":
        return "spacex.svg"

    @property
    def title(self) -> "str":
        return "SpaceX"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SpaceX</title>
     <path d="M24 7.417C8.882 8.287 1.89 14.75.321 16.28L0
 16.583h2.797C10.356 9.005 21.222 7.663 24 7.417zm-17.046
 6.35c-.472.321-.945.68-1.398 1.02l2.457 1.796h2.778zM2.948
 10.8H.189l3.25 2.381c.473-.321 1.02-.661 1.512-.945Z" />
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
