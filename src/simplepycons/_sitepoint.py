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


class SitepointIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sitepoint"

    @property
    def original_file_name(self) -> "str":
        return "sitepoint.svg"

    @property
    def title(self) -> "str":
        return "SitePoint"

    @property
    def primary_color(self) -> "str":
        return "#258AAF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>SitePoint</title>
     <path d="M2.471 10.533l1.771 1.688 5.598 5.141
 2.4-2.291c.21-.297.194-.705-.046-.985L9.99
 12.184l.01-.005-2.371-2.266c-.279-.314-.27-.78.021-1.079l6.39-6.076L11.146
 0 2.475 8.238c-.664.633-.664 1.66 0 2.295h-.004zm19.056
 2.937l-1.77-1.691-5.595-5.142-2.411
 2.291c-.221.3-.207.705.045.985l2.205 1.891h-.006l2.369
 2.265c.27.314.27.766-.029 1.064l-6.391 6.075L12.855
 24l8.67-8.238c.664-.633.666-1.659 0-2.295l.002.003z" />
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
