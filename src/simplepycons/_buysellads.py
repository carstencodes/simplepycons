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


class BuyselladsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "buysellads"

    @property
    def original_file_name(self) -> "str":
        return "buysellads.svg"

    @property
    def title(self) -> "str":
        return "BuySellAds"

    @property
    def primary_color(self) -> "str":
        return "#EB4714"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>BuySellAds</title>
     <path d="M24 16.4h-2.685l-.716-2.704-3.3
 2.704h-2.675l2.796-8.821h3.784zm-5.955-2.785h2.544l-1.272-4.744zM5.581
 11.849c.939.151 1.676 1.049 1.676 2.149 0 1.282-.677 2.392-2.403
 2.392H0V7.579h4.32c1.736 0 2.573 1.141 2.573 2.251 0 1.09-.474
 1.837-1.312 2.019m-3.502 2.634 1.988-.01c.535 0 .868-.313.868-.788
 0-.434-.313-.787-.868-.787H2.079zm0-4.986v1.463h1.726c.464 0
 .777-.302.777-.736 0-.424-.313-.727-.777-.727zm7.953.454c0 1.302
 4.582.202 4.592 3.714 0 1.756-1.171 2.967-3.512 2.967-1.413
 0-2.604-.333-3.492-.938l.888-1.938c.676.525 1.524.898 2.675.898.777 0
 1.15-.302 1.15-.716 0-1.443-4.622-.051-4.612-3.795.01-1.463
 1.312-2.775 3.552-2.775 1.272 0 2.523.242 3.502.867l-.837
 1.928c-.919-.615-1.867-.908-2.735-.888-.656.02-1.171.212-1.171.676"
 />
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
