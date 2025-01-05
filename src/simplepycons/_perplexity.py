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


class PerplexityIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "perplexity"

    @property
    def original_file_name(self) -> "str":
        return "perplexity.svg"

    @property
    def title(self) -> "str":
        return "Perplexity"

    @property
    def primary_color(self) -> "str":
        return "#1FB8CD"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Perplexity</title>
     <path d="M22.3977 7.0896h-2.3106V.0676l-7.5094
 6.3542V.1577h-1.1554v6.1966L4.4904
 0v7.0896H1.6023v10.3976h2.8882V24l6.932-6.3591v6.2005h1.1554v-6.0469l6.9318
 6.1807v-6.4879h2.8882V7.0896zm-3.4657-4.531v4.531h-5.355l5.355-4.531zm-13.2862.0676
 4.8691 4.4634H5.6458V2.6262zM2.7576 16.332V8.245h7.8476l-6.1149
 6.1147v1.9723H2.7576zm2.8882
 5.0404v-3.8852h.0001v-2.6488l5.7763-5.7764v7.0111l-5.7764
 5.2993zm12.7086.0248-5.7766-5.1509V9.0618l5.7766
 5.7766v6.5588zm2.8882-5.0652h-1.733v-1.9723L13.3948
 8.245h7.8478v8.087z" />
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
