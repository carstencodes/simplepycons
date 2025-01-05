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


class RedbubbleIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "redbubble"

    @property
    def original_file_name(self) -> "str":
        return "redbubble.svg"

    @property
    def title(self) -> "str":
        return "Redbubble"

    @property
    def primary_color(self) -> "str":
        return "#E41321"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Redbubble</title>
     <path d="M16.633 16.324h-3.199a.321.321 0 0
 1-.32-.322V7.974a.32.32 0 0 1 .32-.32H16.4c2.226 0 2.693 1.31 2.693
 2.408 0 .636-.169 1.14-.504 1.511.816.337 1.256 1.096 1.256 2.194 0
 1.601-1.201 2.557-3.212 2.557m-4.644 0H5.345a.32.32 0 0
 1-.32-.322V7.974a.32.32 0 0 1 .32-.32h3.103c1.939 0 3.096 1.043 3.096
 2.791 0 1.163-.585 2.077-1.527 2.448l2.21 2.897a.322.322 0 0
 1-.24.533M12 0C5.373 0 0 5.373 0 12s5.373 12 12 12c6.628 0 12-5.373
 12-12S18.63 0 12.001 0" />
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
