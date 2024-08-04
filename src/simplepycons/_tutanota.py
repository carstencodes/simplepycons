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


class TutanotaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "tutanota"

    @property
    def original_file_name(self) -> "str":
        return "tutanota.svg"

    @property
    def title(self) -> "str":
        return "Tutanota"

    @property
    def primary_color(self) -> "str":
        return "#840010"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Tutanota</title>
     <path d="M2.158.934C.978.934.025 1.895.023 3.08.017 9.74.005
 16.413 0 23.066c.793-.297 1.67-.56 2.56-.918 6.188-2.485 11.249-4.598
 11.253-6.983a1.66 1.66 0 0
 0-.016-.23c-.32-2.356-5.916-3.087-5.908-4.166a.37.37 0 0 1
 .05-.177c.673-1.184 3.336-1.128 4.316-1.212.982-.085 3.285-.067
 3.397-.773a.44.44 0 0 0
 .005-.065c.003-.656-1.584-.913-1.584-.913s1.925.29 1.92
 1.042a.445.445 0 0 1-.015.114c-.207.81-1.901.962-3.021
 1.017-1.06.054-2.673.175-2.679.695 0 .03.005.062.015.095.253.76 6.167
 1.127 9.95 3.102 2.178 1.136 3.26 3.004 3.757 4.974V3.08A2.14 2.14 0
 0 0 21.866.934H2.158Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/tutao/tutanota/blob/8ff5f0'''

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
