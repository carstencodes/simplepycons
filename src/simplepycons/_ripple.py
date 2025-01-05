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


class RippleIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "ripple"

    @property
    def original_file_name(self) -> "str":
        return "ripple.svg"

    @property
    def title(self) -> "str":
        return "Ripple"

    @property
    def primary_color(self) -> "str":
        return "#0085C0"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Ripple</title>
     <path d="M20.55
 14.65c-.846-.486-1.805-.632-2.752-.666-.79-.023-1.974-.541-1.974-1.985
 0-1.072.868-1.94 1.985-1.985.947-.034 1.906-.18 2.752-.666A5.018
 5.018 0 0022.4 2.502 5.04 5.04 0 0015.53.674a4.993 4.993 0 00-2.504
 4.343c0 .97.35 1.861.79 2.696.372.699.553 1.996-.71
 2.73-.948.54-2.132.202-2.719-.745-.496-.801-1.094-1.545-1.94-2.03C6.045
 6.28 2.977 7.104 1.6 9.495A5.018 5.018 0 003.44 16.34a5.025 5.025 0
 005.008 0c.846-.485 1.444-1.23 1.94-2.03.406-.654 1.433-1.489
 2.718-.744.948.541 1.241 1.737.711 2.73-.44.823-.79 1.725-.79
 2.695A5.011 5.011 0 0018.034 24a5.011 5.011 0 005.008-5.008 4.982
 4.982 0 00-2.492-4.343z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://brand.ripple.com/document/44#/foundat'''
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
