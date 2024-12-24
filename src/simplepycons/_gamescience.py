#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class GameScienceIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "gamescience"

    @property
    def original_file_name(self) -> "str":
        return "gamescience.svg"

    @property
    def title(self) -> "str":
        return "Game Science"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Game Science</title>
     <path d="M1.847
 19.089c-.555-.137-.853-.305-1.213-.685-.613-.645-.76-1.273-.534-2.287.394-1.77
 1.645-3.34 3.321-4.166 1.03-.508 1.64-.657 2.693-.656.759 0 .928.027
 1.325.212l.456.213 4.263-2.841c2.344-1.563 4.276-2.828
 4.294-2.81s-.177.987-.431 2.155c-.254 1.169-.462 2.176-.462 2.24 0
 .063 1.865-1.167 4.144-2.734 4.153-2.856 4.42-3.037
 4.265-2.883-.268.266-10.33 8.653-10.353
 8.63-.015-.017.174-1.036.419-2.267s.436-2.28.426-2.334c-.011-.053-1.231.964-2.712
 2.26l-2.693 2.356-.053.765c-.17 2.428-2.022 4.156-5.168
 4.823-.69.146-1.42.15-1.987.009" />
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