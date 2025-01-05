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


class SimplexIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "simplex"

    @property
    def original_file_name(self) -> "str":
        return "simplex.svg"

    @property
    def title(self) -> "str":
        return "SimpleX"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SimpleX</title>
     <path d="m16.1 0-4.026 4.025L8.125.076 6.113 2.09l3.95
 3.947-3.975 3.977L2.14 6.066.109 8.096l3.948 3.947L0 16.1l1.975 1.972
 4.056-4.056 3.95 3.947 2.029-2.027-3.95-3.95 3.975-3.972 3.951
 3.949-4.025 4.023v.002L9.947 18l-4.023 4.025L7.896 24l4.026-4.025
 3.95 3.949 2.013-2.014-3.951-3.95 4.027-4.024 3.95 3.949
 2.013-2.012-3.95-3.95L24 7.899l-1.975-1.972L18 9.949 14.049
 6l4.025-4.025z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/simplex-chat/simplex-chat/
blob/2f730d54e9858452e87e641b7fd618c669da68aa/website/src/img/new/logo'''

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
