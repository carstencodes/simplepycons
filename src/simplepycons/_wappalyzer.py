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


class WappalyzerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wappalyzer"

    @property
    def original_file_name(self) -> "str":
        return "wappalyzer.svg"

    @property
    def title(self) -> "str":
        return "Wappalyzer"

    @property
    def primary_color(self) -> "str":
        return "#4608AD"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Wappalyzer</title>
     <path d="M24 11.014v-.604L12 1.805 0 10.41v.603l12 8.606
 12-8.605zM8.634 10.82l2.75 1.07.016-.01-1.526-1.967.984-.72 2.695
 1.116.016-.011-1.463-2.018 1.247-.913 2.6
 3.85-1.046.766-2.797-1.157-.012.008 1.593 2.038-1.048.767-5.26-1.903
 1.251-.916zm14.418 1.488l.947.679v.603l-12 8.605L0
 13.59v-.603l.947-.678 10.761 7.717.292.21.291-.21 10.762-7.717z" />
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
