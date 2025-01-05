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


class ComicfuryIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "comicfury"

    @property
    def original_file_name(self) -> "str":
        return "comicfury.svg"

    @property
    def title(self) -> "str":
        return "ComicFury"

    @property
    def primary_color(self) -> "str":
        return "#79BD42"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ComicFury</title>
     <path d="m0 6.959 1.899-3.256 2.725 2.736 2.973-.204L9.3
 3.297l2.213 2.693 8.655-.252.406-1.085L24 5.128v5.268l-11.248
 3.526-1.085 6.781H0V6.959zm2.195-.748L1.041 8.137l1.75 1.748
 1.133-1.948-1.729-1.726zm7.409-.448L8.48 7.546l1.224 1.598
 1.137-1.766-1.237-1.615zm3.901 3.751-1.992.349.997
 2.025.995-2.374zm3.319-.565-1.992.348.996
 2.025.996-2.373zm3.228-.611-1.991.349.996
 2.025.995-2.374zm3.183-.566-1.992.349.996 2.025.996-2.374z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://comicfury.com/images/gator-icon-black'''

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
