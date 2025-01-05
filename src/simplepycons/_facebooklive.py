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


class FacebookLiveIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "facebooklive"

    @property
    def original_file_name(self) -> "str":
        return "facebooklive.svg"

    @property
    def title(self) -> "str":
        return "Facebook Live"

    @property
    def primary_color(self) -> "str":
        return "#ED4242"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Facebook Live</title>
     <path d="M9.4777 7.8108a.4611.4611 0 0 0-.462.462v7.452a.461.461
 0 0 0 .462.462H23.538v.0024a.4611.4611 0 0 0
 .462-.462V8.2728a.4611.4611 0 0 0-.462-.462zm-5.2862.0072C1.879 7.818
 0 9.6922 0 12.007c0 2.0922 1.533 3.8267 3.5376
 4.1394V13.218h-1.071v-1.211h1.071v-.924c0-1.0497.6208-1.6326
 1.578-1.6326.4573 0 .9336.0877.9336.0877v1.0236h-.5237c-.5213
 0-.6871.327-.6871.6563v.7866h1.1634l-.1872
 1.2108H4.836v2.9286c2.0093-.3104 3.5447-2.0448 3.5447-4.137
 0-2.315-1.8766-4.1891-4.1892-4.1891zm7.1676
 2.4073h.635v2.9926h1.6278v.5544H11.359zm2.9452
 0h.635v3.547h-.635zm1.2439 0h.7014l.8932
 2.8078h.0427l.8862-2.8078h.6752l-1.2273
 3.547h-.7322zm3.81.0024h2.296v.5473h-1.6609v.9407h1.5709v.5165h-1.5709v.9928h1.661v.5497h-2.296Z"
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
