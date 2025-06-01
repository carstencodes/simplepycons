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


class MetagerIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "metager"

    @property
    def original_file_name(self) -> "str":
        return "metager.svg"

    @property
    def title(self) -> "str":
        return "MetaGer"

    @property
    def primary_color(self) -> "str":
        return "#F47216"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>MetaGer</title>
     <path d="M1.563 0v6.92h2.083c.818 0 1.227-.434
 1.227-1.289V3.264h10.391c3.035 0 4.552 1.613 4.552
 4.736v2.575H4.873v1.562c0 .851-.412 1.288-1.227 1.288H.827v4.23C.827
 21.885 2.942 24 7.218 24h8.46c4.965 0 7.494-2.575
 7.494-7.678V7.678C23.172 2.575 20.643 0 15.678 0zm8.706
 13.425h2.246c1.513 0 2.089.777 2.089 2.226v3.389c0 1.15-.577
 1.747-1.705 1.747h-1.16c-.976 0-1.47-.578-1.47-1.726v-5.636" />
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
