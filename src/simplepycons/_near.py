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


class NearIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "near"

    @property
    def original_file_name(self) -> "str":
        return "near.svg"

    @property
    def title(self) -> "str":
        return "NEAR"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>NEAR</title>
     <path d="M21.443 0c-.89 0-1.714.46-2.18 1.218l-5.017
 7.448a.533.533 0 0 0 .792.7l4.938-4.282a.2.2 0 0 1
 .334.151v13.41a.2.2 0 0 1-.354.128L5.03.905A2.555 2.555 0 0 0 3.078
 0h-.521A2.557 2.557 0 0 0 0 2.557v18.886a2.557 2.557 0 0 0 4.736
 1.338l5.017-7.448a.533.533 0 0 0-.792-.7l-4.938 4.283a.2.2 0 0
 1-.333-.152V5.352a.2.2 0 0 1 .354-.128l14.924 17.87c.486.574 1.2.905
 1.952.906h.521A2.558 2.558 0 0 0 24 21.445V2.557A2.558 2.558 0 0 0
 21.443 0Z" />
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
